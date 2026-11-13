import random


def build_challenge_plan(round_number, recent_questions, count):
    """Generate arithmetic questions for the current round."""
    max_operand = round_number * 5
    questions = []

    for _ in range(count):
        left = random.randint(1, max_operand)
        right = random.randint(1, max_operand)

        questions.append({
            "operator": "+",
            "left": left,
            "right": right,
            "answer": left + right,
            "difficulty": round_number,
        })

    return questions