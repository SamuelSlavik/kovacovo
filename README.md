# Kovacovo Web App

## Project description
Web app for lumber association Kovacovo-Javorina. Minimalistic app focused on simplicity and functionality.

## Technologies / Stack

### Frontend
- Vue 3 Composition API, Typescript
- CSS
- Pinia, Axios, VueRouter

### Backend
- FastAPI, Python
- SQLAlchemy

### Database
- PostgreSQL

## LOCAL SETUP
### Frontend

1. Clone the repository and install dependencies in the /frontend.

    ```npm install```

2. Change the base url based to point on your running backend server in the file frontend/lib/endpoints.ts
Run the frontend server

    ```npm run dev```

### Backend

1. Clone the repository and install dependencies in the /backend:

    ```pip install -r requirements.txt```

2. Setup postgres database, you can use the provided docker-compose file or some online tutorial.

3. Change the backend/core/config.py according to your needs.

4. Run the backend server:

    ```python3 run.py```