from flask import Flask, request, jsonify
import tensorflow as tf
import re
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load pre-trained model
model = tf.keras.models.load_model("model/resume_analyzer_model.h5")

# Preprocess text
def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip().lower()
    return text

# Vectorizer simulation
vectorizer = CountVectorizer(max_features=1000)
vectorizer.fit(["example data to initialize"])

# Analyze resume
def analyze_resume(resume_text):
    processed_text = preprocess_text(resume_text)
    text_vector = vectorizer.transform([processed_text]).toarray()
    prediction = model.predict(text_vector)
    return prediction[0][0]

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    resume_text = file.read().decode('utf-8')

    # Analyze the resume
    score = analyze_resume(resume_text)
    feedback = "Strong Resume" if score > 0.7 else "Needs Improvement"
    return jsonify({"score": float(score), "feedback": feedback})

if __name__ == '__main__':
    app.run(debug=True)
