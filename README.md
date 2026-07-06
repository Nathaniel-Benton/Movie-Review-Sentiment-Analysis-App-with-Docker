# Movie Review Sentiment Analysis App with Docker

## Project Description
This project is used to determine the sentiment of a movie review through a Naive Bayes classifier. This is trained on movie reviews from an IMDB dataset. This project contains a Dockerfile, which will allow you to clone and operate this project on your own local host. 

## Prerequisites
In order to run the container, you must have installed:
- Docker
- Make 

## How to Run
To run this on your local machine, the steps you should follow are:
- Clone the repository using "git clone https://github.com/Nathaniel-Benton/Movie-Review-Sentiment-Analysis-App"
- Run the command "make build"
- Run the command "make run"
- Then paste "http://localhost:8501" into the browser window to open the app
- Run the command "make clean" to remove the image