from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

with open('SVM_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('SVM_vectorizer.pkl', 'rb') as model_1_file:
    vectorizer = pickle.load(model_1_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form.get('email_text')
    if email_text:
        email_tfidf = vectorizer.transform([email_text])
        
        prediction = model.predict(email_tfidf)
        
        result = 'Spam' if prediction[0] == 1 else 'Not Spam'
        return jsonify({'prediction': result})
    return jsonify({'error': 'No input provided'})

if __name__ == '__main__':
    app.run(debug=True)
