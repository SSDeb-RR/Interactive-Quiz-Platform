import streamlit as st
import json
import random
from feedback_generator import generate_feedback

# Load questions
@st.cache_data
def load_questions():
    with open("data/tagged_questions.json") as f:
        return json.load(f)

def start_quiz():
    questions = load_questions()
    selected_subject = st.session_state.selected_subject
    selected_difficulty = st.session_state.selected_difficulty

    filtered_questions = [
        q for q in questions
        if q["subject"] == selected_subject and q["difficulty"] == selected_difficulty
    ]

    if len(filtered_questions) < 5:
        st.error("Not enough questions for the selected filters. Please try again.")
        return

    st.session_state.questions = random.sample(filtered_questions, 5)
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.incorrect_questions = []
    st.session_state.stage = "quiz"

def render_intro():
    st.title("🧠 Welcome to the Ultimate Data Science Quiz")

    subjects = ["Python", "Machine Learning", "Deep Learning"]
    difficulties = ["Easy", "Medium", "Hard"]

    st.write("### Please choose your subject and difficulty level:")
    selected_subject = st.selectbox("Select Subject:", subjects, key="subject_select")
    selected_difficulty = st.selectbox("Select Difficulty:", difficulties, key="difficulty_select")

    if st.button("Start Quiz"):
        st.session_state.selected_subject = selected_subject
        st.session_state.selected_difficulty = selected_difficulty
        start_quiz()
        st.session_state.stage = "quiz"
        st.rerun()

def render_question():
    questions = st.session_state.questions
    q_index = st.session_state.q_index

    if q_index < len(questions):
        question_data = questions[q_index]
        st.markdown(f"### Q{q_index + 1}: {question_data['question']}")
        options = question_data['options']
        correct_answer = question_data['answer']

        if f"answered_{q_index}" in st.session_state:
            selected_option = st.session_state.get(f"selected_option_{q_index}")
            st.radio("You selected:", options, index=options.index(selected_option), disabled=True, key=f"radio_disabled_{q_index}")
            if selected_option == correct_answer:
                st.success("Correct! ✅ +1 point")
            else:
                st.error(f"Incorrect ❌ (Correct: {correct_answer})")

            if q_index < len(questions) - 1:
                if st.button("Next"):
                    st.session_state.q_index += 1
                    st.rerun()
            else:
                if st.button("Finish"):
                    st.session_state.q_index += 1
                    st.rerun()
        else:
            selected_option = st.radio("Choose an option:", options, key=f"radio_{q_index}")
            if st.button("Submit"):
                st.session_state[f"selected_option_{q_index}"] = selected_option
                if selected_option == correct_answer:
                    st.success("Correct! ✅ +1 point")
                    st.session_state.score += 1
                else:
                    st.error(f"Incorrect ❌ (Correct: {correct_answer})")
                    question_data_with_selection = question_data.copy()
                    question_data_with_selection["selected"] = selected_option
                    st.session_state.incorrect_questions.append(question_data_with_selection)
                st.session_state[f"answered_{q_index}"] = True
                st.rerun()
    else:
        render_results()

def render_results():
    score = st.session_state.score
    total = len(st.session_state.questions)
    st.success(f"🎉 Quiz Completed! You scored {score}/{total}")
    st.balloons()

    if score == 5:
        st.info("Excellent! You're a pro! 🌟")
    elif score >= 3:
        st.info("Great job! Keep improving! 👍")
    else:
        st.info("Don't worry! Practice makes perfect. 💪")

    feedback = generate_feedback(st.session_state.incorrect_questions)
    st.markdown("### Detailed Feedback")
    st.write(feedback)

    if st.button("Restart Quiz"):
        st.session_state.clear()
        st.session_state.stage = "intro"
        st.rerun()

if "stage" not in st.session_state:
    st.session_state.stage = "intro"

if st.session_state.stage == "intro":
    render_intro()
elif st.session_state.stage == "quiz":
    render_question()
