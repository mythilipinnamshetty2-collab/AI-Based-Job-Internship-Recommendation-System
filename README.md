# 💼 AI-Based Job & Internship Recommendation System

## 📌 Project Overview

The **AI-Based Job & Internship Recommendation System** is a web-based application developed using **Python and Streamlit**.

The system helps students and freshers find suitable job and internship opportunities based on their:

* 🎓 Education
* 💻 Skills
* 🎯 Career interests
* 📍 Preferred location
* 👨‍💻 Experience

The application analyzes the student's profile and recommends suitable opportunities from the available job dataset.

---

## 🎯 Objectives

* To provide personalized job and internship recommendations.
* To help students and freshers find suitable opportunities.
* To match student skills with job requirements.
* To reduce the time required for searching for opportunities.
* To provide career guidance based on the student's profile.
* To identify missing skills required for recommended jobs.

---

## ✨ Features

### 👤 Student Profile

Users can enter:

* Name
* Education
* Skills
* Career Interest
* Preferred Location
* Experience

### 🤖 AI-Based Recommendations

The system analyzes the student's profile and recommends the **Top 5 suitable job or internship opportunities**.

### 📊 Match Percentage

Each recommendation includes an estimated match percentage based on the student's profile and job requirements.

### 💡 Career Advice

The system provides simple career advice to help students improve their chances of getting an internship or job.

### 📍 Location Filtering

Users can select:

* Any
* Hyderabad
* Bangalore
* Chennai

The system filters opportunities according to the selected location.

### ⚠️ Error Handling

The application includes handling for temporary service errors and automatically retries failed requests.

---

## 🛠️ Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Programming language      |
| Streamlit     | Web application interface |
| Google Gemini | AI-based recommendations  |
| Pandas        | Job dataset management    |
| Requests      | API communication         |
| python-dotenv | Environment configuration |
| Git & GitHub  | Version control           |

---

## 📂 Project Structure

```text
AI-Job-Internship-Recommendation/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project folder:

```bash
cd AI-Job-Internship-Recommendation
```

### 2. Create a Virtual Environment

```powershell
python -m venv venv
```

Activate the environment:

```powershell
venv\Scripts\activate
```

### 3. Install Required Libraries

```powershell
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the following command:

```powershell
streamlit run app.py
```

The application will open in your web browser.

---

## 🔄 How the System Works

```text
        User
          ↓
   Enter Profile Details
          ↓
   Education + Skills
          ↓
   Career Interest
          ↓
   Preferred Location
          ↓
     Filter Jobs
          ↓
      AI Analysis
          ↓
   Compare Profile with Jobs
          ↓
   Top 5 Recommendations
          ↓
     Career Advice
```

---

## 🧪 Example Input

```text
Name: Mythili

Education: B.Tech

Skills:
Python, SQL, Pandas, Machine Learning

Career Interest:
Data Science

Preferred Location:
Hyderabad

Experience:
Fresher
```

---

## 📋 Example Output

```text
🎯 AI Recommendations

1. Data Science Intern
   Company: Data Science Hub
   Match: 92%

2. Data Analyst Intern
   Company: DataCorp
   Match: 88%

3. Machine Learning Intern
   Company: AI Labs
   Match: 84%

4. Python Developer Intern
   Company: TechSoft
   Match: 78%

5. AI Developer Intern
   Company: Future AI
   Match: 75%
```

The recommendations may vary depending on the user's profile.

---

## 📊 Available Job Categories

The current dataset includes:

* Python Developer Intern
* Data Analyst Intern
* Machine Learning Intern
* Web Developer Intern
* Frontend Developer Intern
* Java Developer Intern
* AI Developer Intern
* Database Developer Intern
* Software Developer Intern
* Data Science Intern

---

## 🔮 Future Enhancements

* 📄 Resume upload and analysis
* 🔍 Real-time job searching
* 🌐 Job portal integration
* 📧 Email notifications
* 🧠 Skill-gap analysis
* 📚 Course recommendations
* 💬 AI career guidance chatbot
* 👤 User login and registration
* 🗄️ Database integration
* 📱 Mobile-friendly interface

---

## 🎓 Project Use

This project is suitable for:

* College mini projects
* AI/ML projects
* Python projects
* Streamlit projects
* Internship portfolios
* Hackathons
* Academic demonstrations

---

## 👩‍💻 Author

**Pinnamshetty Mythili**

AI-Based Job & Internship Recommendation System

---

## 📜 License

This project is developed for **educational and academic purposes**.
