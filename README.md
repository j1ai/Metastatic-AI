# Metastatic-AI

Metastatic-AI is a Computer Vision Detection Web Platform that analyzes an input image of a metastatic tissue and output whether tissue is malignant or not. Built with Django and React.js, and it is hosted on Heroku. Machine Learning Model is developed with TensorFlow using Convolutional Neural Network and achieved 93% test accuracy. 

A video demo can found here: 

The following diagram gives a high-level overview of the machine learning process:
![ml pipeline](../product_research/unnamed2.jpg)


## Technologies employed

![ml pipeline](./tech.jpg)

We are using GCP as bridge between frontend/backend and ML model. Github is used for CI/CD. Finally, Heroku is used to deploy the app as a website.


### Architecture
 
 ![Dashboard](./architecture.jpg)
 
 Our Machine Learning Model is exported as a Class Object in our backend. Our React JS Frontend will fetch ML Prediction Score from our Django prediction object dynamically.
 

### Setup script

Run the following development setup script:
    ../src/bootstrap.ps1
https://github.com/dcsil/Narwhals/blob/master/src/boostrap.ps1
    
### Web app

 Visit our web app here: https://narwhals-ai.herokuapp.com/
 
 Use Sample Images from this link to test our ML Image Anaysis Features:
 https://github.com/dcsil/Narwhals/tree/master/app/images

### Production

#### Logging Setup

 ![LogDNA](./LogDNA.jpg)

#### Exception Tracking Setup

 ![Sentry](./Sentry.jpg)

#### Github CI Actions
 ![GithubCI](./GithubCI.jpg)

#### Database
 ![Database](./Database.jpg)
 
 #### Service Yaml 
 
 https://github.com/dcsil/Narwhals/blob/master/app/service.yml
 
 ## Build Plan

We have developed a complete Gantt chart which lays out the detailed schedule we will be following towards our second MVP on May 31 2020:

![gantt](./build.jpg)

We hope to follow our timeline as close as possible and achieve the milestones mentioned.

