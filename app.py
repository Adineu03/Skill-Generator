import streamlit as st
import openai

st.title("Job Skills Generator")

st.markdown(
    "Enter your **OpenAI API Key**, **Job Title**, and **Job Description** to generate a detailed list of relevant skills."
)

# Ask user to input the OpenAI API Key directly on the UI
api_key = st.text_input("Enter your OpenAI API Key", type="password")

job_title = st.text_input("Job Title")
job_description = st.text_area("Job Description", height=300)

def generate_skills(api_key, job_title, job_description):
    # Set the API key from user input
    openai.api_key = api_key

    # Construct a refined prompt with clear instructions
    prompt = f"""
Job Title: {job_title}

Job Description:
{job_description}

Based on the job title and job description provided above, generate a comprehensive and detailed list of skills required for the position. Your response must be organized into clearly defined categories similar to the following example for a Housekeeping role. Please follow these guidelines:

1. **Organize Skills into Categories:**  
   - **Core/Technical Skills:** Include essential skills directly related to the primary job functions and technical requirements.  
   - **Organizational & Time Management Skills:** List skills related to task management, prioritization, scheduling, and overall work efficiency.  
   - **Interpersonal & Communication Skills:** Highlight skills that involve effective communication, teamwork, and customer service.  
   - **Additional/Optional Skills:** Include any extra skills that could be beneficial depending on the specific context or work environment.

2. **Formatting Requirements:**  
   - Use clear, bold headings for each category.  
   - Under each category, present the skills as a bullet list for easy readability.

3. **Content Expectations:**  
   - Ensure the output is detailed, professional, and mirrors the clarity and extensiveness of the provided example.

Provide your answer in a structured, detailed, and professional manner.
    """

    try:
        # Call the OpenAI API using ChatCompletion (using GPT-3.5-turbo as an example)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert job skills generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        generated_skills = response.choices[0].message.content.strip()
        return generated_skills
    except Exception as e:
        return f"Error generating skills: {e}"

if st.button("Generate Skills"):
    if not api_key:
        st.error("Please provide your OpenAI API Key.")
    elif job_title and job_description:
        with st.spinner("Generating skills..."):
            skills_output = generate_skills(api_key, job_title, job_description)
        st.markdown("### Generated Skills:")
        st.markdown(skills_output)
    else:
        st.error("Please provide both a job title and a job description.")
