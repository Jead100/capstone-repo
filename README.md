---

# LittleLemon Restaurant Project

Welcome to the LittleLemon Django project! The Capstone project of the Back-End Developer Program. Below are the instructions to set up the project locally and test the provided API endpoints.

---

## Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/Jead100/capstone-repo.git
cd littlelemon
```

---

### 2. Set Up a Virtual Environment
It is recommended to create and activate a virtual environment to isolate the project dependencies.

#### On macOS/Linux:
```bash
python3 -m venv <env-name>
source <env-name>/bin/activate
```

#### On Windows:
```bash
python -m venv <env-name>
<env-name>\Scripts\activate
```

---

### 3. Install Dependencies
Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

### 4. Set Up MySQL Database
This project uses MySQL as the database backend. Ensure you have MySQL installed and running on your system.

1. Open the `settings.py` file in your project directory (`littlelemon/settings.py`).
2. Locate the `DATABASES` configuration section.
3. Replace the placeholder values with your MySQL database credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',  # Or your MySQL host
           'PORT': '3306',       # Default MySQL port
       }
   }
   ```

4. Save the changes.

---

### 5. Run Migrations
Apply the database migrations to set up the database:
```bash
python manage.py migrate
```

---

### 6. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

The server will run at `http://127.0.0.1:8000/`.

---

## API Endpoints to Test

Here are the API paths you can test:

### Menu API:
- **Create a new menu item**:  
  `POST /restaurant/menu/`
- **Retrieve a list of menu items**:  
  `GET /restaurant/menu/`

### Booking API:
- **Make a reservation**:  
  `POST /restaurant/booking/`
- **Retrieve a list of reservations**:  
  `GET /restaurant/booking/`

---

## Additional Notes
- Ensure you have Python 3.x and MySQL installed on your system.
- If you encounter any issues, please refer to the Django documentation or reach out for assistance.

---

Happy testing! 🚀

---
