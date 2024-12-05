# **Task Management System**

A full-stack Task Management System built using **FastAPI** for the backend and **React** for the frontend. The system allows users to manage tasks, collaborate in teams, and streamline workflow management. It demonstrates essential concepts like RESTful APIs, authentication, state management, and containerization.

---

## **Features**

- **User Authentication:** Secure login using JWT tokens.
- **Task Management:** Create, read, update, and delete tasks.
- **Team Collaboration:** Manage and view teams with ease.
- **API Integration:** Seamless interaction between frontend and backend.
- **Testing:** Unit tests for backend functionality.
- **Containerization:** Dockerized setup for deployment.

---

## **Project Structure**

### Backend
```plaintext
backend/
├── app/
│   ├── auth/          # User authentication logic
│   ├── tasks/         # Task CRUD operations
│   ├── teams/         # Team collaboration logic
│   ├── models.py      # Database models
│   ├── routes.py      # REST API routes
│   └── utils.py       # Utility functions
├── config.py          # Configurations (env-based)
├── requirements.txt   # Backend dependencies
└── tests/             # Unit tests
```

### Frontend
```plaintext
frontend/
├── src/
│   ├── components/    # React components (Navbar, TaskItem, TeamCard)
│   ├── pages/         # Pages (Dashboard, Login, Tasks, Teams)
│   ├── services/      # API service calls
│   ├── App.js         # Main entry point
│   └── styles.css     # Global styles
├── public/
│   └── index.html     # Static HTML template
├── package.json       # Frontend dependencies
```

### Root 
```plaintext
├── docker-compose.yml  # Docker setup
├── README.md           # Project documentation
└── .github/
    └── workflows/      # GitHub Actions for CI/CD
```

### Tech Stack
### Backend
FastAPI: High-performance Python web framework.
SQLAlchemy: Database ORM.
PostgreSQL: Relational database.
JWT: Secure user authentication.

### Frontend
React: JavaScript library for building user interfaces.
Axios: HTTP client for API calls.

### Tools
Docker: Containerization for easy deployment.
GitHub Actions: CI/CD workflows.

### Getting Started
### Prerequisites
Python 3.9+
Node.js 14+
Docker

### Backend Setup

1.  Navigate to the backend directory:

    bash

    Copy code

    `cd backend`

2.  Install dependencies:

    bash

    Copy code

    `pip install -r requirements.txt`

3.  Set up environment variables:\
    Create a `.env` file in the backend directory:

    dotenv

    Copy code

    `DATABASE_URL=postgresql://user:password@localhost/task_management
    SECRET_KEY=your_secret_key`

4.  Run the FastAPI server:

    bash

    Copy code

    `uvicorn app.routes:app --reload`

5.  Access the API documentation: Open http://localhost:8000/docs for Swagger UI.

* * * * *

### Frontend Setup

1.  Navigate to the frontend directory:

    bash

    Copy code

    `cd frontend`

2.  Install dependencies:

    bash

    Copy code

    `npm install`

3.  Start the development server:

    bash

    Copy code

    `npm start`

4.  Access the app: Open http://localhost:3000 in your browser.

* * * * *

### Docker Setup

1.  Ensure Docker is running.

2.  Run the project using `docker-compose`:

    bash

    Copy code

    `docker-compose up --build`

3.  Access the services:

    -   Backend: [http://localhost:8000](http://localhost:8000/)
    -   Frontend: http://localhost:3000

* * * * *

Testing
-------

### Backend Tests

Run unit tests for the backend:

bash

Copy code

`pytest`
