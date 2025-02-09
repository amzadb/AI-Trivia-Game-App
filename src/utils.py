def format_question(question):
    return f"**{question['question']}**"

def calculate_score(questions, user_answers):
    score = 0
    for question, user_answer in zip(questions, user_answers):
        if question['answer'].strip().lower() == user_answer.strip().lower():
            score += 1
    return score