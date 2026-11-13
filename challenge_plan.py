import random


def build_challenge_plan(round_number, recent_questions, count):
    """Generate arithmetic questions for the current round."""
    max_operand = round_number * 5
    questions = []

    for _ in range(count):
        left = random.randint(1, max_operand)
        right = random.randint(1, max_operand)

        operator = random.choice(["+", "-", "*"])

        if operator == "+":
            answer = left + right
        elif operator == "-":
            answer = left - right
        else:
            answer = left * right

        questions.append({
            "operator": operator,
            "left": left,
            "right": right,
            "answer": answer,
            "difficulty": round_number,
        })

    return questions