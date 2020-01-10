# Metastatic-AI

![meta](.app//src/assets/logo.png)

Metastatic-AI is a Computer Vision Detection Web Platform that analyzes an input image of a metastatic tissue and output whether tissue is malignant or not. Built with Django and React.js, and it is hosted on Heroku. Machine Learning Model is developed with TensorFlow using Convolutional Neural Network and achieved 93% test accuracy. 

A video demo can found here: 

The following diagram gives a high-level overview of the machine learning process:
![ml pipeline](./product_research/unnamed2.jpg)


## Technologies employed

![ml pipeline](./app/tech.jpg)

We are using GCP as bridge between frontend/backend and ML model. Github is used for CI/CD. Finally, Heroku is used to deploy the app as a website.


### Architecture
 
 ![Dashboard](./app/architecture.jpg)
 
 Our Machine Learning Model is exported as a Class Object in our backend. Our React JS Frontend will fetch ML Prediction Score from our Django prediction object dynamically.
     
### Web app

 Visit our web app here: https://narwhals-ai.herokuapp.com/
 
 Use Sample Images from this link to test our ML Image Anaysis Features:
 https://github.com/dcsil/Narwhals/tree/master/app/images

### Production

#### Logging Setup

 ![LogDNA](./app/LogDNA.jpg)

#### Exception Tracking Setup

 ![Sentry](./app/Sentry.jpg)

#### Github CI Actions
 ![GithubCI](./app/GithubCI.jpg)

#### Database
 ![Database](./app/Database.jpg)
 
 ## Build Plan

We have developed a complete Gantt chart which lays out the detailed schedule we will be following towards our second MVP on May 31 2020:

![gantt](./app/build.jpg)

We hope to follow our timeline as close as possible and achieve the milestones mentioned.

