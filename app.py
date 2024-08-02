from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return "Sentiment Analysis Model is up and running!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the tweet text from the request
    data = request.get_json(force=True)
    tweet = data['tweet']
    
    # Transform the tweet text using the vectorizer
    transformed_tweet = vectorizer.transform([tweet])
    
    # Predict the sentiment
    prediction = model.predict(transformed_tweet)
    
    # Return the result
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
