import random

def _question_key(operator, left, right):
    """Put the smaller number first for addition and multiplication.

    Keep the original order for subtraction so 5 - 3 and 3 - 5
    count as different questions.
    """
    
    if operator in ("+", "*") and left > right:
        left, right = right, left
    return operator, left, right

def build_challenge_plan(round_number, recent_questions, count):
    """Make math questions for the current round.

    Args:
        round_number (int): The round number, starting at 1. The biggest
            number in a question is the round number times 5.
        recent_questions (list[tuple]): Questions used recently, written
            as (operator, left, right) tuples.
        count (int): How many questions to make.

    Returns:
        list[dict]: The questions for the round. Each has an operator,
            two numbers, an answer, and a difficulty level. Questions
            that haven't been used recently come first. If we run
            through all the possible questions, we start the list over.

    Raises:
        ValueError: If the round number or question count is less than 1.
    """


    if round_number < 1 or count < 1:
        raise ValueError("Round number and question count must both be positive.")
    
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