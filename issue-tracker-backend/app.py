from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
from datetime import datetime, timezone

# 1. App Initialization
app = Flask(__name__)
# Enable CORS to allow the frontend to communicate with this backend
CORS(app) 

# 2. In-Memory "Database" with Sample Data
# We'll use a simple list of dictionaries to store issues.
issues = [
    {
        "id": "a1b2c3d4",
        "title": "Implement user authentication",
        "description": "Users should be able to sign up and log in.",
        "status": "In Progress",
        "priority": "High",
        "assignee": "Alice",
        "createdAt": "2025-09-22T18:30:00Z",
        "updatedAt": "2025-09-22T19:00:00Z"
    },
    {
        "id": "e5f6g7h8",
        "title": "Fix button styling on the main page",
        "description": "The primary button has incorrect padding.",
        "status": "Open",
        "priority": "Low",
        "assignee": "Bob",
        "createdAt": "2025-09-21T10:00:00Z",
        "updatedAt": "2025-09-21T10:00:00Z"
    }
]

# 3. API Endpoints

# GET /health -> Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

# POST /issues -> Create a new issue
@app.route('/issues', methods=['POST'])
def create_issue():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400

    now = datetime.now(timezone.utc).isoformat()

    new_issue = {
        "id": str(uuid.uuid4()),
        "title": data.get('title'),
        "description": data.get('description', ''),
        "status": data.get('status', 'Open'),
        "priority": data.get('priority', 'Medium'),
        "assignee": data.get('assignee', None),
        "createdAt": now,
        "updatedAt": now
    }
    issues.append(new_issue)
    return jsonify(new_issue), 201

# GET /issues/:id -> Get a single issue by its ID
@app.route('/issues/<string:issue_id>', methods=['GET'])
def get_issue(issue_id):
    issue = next((issue for issue in issues if issue['id'] == issue_id), None)
    if issue:
        return jsonify(issue)
    return jsonify({"error": "Issue not found"}), 404

# PUT /issues/:id -> Update an existing issue
@app.route('/issues/<string:issue_id>', methods=['PUT'])
def update_issue(issue_id):
    issue = next((issue for issue in issues if issue['id'] == issue_id), None)
    if not issue:
        return jsonify({"error": "Issue not found"}), 404

    data = request.get_json()
    issue.update({
        "title": data.get('title', issue['title']),
        "description": data.get('description', issue['description']),
        "status": data.get('status', issue['status']),
        "priority": data.get('priority', issue['priority']),
        "assignee": data.get('assignee', issue['assignee']),
        "updatedAt": datetime.now(timezone.utc).isoformat()
    })
    return jsonify(issue)

# GET /issues -> Get all issues with filtering, sorting, and pagination
@app.route('/issues', methods=['GET'])
def get_issues():
    args = request.args
    temp_issues = list(issues)

    # Search by title
    if 'search' in args:
        search_term = args.get('search').lower()
        temp_issues = [iss for iss in temp_issues if search_term in iss['title'].lower()]

    # Filtering
    for key in ['status', 'priority', 'assignee']:
        if key in args:
            temp_issues = [iss for iss in temp_issues if iss.get(key) == args.get(key)]

    # Sorting
    if 'sortBy' in args:
        sort_key = args.get('sortBy')
        sort_order = args.get('sortOrder', 'asc')
        reverse = (sort_order == 'desc')
        if temp_issues and sort_key in temp_issues[0]:
            temp_issues.sort(key=lambda x: x[sort_key], reverse=reverse)
    
    # Pagination
    page = int(args.get('page', 1))
    page_size = int(args.get('pageSize', 10))
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_issues = temp_issues[start_index:end_index]

    return jsonify({
        "issues": paginated_issues,
        "total": len(temp_issues),
        "page": page,
        "pageSize": page_size
    })

# 4. Run the App
if __name__ == '__main__':
    app.run(debug=True, port=5000)