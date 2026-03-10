# AI Adaptive Diagnostic Engine

An AI-driven adaptive testing prototype that dynamically adjusts question difficulty based on a student's previous responses.

This system simulates the logic used in standardized adaptive tests such as **GRE and GMAT**, using **Item Response Theory (IRT)** to estimate student ability and serve appropriately difficult questions.

---

## Project Overview

Traditional exams present the same questions to every student. Adaptive testing improves assessment accuracy by dynamically selecting questions based on the student’s performance.

This project implements a **1-Dimensional Adaptive Testing Engine** with:

- Dynamic question difficulty selection
- Ability estimation using Item Response Theory (IRT)
- MongoDB based question storage
- FastAPI backend APIs
- AI generated personalized study plan

---

## API Documentation (Swagger UI)

FastAPI automatically generates an interactive API documentation interface.

Recruiters can directly test the APIs using Swagger.

Access it at:
http://localhost:8000/docs



### Screenshot

![API Documentation](docs/swagger-ui.png)

---

## System Architecture
         +----------------------+
         |       Student        |
         |  (Client / Swagger)  |
         +----------+-----------+
                    |
                    v
         +----------------------+
         |      FastAPI API     |
         | Adaptive Engine Core |
         +----------+-----------+
                    |
    +---------------+---------------+
    |                               |
    v                               v
    +---------------+ +------------------+
| MongoDB | | AI Study Plan |
| Question Bank | | (Rule Based LLM) |
+---------------+ +------------------+

---

## Adaptive Algorithm (IRT Model)

The system estimates a student's ability using **Item Response Theory**.

Probability of answering correctly:

Where:

- θ = student ability
- b = question difficulty

Ability is updated after each response:

- If correct → ability increases
- If incorrect → ability decreases

This allows the system to **adaptively converge to the student's true proficiency level**.

---

## Database Design (MongoDB)

### Questions Collection

Example document:

```json
{
  "question": "Solve: 2x + 5 = 15",
  "options": ["3", "4", "5", "6"],
  "correct_answer": "5",
  "difficulty": 0.4,
  "topic": "Algebra",
  "tags": ["equation"]
}


Where:

- θ = student ability
- b = question difficulty

Ability is updated after each response:

- If correct → ability increases
- If incorrect → ability decreases

This allows the system to **adaptively converge to the student's true proficiency level**.

---

## Database Design (MongoDB)

### Questions Collection

Example document:

```json
{
  "question": "Solve: 2x + 5 = 15",
  "options": ["3", "4", "5", "6"],
  "correct_answer": "5",
  "difficulty": 0.4,
  "topic": "Algebra",
  "tags": ["equation"]
}

adaptive-diagnostic-engine
│
├── app
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── adaptive_algorithm.py
│   ├── ai_plan.py
│   └── models.py
│
├── data
│   └── seed_questions.json
│
├── docs
│   └── swagger-ui.png
│
├── seed_db.py
├── requirements.txt
├── .env
└── README.md

install dependency  pip install -r requirements.txt

Run the Server

Start FastAPI server:

uvicorn app.main:app --reload

Open API documentation:

http://127.0.0.1:8000/docs