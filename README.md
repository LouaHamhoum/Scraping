# Scraping_Facebook_Page
Create docker image from a python docker image pulled from DockerHub while installing the requirements for the app from requirements.txt file.

Once you run the container, the application is launched, it consists of an API of the facebook scraping. 

The command lines to do this are:

> $ docker build -t python-facebook_scraping . -f Dockerfile.txt

> $ docker-compose -f docker-compose.yaml.txt up -d

When you access the FastAPI UI from http://127.0.0.1:8080/docs, you can test it through filling the required field with a name of the page that you want to scrap.
As a results, a database is updated with the results of the scraping.

Example: Amazon Facebook Page
URL: https://www.facebook.com/Amazon , URL Page Name: Amazon 
![image](https://user-images.githubusercontent.com/85879445/192097751-a06c3889-d58c-42db-b61a-d2bd098b649f.png)
 
You can also test if the scraping function returns scraping data or not through the test script. 
 
You can run 
 
> >pytest

![image](https://user-images.githubusercontent.com/85879445/192097981-ac2ea826-4fc7-4aa6-a99c-182d2f38a2af.png)




