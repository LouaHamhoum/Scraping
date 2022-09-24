# Scraping
A Docker image to deploy a Python-FastApi app from a Git repository.

The container will handle the git clone and requirements installing before the app starts for the first time.
## Features
Clone from GIT repository

Install requirements from requirements.txt file

## Build application
Build the Docker image manually by cloning the Git repo.

$ git clone https://github.com/LouaHamhoum/Scraping.git

$ docker build -t LouaHamhoum/Scraping

## Download precreated image
You can also just download the existing image from DockerHub.

$ docker pull LouaHamhoum/Scraping

## Files
The Dockerfile sets up the pipenv environment, and installs the dependencies

The docker-compose.yml defines the 'app' Docker service and how it should be built

The app folder contains the script file and local_db contains the database created 
