# AI Interview Assistant

## Project Description

AI Interview Assistant is an AI-powered web application that helps users prepare for interviews by generating interview questions and sample answers based on their job role, skills, experience, and selected difficulty level.

## Features

- Generate AI-based interview questions
- Select interview difficulty
- Enter job role and skills
- Provide project or experience details
- Generate sample answers
- Uses candidate information as context
- Simple and user-friendly interface
- Basic input and error handling

## Technologies Used

- Python
- Streamlit
- Google Gemini API

## Workflow

User Details
↓
Prompt Design
↓
Gemini AI API
↓
Context Handling
↓
Response Generation
↓
Interview Questions and Sample Answers

## How to Run

1. Install the required packages:

   pip install -r requirements.txt

2. Run the application:

   streamlit run app.py

3. Enter your Gemini API key.
4. Enter the job role and skills.
5. Enter your experience or project details.
6. Select the difficulty level.
7. Select the number of questions.
8. Click "Generate Interview Questions".

## Expected Outcome

The application generates relevant interview questions and sample answers based on the candidate's provided information.

## Testing

The application was tested using different job roles, skills, and experience details. It successfully generated interview questions and sample answers.

## Conclusion

The AI Interview Assistant demonstrates prompt design, AI API integration, context handling, and response generation using Python, Streamlit, and Google Gemini.