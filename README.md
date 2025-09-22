# Simple Issue Tracker

A full-stack issue tracking application built with a Python (Flask) backend and an Angular frontend. This project was developed as a technical assignment and demonstrates a complete CRUD (Create, Read, Update, Delete) workflow with a modern, responsive user interface.


---
## Features

* ✅ **View Issues:** Display a list of all issues in a clean, paginated table.
* ✅ **Search & Filter:** Dynamically search by title and filter by status or priority.
* ✅ **Sortable Data:** Sort the issue list by any column.
* ✅ **Create & Update:** A full-featured form to create new issues and edit existing ones.
* ✅ **View Details:** Click on any issue to see its complete data in JSON format.
* ✅ **RESTful API:** A backend built with Flask providing all necessary API endpoints.

---
## Tech Stack

### Backend
* **Python 3**
* **Flask:** A lightweight WSGI web application framework.
* **Flask-CORS:** For handling Cross-Origin Resource Sharing.

### Frontend
* **Angular** (v17+ recommended)
* **TypeScript**
* **ngx-pagination:** For simple and effective table pagination.

---
## Prerequisites

Before you begin, ensure you have the following installed on your system:
* **Node.js** (which includes npm) (v18 or higher recommended)
* **Python** (v3.8 or higher recommended)
* **Angular CLI:** `npm install -g @angular/cli`

---
## Installation & Usage

To run this project locally, you will need to run the backend and frontend servers in two separate terminals.

### 1. Clone the Repository
bash
git clone <your-repository-url>
cd issue-tracker-app

### 2. Backend Setup
Navigate to the backend directory from the project root:

Bash
cd issue-tracker-backend
Create and activate a Python virtual environment:

Bash
Create the environment
python -m venv venv

Activate the environment
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install the required packages:

Bash
pip install -r requirements.txt
Run the Flask server:

Bash
python app.py
The backend server will now be running at http://127.0.0.1:5000.

### 3. Frontend Setup
Open a new terminal and navigate to the frontend directory from the project root:

Bash
cd issue-tracker-frontend
Install the required npm packages:

Bash
npm install
Run the Angular development server:

Bash
ng serve
The frontend application will now be running and accessible at http://localhost:4200/
