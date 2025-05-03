# Task Management Application

A full-stack task management application built with Django REST Framework and React.

## Features

- User Authentication (Register/Login)
- Task Creation and Management
- Project Organization
- Secure API Endpoints
- Responsive UI with Tailwind CSS

## Tech Stack

### Backend
- Python 3.x
- Django
- Django REST Framework
- MySQL Database
- JWT Authentication

### Frontend
- React
- Tailwind CSS
- React Router
- Axios for API calls

## Setup Details

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/HimanshuR321/Task-Management-System
   cd task-management/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory with the following variables:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_NAME=task_management
   DATABASE_USER=root
   DATABASE_PASSWORD=your-password
   DATABASE_HOST=localhost
   DATABASE_PORT=3306
   JWT_ACCESS_TOKEN_LIFETIME=60
   JWT_REFRESH_TOKEN_LIFETIME=1
   CORS_ALLOWED_ORIGINS=http://localhost:3000
   ```

5. Create the MySQL database:
   ```sql
   CREATE DATABASE task_management;
   ```

6. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Start the backend server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd task-management/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file in the frontend directory:
   ```
   REACT_APP_API_URL=http://localhost:8000/api
   ```

4. Start the frontend development server:
   ```bash
   npm start
   ```

The application should now be running with:
- Backend at http://localhost:8000
- Frontend at http://localhost:3000

## API Documentation

### Authentication Endpoints

#### Register User
- **URL**: `/api/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "user@example.com",
    "password": "string"
  }
  ```
- **Success Response**: `201 Created`
  ```json
  {
    "id": "integer",
    "username": "string",
    "email": "string"
  }
  ```

#### Login
- **URL**: `/api/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Success Response**: `200 OK`
  ```json
  {
    "access": "string",
    "refresh": "string"
  }
  ```

#### Refresh Token
- **URL**: `/api/token/refresh/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "refresh": "string"
  }
  ```
- **Success Response**: `200 OK`
  ```json
  {
    "access": "string"
  }
  ```

### Project Endpoints

#### List Projects
- **URL**: `/api/projects/`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer <token>`
- **Success Response**: `200 OK`
  ```json
  [
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "created_at": "datetime",
      "user": "integer"
    }
  ]
  ```

#### Create Project
- **URL**: `/api/projects/`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "title": "string",
    "description": "string"
  }
  ```
- **Success Response**: `201 Created`

#### Get Project Details
- **URL**: `/api/projects/<id>/`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer <token>`
- **Success Response**: `200 OK`
  ```json
  {
    "id": "integer",
    "title": "string",
    "description": "string",
    "created_at": "datetime",
    "user": "integer"
  }
  ```

#### Update Project
- **URL**: `/api/projects/<id>/`
- **Method**: `PUT`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "title": "string",
    "description": "string"
  }
  ```
- **Success Response**: `200 OK`

#### Delete Project
- **URL**: `/api/projects/<id>/`
- **Method**: `DELETE`
- **Headers**: `Authorization: Bearer <token>`
- **Success Response**: `204 No Content`

### Task Endpoints

#### List Tasks
- **URL**: `/api/tasks/`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer <token>`
- **Query Parameters**:
  - `project`: Filter by project ID
  - `status`: Filter by status (pending, in_progress, completed)
- **Success Response**: `200 OK`
  ```json
  [
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "status": "string",
      "due_date": "date",
      "created_at": "datetime",
      "project": "integer",
      "user": "integer"
    }
  ]
  ```

#### Create Task
- **URL**: `/api/tasks/`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "title": "string",
    "description": "string",
    "status": "string",
    "due_date": "date",
    "project": "integer"
  }
  ```
- **Success Response**: `201 Created`

#### Get Task Details
- **URL**: `/api/tasks/<id>/`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer <token>`
- **Success Response**: `200 OK`
  ```json
  {
    "id": "integer",
    "title": "string",
    "description": "string",
    "status": "string",
    "due_date": "date",
    "created_at": "datetime",
    "project": "integer",
    "user": "integer"
  }
  ```

#### Update Task
- **URL**: `/api/tasks/<id>/`
- **Method**: `PUT`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "title": "string",
    "description": "string",
    "status": "string",
    "due_date": "date",
    "project": "integer"
  }
  ```
- **Success Response**: `200 OK`

#### Delete Task
- **URL**: `/api/tasks/<id>/`
- **Method**: `DELETE`
- **Headers**: `Authorization: Bearer <token>`
- **Success Response**: `204 No Content`

### Error Responses

All endpoints may return the following error responses:

#### Authentication Errors
- `401 Unauthorized`
  ```json
  {
    "detail": "Authentication credentials were not provided."
  }
  ```
- `403 Forbidden`
  ```json
  {
    "detail": "You do not have permission to perform this action."
  }
  ```

#### Validation Errors
- `400 Bad Request`
  ```json
  {
    "field_name": [
      "Error message"
    ]
  }
  ```

#### Not Found Error
- `404 Not Found`
  ```json
  {
    "detail": "Not found."
  }
  ```

## Project Structure

```
task-management/
├── backend/
│   ├── api/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── taskmanager/
│   │   ├── settings.py
│   │   └── urls.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── Dashboard.js
    │   │   ├── Login.js
    │   │   ├── Register.js
    │   │   └── ProjectView.js
    │   └── App.js
    └── package.json
```
