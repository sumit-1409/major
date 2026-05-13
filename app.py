# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import numpy as np
import os

app = Flask(__name__)

# Print current working directory and template folder for debugging
print("Current working directory:", os.getcwd())
print("Template folder:", app.template_folder)

# Load datasets
def load_datasets():
    training_df = pd.read_csv('training_data.csv')
    training_df['skills_clean'] = training_df['skills'].str.lower().str.replace(',', ' ')
    
    job_df = pd.read_csv('job_required_skills.csv')
    job_required_skills = {}
    for _, row in job_df.iterrows():
        job = row['job_role']
        skills = {s.strip() for s in str(row['required_skills']).split(',') if s.strip()}
        job_required_skills[job] = skills
    
    courses_df = pd.read_csv('courses.csv')
    courses_db = []
    for _, row in courses_df.iterrows():
        skills = [s.strip() for s in str(row['skills']).split(',') if s.strip()]
        courses_db.append({
            "name": row['name'],
            "provider": row['provider'],
            "skills": skills
        })
    
    return training_df, job_required_skills, courses_db

training_df, job_required_skills, courses_db = load_datasets()

# Train model
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 3)),
    LogisticRegression(max_iter=1000, random_state=42)
)
model.fit(training_df['skills_clean'], training_df['job_role'])

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Template Error: {str(e)}<br><br>Make sure index.html is inside the 'templates' folder.", 500

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_input = data.get('skills', '').strip().lower()
    
    if not user_input:
        return jsonify({"error": "Please enter your skills"}), 400
    
    user_clean = user_input.replace(',', ' ')
    
    predicted_job = model.predict([user_clean])[0]
    proba = model.predict_proba([user_clean])[0]
    confidence = round(float(np.max(proba) * 100), 2)
    
    user_skills_set = {s.strip() for s in user_input.split(',') if s.strip()}
    required_skills = job_required_skills.get(predicted_job, set())
    
    matching_skills = sorted(list(user_skills_set.intersection(required_skills)))
    missing_skills = sorted(list(required_skills.difference(user_skills_set)))
    match_percentage = round((len(matching_skills) / len(required_skills) * 100), 2) if required_skills else 100.0
    
    if match_percentage >= 80:
        feedback = "🎉 Excellent alignment! You are already well-prepared for this role."
    elif match_percentage >= 50:
        feedback = "👍 Good match. Upskill on the missing areas below."
    else:
        feedback = "🔥 Opportunity to grow. Focus on the recommended courses."
    
    recommendations = []
    for course in courses_db:
        course_skills_set = {s.lower().strip() for s in course["skills"]}
        overlap = len(course_skills_set.intersection(missing_skills))
        if overlap > 0 or not missing_skills:
            score = overlap / len(missing_skills) if missing_skills else 1.0
            recommendations.append({
                "name": course["name"],
                "provider": course["provider"],
                "overlap": overlap,
                "score": score
            })
    
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    top_courses = recommendations[:4]
    
    result = {
        "predicted_job": predicted_job,
        "confidence": confidence,
        "match_percentage": match_percentage,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "feedback": feedback,
        "recommended_courses": [{"name": c["name"], "provider": c["provider"], "overlap": c["overlap"]} for c in top_courses]
    }
    
    return jsonify(result)

if __name__ == '__main__':
    print("🚀 Starting SkillBridge AI...")
    print("Current directory:", os.getcwd())
    print("Make sure 'templates/index.html' exists!")
    app.run(debug=True, port=5000)