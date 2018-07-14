# Click-Bait Detection API

## About
This API takes in a headline and gives out probability whether it is a click-bait.

## Demo
https://click-bait.herokuapp.com/predict?text={Your_Headline}

## Model
This API uses a Naive-Bayes Classifier. 
The Model Accuracy is 91%. 
For more Information : https://github.com/SerChirag/click_bait_detector

## Working
The API is hosted on Heroku through Flask.

## Requirement

 1. numpy==1.14.5
 2. nltk==3.3
 3. Flask==1.0.2
 4. gunicorn==19.9.0

