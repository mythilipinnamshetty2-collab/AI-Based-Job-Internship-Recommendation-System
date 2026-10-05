import os
import requests
import pandas as pd
import streamlit as st

from dotenv import load_dotenv


# =====================================================
# LOAD API KEY
# =====================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Job & Internship Recommendation System",
    page_icon="💼",
    layout="wide"
)


# =====================================================
# TITLE
# =====================================================

st.title("💼 AI-Based Job & Internship Recommendation System")

st.write(
    "Get personalized job and internship recommendations "
    "using your skills, education and interests."
)


# =====================================================
# CHECK API KEY
# =====================================================

if not GEMINI_API_KEY:

    st.error("❌ Gemini API key not found.")

    st.info(
        "Add GEMINI_API_KEY to your .env file."
    )

    st.stop()


# =====================================================
# JOB DATASET
# =====================================================

jobs = pd.DataFrame({

    "Job Title": [
        "Python Developer Intern",
        "Data Analyst Intern",
        "Machine Learning Intern",
        "Web Developer Intern",
        "Frontend Developer Intern",
        "Java Developer Intern",
        "AI Developer Intern",
        "Database Developer Intern",
        "Software Developer Intern",
        "Data Science Intern"
    ],

    "Company": [
        "TechSoft",
        "DataCorp",
        "AI Labs",
        "WebWorks",
        "DesignTech",
        "Java Solutions",
        "Future AI",
        "DB Systems",
        "CodeWorks",
        "Data Science Hub"
    ],

    "Skills": [
        "Python SQL Django Flask Git",
        "Python SQL Excel Pandas Power BI",
        "Python Machine Learning NumPy Pandas Scikit-learn",
        "HTML CSS JavaScript React Git",
        "HTML CSS JavaScript React Bootstrap",
        "Java SQL Spring OOP Git",
        "Python Machine Learning Deep Learning TensorFlow",
        "SQL MySQL Database Python",
        "Python Java C++ SQL Git",
        "Python Pandas NumPy Machine Learning SQL"
    ],

    "Location": [
        "Hyderabad",
        "Hyderabad",
        "Bangalore",
        "Hyderabad",
        "Bangalore",
        "Chennai",
        "Bangalore",
        "Hyderabad",
        "Chennai",
        "Hyderabad"
    ],

    "Type": [
        "Internship",
        "Internship",
        "Internship",
        "Internship",
        "Internship",
        "Internship",
        "Internship",
        "Internship",
        "Internship",
        "Internship"
    ],

    "Eligibility": [
        "B.Tech / B.E / MCA",
        "B.Tech / B.E / B.Sc",
        "B.Tech / B.E / MCA",
        "B.Tech / B.E / BCA",
        "B.Tech / B.E / BCA",
        "B.Tech / B.E / MCA",
        "B.Tech / B.E / MCA",
        "B.Tech / B.E / BCA",
        "B.Tech / B.E / MCA",
        "B.Tech / B.E / B.Sc / MCA"
    ]
})


# =====================================================
# GEMINI FUNCTION
# =====================================================

def ask_gemini(prompt):

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"
    headers = {
        "Content-Type": "application/json"
    }

    params = {
        "key": GEMINI_API_KEY
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            params=params,
            json=data,
            timeout=60
        )

        if response.status_code != 200:

            return (
                "Gemini API Error:\n\n"
                + response.text
            )

        result = response.json()

        return (
            result["candidates"][0]
            ["content"]["parts"][0]["text"]
        )

    except requests.exceptions.Timeout:

        return (
            "Gemini request timed out. "
            "Please check your internet connection."
        )

    except requests.exceptions.ConnectionError:

        return (
            "Unable to connect to Gemini. "
            "Please check your internet connection."
        )

    except Exception as e:

        return f"Unexpected error: {e}"


# =====================================================
# USER PROFILE
# =====================================================

st.header("👤 Enter Your Profile")

col1, col2 = st.columns(2)


with col1:

    name = st.text_input(
        "Name",
        placeholder="Enter your name"
    )

    education = st.selectbox(
        "Education",
        [
            "B.Tech",
            "B.E",
            "BCA",
            "B.Sc",
            "MCA",
            "M.Tech"
        ]
    )

    skills = st.text_area(
        "Skills",
        placeholder="Example: Python, SQL, Pandas"
    )


with col2:

    interest = st.text_input(
        "Career Interest",
        placeholder="Example: Data Science"
    )

    location = st.selectbox(
        "Preferred Location",
        [
            "Any",
            "Hyderabad",
            "Bangalore",
            "Chennai"
        ]
    )

    experience = st.selectbox(
        "Experience",
        [
            "Fresher",
            "Less than 1 year",
            "1-2 years"
        ]
    )


# =====================================================
# RECOMMEND BUTTON
# =====================================================

if st.button(
    "🔍 Find Recommended Jobs",
    use_container_width=True
):

    if not name.strip():

        st.warning("Please enter your name.")
        st.stop()

    if not skills.strip():

        st.warning("Please enter your skills.")
        st.stop()

    if not interest.strip():

        st.warning("Please enter your career interest.")
        st.stop()


    # =================================================
    # FILTER JOBS BY LOCATION
    # =================================================

    if location == "Any":

        results = jobs.copy()

    else:

        results = jobs[
            jobs["Location"] == location
        ].copy()


    # =================================================
    # GEMINI RECOMMENDATION
    # =================================================

    job_data = ""

    for _, job in results.iterrows():

        job_data += f"""

Job Title: {job['Job Title']}
Company: {job['Company']}
Required Skills: {job['Skills']}
Location: {job['Location']}
Type: {job['Type']}
Eligibility: {job['Eligibility']}

"""


    prompt = f"""

You are an AI-based job and internship recommendation assistant.

Student Profile:

Name: {name}

Education: {education}

Skills: {skills}

Career Interest: {interest}

Experience: {experience}

Preferred Location: {location}


Available Jobs and Internships:

{job_data}


Analyze the student's profile and recommend the
TOP 5 most suitable opportunities.

For each recommendation provide:

1. Job/Internship name
2. Company
3. Match percentage
4. Why it matches
5. Required skills
6. Missing skills

Then provide:

## Career Advice

Give simple advice for this student to improve
their chances of getting an internship or job.

Keep the response suitable for a college student.
"""


    with st.spinner(
        "🤖 Gemini is analyzing your profile..."
    ):

        result = ask_gemini(prompt)


    # =================================================
    # DISPLAY RESULT
    # =================================================

    st.header("🎯 AI Recommendations")

    st.markdown(result)


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "AI-Based Job & Internship Recommendation System "
    "| Streamlit + Gemini API"
)