# SkillBridge - AI Career Recommendation Platform

![Project Banner](https://via.placeholder.com/800x300/00d4ff/ffffff?text=SkillBridge+-+AI+Career+Advisor)

**An AI-Powered Personalized Learning & Career Recommendation System** built to bridge the gap between student skills and industry requirements.

---

## 🚀 Project Overview

SkillBridge is an intelligent web platform that helps students and fresh graduates discover suitable job roles, analyze their skill gaps, and get personalized course recommendations to improve their employability.

By entering their skills, users instantly receive:
- Best matching job role with confidence score
- Detailed skill gap analysis
- Personalized course suggestions to bridge missing skills

---

## ✨ Key Features

- **Job Role Prediction** using Machine Learning (Logistic Regression + TF-IDF)
- **Skill Gap Analysis** with Match Percentage
- **Personalized Course Recommendations** ranked by relevance
- **Interactive Dashboard** with clean UI
- **Real-time Processing**
- **CSV-based Scalable Datasets** (Easy to expand)
- **SDG 8 Aligned** (Decent Work and Economic Growth)

---

## 🛠️ Tech Stack

| Layer          | Technologies                          |
|----------------|---------------------------------------|
| **Frontend**   | HTML, CSS, JavaScript, Tailwind CSS   |
| **Backend**    | Python, Flask                         |
| **ML Model**   | Scikit-learn (Logistic Regression + TF-IDF) |
| **Data**       | Pandas, CSV Datasets                  |
| **Visualization** | Interactive Dashboard              |

---

## 📁 Project Structure
skillbridge/
├── app.py                      # Flask Backend
├── training_data.csv
├── job_required_skills.csv
├── courses.csv
├── templates/
│   └── index.html              # Frontend
├── uploads/                    # (Optional for future resume upload)
└── README.md
text---

## 🏃‍♂️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/skillbridge.git
cd skillbridge
2. Install Dependencies
Bashpip install flask scikit-learn pandas numpy
3. Run the Application
Bashpython app.py
4. Open in Browser
Go to: http://127.0.0.1:5000

📊 Datasets Used

training_data.csv → Skill to Job Role mappings (for model training)
job_required_skills.csv → Required skills for each job (for gap analysis)
courses.csv → Course database with associated skills


🎯 Sample Inputs

Data Scientist: python, machine learning, pandas, sql, data analysis
Full Stack Developer: javascript, react, node.js, typescript, mongodb
AI Engineer: python, pytorch, llms, generative ai, prompt engineering


🔮 Future Scope

Resume upload & parsing (PDF)
Integration with real job APIs (LinkedIn, Naukri)
User authentication & profile tracking
Deep Learning models for better accuracy
Mobile App (React Native / Flutter)
Learning path visualization


🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repository
Create a new branch
Make improvements
Submit a Pull Request


📄 License
This project is open-source and available under the MIT License.

🙏 Acknowledgements

Supervisor: Dr. Sonia Arora, Assistant Professor, NIET Greater Noida
Institute: Noida Institute of Engineering and Technology (NIET)
University: Dr. A.P.J. Abdul Kalam Technical University, Lucknow


Made with ❤️ for better career guidance
Star this repository if you found it helpful!
