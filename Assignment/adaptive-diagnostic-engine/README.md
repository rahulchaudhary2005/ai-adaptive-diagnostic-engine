# AI Adaptive Diagnostic Engine

An **AI-driven adaptive testing system** that dynamically adjusts question difficulty based on a student's performance.
The system simulates standardized adaptive exams such as **GRE and GMAT** using **Item Response Theory (IRT)** to estimate student ability and deliver appropriately difficult questions.

---

# Project Overview

Traditional exams provide the same questions to every student.
Adaptive testing improves assessment accuracy by selecting questions based on previous answers.

This project implements a **1-Dimensional Adaptive Testing Engine** that:

* Dynamically adjusts question difficulty
* Estimates student ability using **Item Response Theory (IRT)**
* Stores questions and sessions in **MongoDB**
* Provides REST APIs using **FastAPI**
* Generates **personalized study plans**

---

# API Documentation (Swagger UI)

FastAPI automatically generates interactive API documentation.

Recruiters can directly test all APIs.

Open:

```
http://localhost:8000/docs
```

### Screenshot

![API Documentation](docs/swagger-ui.png)

---

# System Architecture

```
                 +-----------------------+
                 |        Student        |
                 |   (Browser / Swagger) |
                 +-----------+-----------+
                             |
                             v
                 +-----------------------+
                 |      FastAPI Server   |
                 |  Adaptive Engine API  |
                 +-----------+-----------+
                             |
             +---------------+----------------+
             |                                |
             v                                v
     +---------------+               +------------------+
     |   MongoDB     |               |   Study Planner  |
     | Question Bank |               |  (Rule-Based AI) |
     +---------------+               +------------------+
```

---

# Adaptive Algorithm (IRT Model)

The system estimates student ability using **Item Response Theory (IRT)**.

Probability of answering correctly:

```
P(θ) = 1 / (1 + e^(-(θ - b)))
```

Where:

* **θ (theta)** → student ability
* **b** → question difficulty

Ability updates after each answer:

* Correct answer → ability increases
* Incorrect answer → ability decreases

This allows the engine to **adaptively converge to the student's actual skill level**.

---

# Database Design (MongoDB)

## Questions Collection

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
```

---

## User Session Collection

```
{
  "ability_score": 0.5,
  "questions_answered": 0,
  "correct_answers": 0,
  "history": []
}
```

This tracks a student's adaptive testing progress.

---

# API Endpoints

| Method | Endpoint                      | Description                      |
| ------ | ----------------------------- | -------------------------------- |
| GET    | `/`                           | API overview                     |
| POST   | `/start-session`              | Start adaptive test session      |
| GET    | `/next-question/{session_id}` | Fetch next adaptive question     |
| POST   | `/submit-answer`              | Submit answer and update ability |
| GET    | `/study-plan/{session_id}`    | Generate personalized study plan |

---

# Project Structure

```
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
```

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-adaptive-diagnostic-engine
```

Move into the project directory:

```
cd ai-adaptive-diagnostic-engine
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```
MONGO_URI=mongodb://localhost:27017
```

---

# Seed Database

Insert sample GRE-style questions into MongoDB.

```
python seed_db.py
```

---

# Run the Server

Start FastAPI server:

```
uvicorn app.main:app --reload
```

Open API documentation:

```
http://127.0.0.1:8000/docs
```

---

# Example Workflow

1️⃣ Start session

```
POST /start-session
```

2️⃣ Get adaptive question

```
GET /next-question/{session_id}
```

3️⃣ Submit answer

```
POST /submit-answer
```

4️⃣ Generate study plan

```
GET /study-plan/{session_id}
```

---

# Personalized Study Plan

After several responses, the engine analyzes performance and generates a study plan.

Example output:

```
1. Review algebra equation solving techniques
2. Practice medium difficulty algebra problems
3. Attempt timed mock tests to improve accuracy
```

---

# AI Development Log (Assignment Requirement)

AI tools were used to accelerate development:

* ChatGPT for architectural guidance
* AI assistance for debugging MongoDB queries
* AI-generated GRE-style dataset creation

Manual work was required for:

* Implementing Item Response Theory algorithm
* Designing adaptive difficulty selection logic
* Structuring MongoDB schemas

---

# Tech Stack

* FastAPI
* MongoDB
* Python
* Item Response Theory (IRT)
* REST API Architecture

---

# Author

**Rahul Kumar Chaudhary**
BTech CSE (AI & ML)
Full Stack + AI Developer
