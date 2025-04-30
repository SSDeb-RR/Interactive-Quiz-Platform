import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


def process_questions(raw_file_path, processed_file_path=None):
    with open(raw_file_path, encoding='utf-8') as file:
        qna_data = json.load(file)
        enriched_qna_data = []
        for qna in qna_data:
            qna_metadata = extract_metadata(qna)
            qna_with_metadata = qna | qna_metadata
            enriched_qna_data.append(qna_with_metadata)


    with open(processed_file_path, encoding='utf-8', mode="w") as outfile:
        json.dump(enriched_qna_data, outfile, indent=4)


def extract_metadata(qna):
    template = '''
    Given the following MCQ, identify its subject as one of ['Python', 'Machine Learning', 'Deep Learning']
    and its difficulty as one of ['Easy', 'Medium', 'Hard'].

    Question: {question}
    Options: {options}
    Answer: {answer}

    1. Return a valid JSON. No preamble. 
    2. JSON object should have exactly two keys: subject and difficulty. 
    '''

    # Step 1: Create prompt template with input variables
    pt = PromptTemplate(
        input_variables=["question", "options", "answer"],
        template=template
    )

    # Step 2: Create the chain
    chain = pt | llm

    # Step 3: Format the input dictionary
    input_data = {
        "question": qna["question"],
        "options": ', '.join(qna["options"]),
        "answer": qna["answer"]
    }

    # Step 4: Invoke chain with formatted input
    response = chain.invoke(input=input_data)

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")

    return res



process_questions("data/raw_questions.json", "data/tagged_questions.json")