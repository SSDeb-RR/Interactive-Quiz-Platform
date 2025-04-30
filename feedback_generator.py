import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"),model_name="llama-3.3-70b-versatile")

def generate_feedback(incorrect_questions):
    prompt = f"""
    You are an expert tutor. Analyze the following MCQs that a user got wrong. Identify the underlying topics,
    and give the user concise advice on which concepts to review and why.

    Questions and user answers:
    {json.dumps(incorrect_questions, indent=2)}

    Respond as a tutor giving feedback.
    """

    response = llm([HumanMessage(content=prompt)])
    return response.content
