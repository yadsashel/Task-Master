import os
import sys
from flask import Flask, render_template, url_for, request, redirect, jsonify
from bson import ObjectId
from flask_cors import CORS 
from backend.config import get_db_connection


#creating flask app
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

#establishing the database connection
db = get_db_connection()
task_collection = db['tasks'] #access the tasks collection


#route for the index page(Home Page)
@app.route('/')
def index():
    return render_template('index.html') 


#route for register page
@app.route('/register')
def register():
    return render_template('register.html')

#route for login page
@app.route('/login')
def login():
    return render_template('login.html')

#route for tasks page
@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

#add a task and store it in the mongodb
@app.route('/api/tasks', method=['POST'])
def add_task():
    data = request.json
    new_task = {
       "title": data.get("title"),
       "desciption": data.get("description"),
       "due_date": data.get("due_date"),
       "completed": False
    }
    result = task_collection.insert_one(new_task)
    new_task["_id"] = str(result.iserted_id) #convet objectID to string
    return jsonify(new_task), 201

#feth a task and displayed it in the frontend
@app.route('/api/tasks', method=['GET'])
def get_task():
    tasks = list(task_collection.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return jsonify(tasks), 200

#edit a task
@app.route('/tasks<task_id>', method=['PUT'])
def edit_task():
    # Step 1: Get the data from the request
    data = request.json
    
    # Step 2: Update the task in the database
    result = task_collection.update_one(
        {'_id': ObjectId('task_id')}, # Find the task by its ID
        {'$set': data}  # Update with the new data based on the data recieved
    )    

    # Step 3: Return a response
    if result.modified_count > 0:
        return jsonify({'message': 'The Task Is Updated Successfully'}), 200
    else:
        return jsonify({'message': 'No Changes Made Or Task Not Found'}), 404
    
if __name__ == '__main__':
    app.run(debug=True)