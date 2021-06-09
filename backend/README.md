# Backend - Full Stack Trivia API 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


## Review Comment to the Students (done)
```
## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "resource not found"
}
```
The API will return three error types when requests fail:
- 404: Resource Not Found
- 400: Bad Request
- 422: Not Processable 

### Endpoints 
GET '/categories'
- Returns a list of all categories.
- Request Arguments: None
Sample: curl http://127.0.0.1:5000/categories
{"categories":{"1":"Science","2":"Art","3":"Geography","4":"History","5":"Entertainment","6":"Sports"}}
```
GET '/questions'
- Returns a list questions as 10 paginated questions it also return a list of all categories and total number
of questions .
- Request Arguments: None
- Sample: curl http://127.0.0.1:5000/questions
{"categories":[["1","Science"],["2","Art"],["3","Geography"],["4","History"],["5","Entertainment"],["6","Sports"]],"questions":[{"answer":"Apollo 13","category":5,"difficulty":4,"id":2,"question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"},{"answer":"Tom Cruise","category":5,"difficulty":4,"id":4,"question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"},{"answer":"Maya Angelou","category":4,"difficulty":2,"id":5,"question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"},{"answer":"Edward Scissorhands","category":5,"difficulty":3,"id":6,"question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"},{"answer":"Muhammad Ali","category":4,"difficulty":1,"id":9,"question":"What boxer's original name is Cassius Clay?"},{"answer":"Brazil","category":6,"difficulty":3,"id":10,"question":"Which is the only team to play in every soccer World Cup tournament?"},{"answer":"Uruguay","category":6,"difficulty":4,"id":11,"question":"Which country won the first ever soccer World Cup in 1930?"},{"answer":"George Washington Carver","category":4,"difficulty":2,"id":12,"question":"Who invented Peanut Butter?"},{"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,"question":"What is the largest lake in Africa?"},{"answer":"The Palace of Versailles","category":3,"difficulty":3,"id":14,"question":"In which royal palace would you find the Hall of Mirrors?"}],"totalQuestions":19}
-----
GET '/categories/${id}/questions'
- Returns a list questions as 10 paginated questions in certain category it also return total number
of questions and the current category .
- Request Arguments:category id - integer
- sample:curl http://127.0.0.1:5000/categories/1/questions
{"currentCategory":"Science","questions":[{"answer":"The Liver","category":1,"difficulty":4,"id":20,"question":"What is the heaviest organ in the human body?"},{"answer":"Alexander Fleming","category":1,"difficulty":3,"id":21,"question":"Who discovered penicillin?"},{"answer":"Blood","category":1,"difficulty":4,"id":22,"question":"Hematology is a branch of medicine involving the study of what?"}],"totalQuestions":19}
------
DELETE '/questions/${id}'
-Deletes a question based on its id number 
-Returns the id number of the deleted question
- Request Arguments:question id - integer
-Sample: curl http://127.0.0.1:5000/questions/22 -X DELETE
{"deleted":22,"success":true}
-----
POST '/questions'
- This end point can be used for adding a new question or search for question
* in Adding new question case 
- Returns the id of the newlly created question,a list questions as 10 paginated questions, total number
of questions and the  category of the new question.
- JSON request parameters:{
    'question':  'Heres a new question string',
    'answer':  'Heres a new answer string',
    'difficulty': 1,
    'category': 3,
}
- Sample:curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d "{ \"question\": \"wts ur name?\", \"answer\": \"Shawara\", \"difficulty\": \"3\", \"category\": \"5\" }"
{"created":24,"currentCategory":"Geography","questions":[{"answer":"Apollo 13","category":5,"difficulty":4,"id":2,"question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"},{"answer":"Tom Cruise","category":5,"difficulty":4,"id":4,"question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"},{"answer":"Maya Angelou","category":4,"difficulty":2,"id":5,"question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"},{"answer":"Edward Scissorhands","category":5,"difficulty":3,"id":6,"question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"},{"answer":"Muhammad Ali","category":4,"difficulty":1,"id":9,"question":"What boxer's original name is Cassius Clay?"},{"answer":"Brazil","category":6,"difficulty":3,"id":10,"question":"Which is the only team to play in every soccer World Cup tournament?"},{"answer":"Uruguay","category":6,"difficulty":4,"id":11,"question":"Which country won the first ever soccer World Cup in 1930?"},{"answer":"George Washington Carver","category":4,"difficulty":2,"id":12,"question":"Who invented Peanut Butter?"},{"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,"question":"What is the largest lake in Africa?"},{"answer":"The Palace of Versailles","category":3,"difficulty":3,"id":14,"question":"In which royal palace would you find the Hall of Mirrors?"}],"totalQuestions":19}
--
 in Searching case 
- Returns a list questions as 10 paginated questions that match the search term, total number
of questions.
- JSON request parameters:{
    'search Term':  'Heres a search term string',
}
sample:Sample:curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d "{ \"searchTerm\": \"wts ur name?\"}
{"questions":[{"answer":"Shawara","category":3,"difficulty":3,"id":24,"question":"wts ur name?"}],"totalQuestions":19}
-----
POST /quizzes
- This end point can be used for playing quiz
- JSON request parameters: list of ids of previos questions and quiz category string
-Returns  random new question from the same category. 
-Sample: curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d "{\"previous_questions\": [15, 16], \"quiz_category\": \"Science\"}"
{"question":{"answer":"The Liver","category":1,"difficulty":4,"id":20,"question":"What is the heaviest organ in the human body?"}}


## Testing (for every test, you can skip dropdb trivia_test for the first test)
To run the tests, cd to backend folder and run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
Authors
Mahmoud M. Shawara completed the API todos in  (__init__.py), test suite (test_flaskr.py), and this README in Udacity ull Stack Web Developer Nanodegree. The remaining project files (all frontend files) was created before by Udacity team>
