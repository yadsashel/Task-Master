# Task Master

Task Master is a web application for managing daily tasks. Users can add, edit, delete, and mark tasks as complete, making it easier to stay organized and productive.

## Features

- **Add Tasks:** Create tasks with titles, descriptions, and due dates.
- **Edit Tasks:** Modify task details if anything changes.
- **Delete Tasks:** Remove tasks that are no longer relevant.
- **Mark Complete:** Track completed tasks easily.
- **Daily Planner View:** Organizes tasks by day for efficient planning.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python), RESTful API
- **Database:** MongoDB (hosted on MongoDB Atlas)
- **Cache:** Redis (optional for quick access)
  
## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yadsashel/Task-Master.git
   cd Task-Master
   ```

2. **Install dependencies:**
   - Make sure you have Python and pip installed.
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure Database:**
   - Set up your MongoDB connection string in `config.py`:
     ```python
     # config.py
     from pymongo import MongoClient

     def get_db_connection():
         client = MongoClient("YOUR_MONGO_URI")
         db = client['taskmaster_db']
         return db
     ```

4. **Run the app:**
   ```bash
   flask run
   ```

5. **Access the application:**
   - Visit [http://localhost:5000](http://localhost:5000) in your browser.

## API Endpoints

| Method | Endpoint        | Description                  |
| ------ | --------------- | ---------------------------- |
| GET    | `/tasks`        | Retrieve all tasks           |
| POST   | `/tasks`        | Create a new task            |
| PUT    | `/tasks/<id>`   | Update a specific task       |
| DELETE | `/tasks/<id>`   | Delete a specific task       |

## Deploying on Render

1. Commit your code to GitHub.
2. Go to [Render](https://render.com/), sign in, and select "New Web Service."
3. Connect to your GitHub repository.
4. Follow the prompts to deploy your app.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Author

Created by Yadsashel.
```