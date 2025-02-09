# Trivia Game

Welcome to the Trivia Game project! This interactive trivia game is built using Streamlit and integrates with Amazon Bedrock to provide an engaging experience focused on tech history, famous programmers, coding terms, and current tech trends.

## Project Structure

```
trivia-game
├── src
│   ├── app.py                # Main entry point for the Streamlit 
│   ├── questions.py          # Manages trivia questions
│   └── utils.py              # Utility functions for the application
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd trivia-game
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Streamlit app with the following command:
   ```
   streamlit run src/app.py
   ```

## Features

- **Interactive Trivia:** Answer questions related to technology and programming.
- **Random Questions:** Get a random question from a curated question bank.
- **DeepSeek Integration:** Explanation for any question is retrieved from Ollama DeepSeek, after submitting the answers.
- **Score Calculation:** Track your score as after answering all the questions.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features!

## License

This project is licensed under the MIT License. See the LICENSE file for details.