def format_question(question):
    return f"**{question['question']}**"

# def calculate_score(correct_answers, total_questions):
#     if total_questions == 0:
#         return 0
#     return (correct_answers / total_questions) * 100

def calculate_score(questions, user_answers):
    score = 0
    for question, user_answer in zip(questions, user_answers):
        if question['answer'].strip().lower() == user_answer.strip().lower():
            score += 1
    return score