import numpy as np
from flask import Flask, abort, jsonify, request
import pickle 
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()
f = open('outfile', 'rb')
word_features = pickle.load(f)
f.close()
app = Flask(__name__)


def find_features(document):
    words = {}
    for w in nltk.word_tokenize(document):
        stemmed_word = stemmer.stem(w.lower())
        words[stemmed_word] = 1
    
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/predict', methods=['GET'])
def predict():
     predict_sentence = text = request.args.get('text')
     dist = classifier.prob_classify(find_features(predict_sentence))
     return jsonify({'click-bait': dist.prob(1), 'non-click-bait':dist.prob(0)})

if __name__ == '__main__':
     app.run(port = 8080, debug = True)