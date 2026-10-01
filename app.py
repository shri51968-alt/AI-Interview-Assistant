import streamlit as st
from google import genai

st.set_page_config(page_title="AI Interview Assistant")

st.title("🤖 AI Interview Assistant")
st.write("Practice interview questions using Generative AI.")

api_key = st.text_input(
    "Enter your Gemini API Key",
    type="password"
)

job_role = st.text_input(
    "Enter the job role",
    placeholder="Example: Python Developer"
)

skills = st.text_area(
    "Enter your skills",
    placeholder="Example: Python, SQL, HTML, CSS"
)

experience = st.text_area(
    "Enter your experience or project details",
    placeholder="Example: Developed a Python FAQ chatbot project."
)

difficulty = st.selectbox(
    "Select interview difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

number = st.slider(
    "Number of questions",
    3,
    10,
    5
)

if st.button("Generate Interview Questions"):

    if not api_key:
        st.warning("Please enter your Gemini API key.")

    elif not job_role.strip():
        st.warning("Please enter a job role.")

    elif not skills.strip():
        st.warning("Please enter your skills.")

    else:
        try:
            client = genai.Client(api_key=api_key)

            prompt = f"""
You are an AI Interview Assistant.

Candidate information:
Job Role: {job_role}
Skills: {skills}
Experience/Projects: {experience}
Difficulty Level: {difficulty}

Generate {number} interview questions suitable for this candidate.

For each question provide:
1. Interview Question
2. What the interviewer expects
3. Sample Answer

Use the candidate's job role, skills, and experience as context.
Keep the answers clear and suitable for an interview.

Do not invent qualifications that the candidate has not provided.
"""

            with st.spinner("Generating interview questions..."):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            st.subheader("🎯 Interview Questions")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
        