# Youtube_Watch_History
 
 ##1. Feature
"Youtube_Watch_History" is an application that manages the delivery history of Youtube.  
This app is created by [Nuxt.js](https://github.com/nuxt/nuxt.js) and [Django](https://github.com/django/django), [Django-Rest-Framework](https://github.com/encode/django-rest-framework)
 
 ***
## 2. Version
 
* Python 3.6.5
* Node.js 16.4.0

***
## 3. Clone Github repository

 ```
git clone https://github.com/scientist024/youtube-watch-history.git
 ```
 
 ***
## 4. Backend 

### 4-1. Install
You can use Pipenv to install the required modules.
```
pipenv shell

pipenv install
```

### 4-2. Migrate
```
pipenv run python manage.py migrate
```

### 4-3. Start the development server
```
pipenv run python manage.py runserver
```
 ***
 
 ## 5. Frontend
 ### 5-1. Setup
 ```
 npm install
 ```
 
 ### 5-2. Start the development server
 ```
 npm run dev
 ```
 
 ## 6. How to use
 You can check the list of Youtube browsing history by accessing http://localhost:3000/movies  
 You can create, modify and delete the history.  
 You also do those actions by accessing http://localhost:3000/streamers or upper Navigation bar.  
 
 ## 7. To Be Developed
 Filter function  
 Function to search for movie by streamrs tag  
 Pagination 
 
### Note
I don't test environments under Linux and Mac.
