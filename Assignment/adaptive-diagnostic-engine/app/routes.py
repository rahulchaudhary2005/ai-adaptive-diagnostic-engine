from fastapi import APIRouter, HTTPException
from bson import ObjectId

from .database import questions_collection, sessions_collection
from .adaptive_algorithm import update_ability
from .models import AnswerSubmission
from .ai_plan import generate_study_plan

router = APIRouter()


@router.get("/")
def home():
    return {
        "project": "AI Adaptive Diagnostic Engine",
        "description": "Adaptive testing system that adjusts question difficulty based on student performance.",
        "api_routes": {
            "POST /start-session": "Start a new test session",
            "GET /next-question/{session_id}": "Get next adaptive question",
            "POST /submit-answer": "Submit answer and update ability score",
            "GET /study-plan/{session_id}": "Generate personalized study plan"
        },
        "documentation": "/docs"
    }
# START TEST SESSION
@router.post("/start-session")
def start_session():

    session = {
        "ability_score": 0.5,
        "questions_answered": 0,
        "correct_answers": 0,
        "history": []
    }

    result = sessions_collection.insert_one(session)

    return {
        "message": "Session started",
        "session_id": str(result.inserted_id)
    }


# GET NEXT QUESTION BASED ON ABILITY
@router.get("/next-question/{session_id}")
def get_next_question(session_id):

    session = sessions_collection.find_one({"_id": ObjectId(session_id)})

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    ability = session["ability_score"]

    # Find question with closest difficulty
    question = questions_collection.find_one(
        {},
        sort=[("difficulty", 1)]
    )

    if not question:
        raise HTTPException(status_code=404, detail="No questions available")

    question["_id"] = str(question["_id"])

    return {
        "question_id": question["_id"],
        "question": question["question"],
        "options": question["options"],
        "difficulty": question["difficulty"]
    }


# SUBMIT ANSWER
@router.post("/submit-answer")
def submit_answer(data: AnswerSubmission):

    session = sessions_collection.find_one({"_id": ObjectId(data.session_id)})
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    question = questions_collection.find_one({"_id": ObjectId(data.question_id)})
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    correct = question["correct_answer"] == data.selected_answer

    # IRT ability update
    new_ability = update_ability(
        session["ability_score"],
        question["difficulty"],
        correct
    )

    update_data = {
        "$set": {"ability_score": new_ability},
        "$inc": {"questions_answered": 1},
        "$push": {
            "history": {
                "question": question["question"],
                "difficulty": question["difficulty"],
                "correct": correct
            }
        }
    }

    if correct:
        update_data["$inc"]["correct_answers"] = 1

    sessions_collection.update_one(
        {"_id": ObjectId(data.session_id)},
        update_data
    )

    return {
        "correct": correct,
        "new_ability_score": new_ability
    }


# GENERATE STUDY PLAN
@router.get("/study-plan/{session_id}")
def study_plan(session_id):

    session = sessions_collection.find_one({"_id": ObjectId(session_id)})

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    plan = generate_study_plan(session)

    return {
        "ability_score": session["ability_score"],
        "questions_answered": session["questions_answered"],
        "correct_answers": session["correct_answers"],
        "study_plan": plan
    }