# Full Stack API Final Project


## Full Stack Trivia

Trivia API project is a game that can help you to increase your knowledge by answering different questions in deferent gategories. The Task in this project is to complete the backend and test file to be sure that the API can do the following functions  :

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.


## Getting Started


### Backend
>View the [README within ./frontend for more details.](./frontend/README.md)


### Frontend

>View the [README within ./frontend for more details.](./frontend/README.md)



## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{"error":404,"message":"resource not found","success":false}
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

### Authors
Mahmoud M. Shawara completed the API todos in  (__init__.py), test suite (test_flaskr.py), and this README in Udacity ull Stack Web Developer Nanodegree. The remaining project files (all frontend files) was created before by Udacity team>
