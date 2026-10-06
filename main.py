from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="Genie")


class Question(BaseModel):
    task: str
    question: str


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/ask")
def ask_question(data: Question):

    q = data.question

    if data.task == "Explain":
        answer = f"Explanation: {q} is explained in simple terms. It is an important concept to understand and practice."

    elif data.task == "Q&A":
        answer = f"Answer: Your question is about {q}. This is a useful topic to learn with examples and practice."

    elif data.task == "Quiz":
        answer = f"Quiz: Let's test your knowledge about {q}. Think about its definition, uses, and examples."

    elif data.task == "Summary":
        answer = f"Summary: {q} is an important topic. Learn its basic meaning, main features, uses, and examples."

    elif data.task == "Recommend Path":
        answer = f"Learning Path: Start with the basics of {q}, then learn examples, practice exercises, and finally build a small project."

    else:
        answer = "Please select a task."

    return {
        "question": q,
        "answer": answer
    }