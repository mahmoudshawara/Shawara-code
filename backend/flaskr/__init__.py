import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import json

from sqlalchemy.sql.expression import delete

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE  
  questions = [question.format() for question in selection]
  current_questions = questions[start:end]

  return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
    
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs (done)
  '''
  #CORS(app)
  CORS(app, resources={'/': {'origins': '*'}})
  
  
  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow (done)
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE')
      return response
  '''
  @TODO: (done)
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def retrieve_categories():
    all_categories = Category.query.order_by(Category.id).all()
    current_categories = [category.format() for category in all_categories]
    categories={}

    for category in all_categories:
      categories[category.id]=category.type
    if len(current_categories) == 0 :
      abort(404)
    return jsonify({
      'categories': categories,
    }) 


  '''
  @TODO: (done)
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 
  

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def retrieve_questions():
    selection= Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)
    
    if len(current_questions) == 0 :
      abort(404)
    all_categories = Category.query.order_by(Category.id).all()
    categories={}

    categories = [(str(category.id), category.type) for category in all_categories]

    #currentCategory=str(categories[len(categories-1)].type)
    return jsonify({
    'questions':current_questions,
    'totalQuestions': len(Question.query.all()),
    'categories':categories,
    #'currentCategory': currentCategory,   
    })   


  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None :
        abort(404)
      else:
        question.delete()
        return jsonify({
        'success': True,
        'deleted': question_id,
        })  
    except:
      abort(422)            

  '''
  @TODO: (done)
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def add_search_question():
    body = request.get_json()
    if (body.get('searchTerm') is None):
      new_answer =body.get('answer', None)
      new_category =body.get('category', None)
      new_difficulty=body.get('difficulty', None)
      new_question = body.get('question', None)
   
      try:      
        new_question= Question(answer=new_answer,category=new_category,difficulty=new_difficulty,question=new_question)
        new_question.insert()
        current_category= Category.query.filter_by(id = int(new_category)).one_or_none()
        selection= Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)
      
        if len(current_questions) == 0 :
          abort(404)
        
        return jsonify({
          'created':new_question.id,
          'questions':current_questions,
          'totalQuestions': len(Question.query.all()),
          'currentCategory': current_category.type,
        })
      except:
        abort(422)
   #add search for question  
    else:
      try:
        search_term =body.get('searchTerm')
        selection=Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()
        current_questions= paginate_questions(request, selection)
        if len(current_questions) ==0 :
          abort(404)
        return jsonify({
          'questions':current_questions,
          'totalQuestions': len(Question.query.all()),
          #'currentCategory': currentCategory,   
          })   

      
      except:
        abort(404) 

        


  '''
  @TODO: (done) 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: (done)
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def category_questions(category_id):
    try:
      current_category= Category.query.filter_by(id = category_id).one_or_none()
      selection= Question.query.filter_by(category =str(category_id)).order_by(Question.id).all()
      current_questions= paginate_questions(request, selection)
      
      if current_category is None :
        abort (400)
      else:
        return jsonify({
          'questions':current_questions,                  
          'totalQuestions': len(Question.query.all()),          
          'currentCategory': current_category.type,   
        })     
    except:
      abort(400)  

  '''
  @TODO: (done)
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def play_quiz():
    body = request.get_json()
    previous_questions= body.get('previous_questions')
    quiz_category=body.get('quiz_category')
    if quiz_category is None or previous_questions is None :
      abort(400)
    Current_category = Category.query.filter(Category.type==quiz_category).one_or_none()
    if quiz_category == "ALL":
      questions= Question.query.all()
    else:
      questions= Question.query.filter(Question.category==str(Current_category.id)).all()
      #formatted_questions = [question.format() for question in questions]

    non_repeated_questions = []
    for ques in questions:
      if ques.id not in previous_questions:
        non_repeated_questions.append(ques)
    if len (non_repeated_questions) ==0:
      return jsonify({
      'Sucess': True,
    })
    new_question = random.choice(non_repeated_questions)
    return jsonify({
      'question': new_question.format(),
    })  
      
  '''
  @TODO:   (done)
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource not found"
   }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request"
    }), 400

  return app

    