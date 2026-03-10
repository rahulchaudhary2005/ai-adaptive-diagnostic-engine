def generate_study_plan(session_data):

    ability = session_data["ability_score"]
    correct = session_data["correct_answers"]
    total = session_data["questions_answered"]

    if ability < 0.4:
        plan = [
            "1. Review fundamental concepts of the subject.",
            "2. Practice basic level problems daily.",
            "3. Focus on understanding mistakes from incorrect answers."
        ]

    elif ability < 0.7:
        plan = [
            "1. Practice medium difficulty questions.",
            "2. Strengthen weak topics identified during the test.",
            "3. Solve timed quizzes to improve accuracy."
        ]

    else:
        plan = [
            "1. Attempt advanced level problems.",
            "2. Focus on speed and optimization strategies.",
            "3. Practice full-length mock tests."
        ]

    return plan