import streamlit as st
import random
from questions import QuestionBank
from utils import format_question
from utils import calculate_score

def main():
    st.title("Tech Trivia Game")
    st.markdown("Test your knowledge about tech history, famous programmers, coding terms, and current tech trends!")

    st.write("**Instructions:**")
    st.write("1. Select the number of questions you want to answer.")
    st.write("2. Read the questions and choose the correct answer from the options.")
    st.write("3. After answering all questions, click the 'Submit' button to see the results.")
    st.write("4. Use the 'Explain' button to view detailed explanations from DeepSeek LLM.")

    num_questions = st.selectbox("Select number of questions", [1, 2, 3, 4, 5])

    if st.button("Start Game"):
        st.session_state.num_questions = num_questions
        st.session_state.score = 0
        question_bank = QuestionBank()
        question_bank.load_questions()
        random.shuffle(question_bank.questions)
        st.session_state.questions = question_bank.questions[:num_questions]
        st.session_state.user_answers = [None] * num_questions
        st.session_state.submitted = False
        st.session_state.show_explanation = [False] * num_questions

    if 'questions' in st.session_state and not st.session_state.submitted:
        total_questions = st.session_state.num_questions

        for i in range(total_questions):
            st.write(f"**Question {i + 1}:**")
            print(f"Question {i + 1}:")
            st.write(format_question(st.session_state.questions[i]))
            print(f"{st.session_state.questions[i]['question']}")

            # Display multiple-choice options
            options = st.session_state.questions[i]['options']
            st.session_state.user_answers[i] = st.radio(
                "Choose an answer:",
                options,
                key=f"user_answer_{i}",
                index=None
            )

        if st.button("Submit Answers"):
            st.session_state.submitted = True
            st.session_state.score = calculate_score(st.session_state.questions, st.session_state.user_answers)

    if 'submitted' in st.session_state and st.session_state.submitted:
        total_questions = st.session_state.num_questions
        score_text = f"Game Over! Your final score is {st.session_state.score}/{total_questions}"
 
        st.markdown(f"""
    <div style="background-color: #28a745; color: white; padding: 10px; border-radius: 10px; font-size: 18px;">
        {score_text}
    </div>
    """, unsafe_allow_html=True)
       
        st.write("")
        st.write("")

        for i in range(total_questions):
            col1, col2 = st.columns([8, 2])  # Use two columns for layout (question + explain button)
            with col1:
                st.write(f"**Question {i + 1}:** {format_question(st.session_state.questions[i])}")
                st.write(f"**Your Answer:** {st.session_state.user_answers[i]}")
                if st.session_state.user_answers[i] == st.session_state.questions[i]['answer']:
                    st.success("Correct!")
                else:
                    st.error("Wrong!")
                st.write(f"**Correct Answer:** {st.session_state.questions[i]['answer']}")

            with col2:
                if st.button("Explain", key=f"explain_button_{i}"):
                    st.session_state.show_explanation[i] = True

            if st.session_state.show_explanation[i]:
                explanation = QuestionBank.explain(st.session_state.questions[i], st.session_state.user_answers[i], st.session_state.questions[i]['answer'])
                st.text_area("Explanation:", explanation, key=f"explanation_{i}")

            print("\n")
            print(f"Question {i + 1}: {st.session_state.questions[i]['question']}")
            print(f"Your Answer: {st.session_state.user_answers[i]}")
            print(f"Correct Answer: {st.session_state.questions[i]['answer']}")

            st.write("---")

if __name__ == "__main__":
    main()
