import nltk
from nltk.stem import WordNetLemmatizer
import json
import numpy as np

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load and preprocess data (intents, keywords, etc.)
with open('intents.json', 'r') as file:
    intents = json.load(file)

def preprocess_text(text):
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(w.lower()) for w in words]
    return words
