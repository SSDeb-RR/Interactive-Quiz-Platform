
# 🎯 Interactive Data Science Quiz Platform

An **AI-powered interactive quiz platform** for Data Science enthusiasts that dynamically generates quizzes based on your **chosen topic** and **skill level**. Built using a pre-tagged **JSON dataset**, fine-tuned LLMs (DeepSeek-v1 7B via Ollama), and an intuitive **Streamlit** front-end. Includes **personalized feedback generation** using LLM reasoning for every quiz session.

---

## 🧠 Project Overview

This tool is designed for learners who want to assess and improve their knowledge in **Machine Learning, Deep Learning, Python**, and other Data Science domains. It uses a large dataset of hand-curated questions, automatically tagged using an LLM with metadata like **topic** and **difficulty level**.

Users select their desired topic and proficiency level, and the system generates a personalized quiz. After completion, the LLM reviews incorrect answers and generates tailored feedback to help the user improve — making it a **smart learning companion**, not just a quiz app.

---

## 🧱 Technical Architecture

### Stage 1: Metadata Tagging
- **Input**: Raw dataset of Data Science questions (stored in JSON).
- **Output**: Each question is annotated with:
  - Topic (e.g., Python, ML, DL, etc.)
  - Difficulty (Easy, Medium, Hard)

> Questions were tagged using an LLM to enable topic-wise and difficulty-wise selection.

### Stage 2: Quiz Generation + Feedback Loop
- **User selects**:
  - Proficiency level (Easy/Medium/Hard)
  - Topic(s) of interest
- **Quiz Generator**:
  - Pulls matching questions from the local JSON dataset.
  - Presents questions one-by-one on the Streamlit interface.
- **Feedback Engine**:
  - After submission, incorrect answers are passed through the LLM.
  - Generates **personalized feedback** explaining:
    - Where the learner went wrong.
    - Suggestions for improvement or revision.

---

## ✨ Features

✅ Dynamic quiz generation based on **user proficiency & topic**  
✅ **LLM-powered tagging** of questions by topic and difficulty  
✅ **Automatic scoring** with real-time results  
✅ **LLM-generated personalized feedback** for incorrect answers  
✅ Minimal, clean UI built in **Streamlit**  
✅ Modular, extensible codebase with Langflow integration  

---

## 🛠️ Tech Stack

| Tool        | Use Case                                |
|-------------|------------------------------------------|
| **Streamlit** | Front-end quiz interface                 |
| **Langflow**  | Chain design and modular orchestration   |
| **Ollama**    | Local LLM inference with DeepSeek-v1 7B |
| **Python**    | Core logic and glue code                |
| **JSON**      | Local storage for the full question dataset |
| **LLM Prompting** | For tagging, quiz generation, and feedback |

---

## ⚙️ Setup Instructions

> Make sure you have [Ollama](https://ollama.com/) installed locally and DeepSeek-v1 model pulled:
```bash
ollama run deepseek-coder:7b
```

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/data-science-quiz-ai.git
cd data-science-quiz-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run main.py
```

---

## 📌 Future Improvements

- [ ] Add user authentication (login, history tracking)  
- [ ] Enhance question variety with broader JSON sources  
- [ ] Include visual and code-based interactive questions  
- [ ] Add timer support and difficulty progression  
- [ ] Let users bookmark questions for revision  

---

## 🤝 Who's This For?

Whether you're just starting out or preparing for interviews, this personalized quiz tool tailors itself to your **skill level**, **topics of interest**, and provides **detailed AI-generated feedback** — making your practice sessions more effective and actionable.

---
