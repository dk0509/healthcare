# 🏥 Healthcare Backend API
A Django REST Framework-based backend for managing Patients, Doctors, and their Mappings.The system allows users to register, log in, and manage patient and doctor records securely.


## Features
- Patient CRUD operations
- Doctor CRUD operations
- Map Doctors to Patients
- Get all doctors assigned to a patient
- Remove a doctor from a patient
- Token-based Authentication

## 📦 Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Auth:** JWT Authentication (djangorestframework-simplejwt)
- **Env Config:** python-decouple

## 🛠️ Setup Instructions
1.  **Clone the repo**
    ```bash
    git clone https://github.com/dk0509/healthcare
    cd healthcare
    ```
2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate  
    # On macOS/Linux
    source venv/bin/activate 
    ```
3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure `.env` file**
    Create a `.env` file in the root directory:
    ```env
    SECRET_KEY=your-secret-key
    DEBUG=True
    DB_NAME=healthcare_db
    DB_USER=postgres
    DB_PASSWORD=yourpassword
    DB_HOST=localhost
    DB_PORT=5432
    ```
5.  **Set Up PostgreSQL**
    Install PostgreSQL.
    Create a database named `healthcare_db`.
    ```sql
    CREATE DATABASE healthcare_db;
    ```
6.  **Run Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

## 📬 API Endpoints

### Auth
- **POST** `/api/auth/register/` –  Register a new user with name, email, and password.
- **POST** `/api/auth/login/` – Log in a user and return a JWT token.

### Patients
- **GET** `/api/patients/` – List all patients created by authenticated user.
- **POST** `/api/patients/` – Add a patient
- **GET** `/api/patients/<id>/` – Retrieve patient
- **PUT** `/api/patients/<id>/` – Update patient
- **DELETE** `/api/patients/<id>/` – Delete patient

### Doctors
- **GET** `/api/doctors/` – List all doctors
- **POST** `/api/doctors/` – Create doctor
- **GET** `/api/doctors/<id>/` – Retrieve doctor
- **PUT** `/api/doctors/<id>/` – Update doctor
- **DELETE** `/api/doctors/<id>/` – Delete doctor

### Mappings (Patient ↔ Doctor)
- **GET** `/api/mappings/` – List all mappings
- **POST** `/api/mappings/` – Assign doctor to patient
- **GET** `/api/mappings/<patient_id>/` – Get doctors assigned to patient
- **DELETE** `/api/mappings/<id>/` – Remove doctor from patient



## 📂 Project Structure
```bash
healthcare/
├── healthcare/        # Django settings and root URLs
├── accounts/          # Accounts app
├── patients/          # Patients app
├── doctors/           # Doctors app
├── mappings/          # Mapping app
├── venv/              # Virtual environment
├── .env               # Environment variables
└── manage.py