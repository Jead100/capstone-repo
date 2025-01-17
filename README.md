Here’s a `README.md` file tailored to your Django project setup (`littlelemon`) and the instructions provided. It includes steps for setting up the virtual environment, installing dependencies, and testing the API paths:

---

# LittleLemon Restaurant Project

Welcome to the LittleLemon Django project! This project is a restaurant management system built using Django. Below are the instructions to set up the project locally and test the provided API endpoints.

---

## Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone <repository-url>
cd littlelemon
```

---

### 2. Set Up a Virtual Environment
It is recommended to create and activate a virtual environment to isolate the project dependencies.

#### On macOS/Linux:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

#### On Windows:
```bash
python -m venv myenv
myenv\Scripts\activate
```

---

### 3. Install Dependencies
Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

### 4. Run Migrations
Apply the database migrations to set up the database:
```bash
python manage.py migrate
```

---

### 5. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

The server will run at `http://127.0.0.1:8000/`.

---

## API Endpoints to Test

Here are the API paths you can test:

- **Bookings API**:  
  `GET /api/bookings/` - Retrieve a list of bookings.  
  `POST /api/bookings/` - Create a new booking.

- **Registration API**:  
  `POST /api/registration/` - Register a new user.

---

## Additional Notes
- Ensure you have Python 3.x installed on your system.
- If you encounter any issues, please refer to the Django documentation or reach out for assistance.

---

Happy testing! 🚀

---

### Explanation of the README:
1. **Cloning the Repository**: This step ensures your peer has the project files locally.
2. **Virtual Environment**: Encourages isolation of dependencies to avoid conflicts.
3. **Installing Dependencies**: Uses `requirements.txt` to install all necessary packages.
4. **Running Migrations**: Sets up the database schema.
5. **Running the Server**: Starts the Django development server for testing.
6. **API Endpoints**: Lists the paths your peer can test, as per your instructions.

Save this content in a file named `README.md` in the root of your project directory (`littlelemon`). This will make it easy for your peer to follow the setup process and test the APIs. 😊
