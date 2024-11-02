import os
import sys
from flask import Flask, render_template, url_for, request, redirect, jsonify, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS 
from config import get_db_connection

#creating flask app
app = Flask(__name__)

# Set the secret key for session management
app.secret_key = '5#y2L"F4Q8z\n\xec]/'
CORS(app)

#establishing the database connection
db = get_db_connection()
if db is not None:
    task_collection = db['tasks']    # Access the tasks collection
    users_collection = db['users']   # Access the users collection
else:
    print("Database connection failed.")

#route for the index page(Home Page)
@app.route('/')
def index():
    return render_template('index.html') 


# Route for registration page and form handling
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if password and confirm_password match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.')
            return redirect('/register')
        
        # Check if the username already exists
        if users_collection.find_one({"username": username}):
            flash("This username already exists! Please choose a different one.")
            return redirect('/register')

        # Check if the email already exists
        if users_collection.find_one({"email": email}):
            flash("This email already exists! Try logging in.")
            return redirect('/login')

        # Hash password and save user
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256') 
        users_collection.insert_one({
            "username": username,
            "email": email,
            "password": hashed_password  # Save the hashed password
        })

        flash('Registration successful! Please log in.')
        return redirect('/login')

    return render_template('register.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Correct request method check
        username = request.form['username']
        password = request.form['password']

        # Find the user by username
        user = users_collection.find_one({"username": username})

        # Check if the user exists and the password is correct
        if user and check_password_hash(user['password'], password):  # Correctly reference stored password
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            flash('Login Successful!')
            return redirect('/tasks')
        
        else:
            flash('Invalid username or password! Please try again.')
    
    return render_template('login.html')

#route for tasks page
@app.route('/tasks')
def tasks():
    if 'user_id' not in session:
        return redirect('/login')  # Redirect to login if not authenticated

    # Fetch tasks from the database if needed
    tasks = task_collection.find()  # Example: Fetch all tasks
    return render_template('tasks.html', tasks=tasks)  # Pass tasks to the template


#add a task and store it in the mongodb
@app.route('/api/tasks', methods=['POST'])
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
@app.route('/api/tasks', methods=['GET'])
def get_task():
    tasks = list(task_collection.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return jsonify(tasks), 200

#edit a task
@app.route('/tasks<task_id>', methods=['PUT'])
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