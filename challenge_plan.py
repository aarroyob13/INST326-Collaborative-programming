import random

def _question_key(operator, left, right):
    """Return a comparison key for an arithmetic question."""
    if operator in ("+", "*") and left > right:
        left, right = right, left
    return operator, left, right

def build_challenge_plan(round_number, recent_questions, count):
    """Generate arithmetic questions for the current round."""
    max_operand = round_number * 5
    questions = []
    recent_keys = set()
    for operator, left, right in recent_questions:
        recent_keys.add(_question_key(operator, left, right))

    fresh_questions = []
    repeated_questions = []

    for operator in ("+", "-", "*"):
        for left in range(1, max_operand + 1):
            for right in range(1, max_operand + 1):
                key = _question_key(operator, left, right)

                if key != (operator, left, right):
                    continue

                if key in recent_keys:
                    repeated_questions.append(key)
                else:
                    fresh_questions.append(key)

    random.shuffle(fresh_questions)
    random.shuffle(repeated_questions)
    candidates = fresh_questions + repeated_questions

    for index in range(count):
        operator, left, right = candidates[index % len(candidates)]

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