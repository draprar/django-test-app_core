# Driving Test App

Driving Test App is my Django-based core application that allows users to practice (here: driving) test questions. The app includes a timed quiz, score tracking, and an admin panel for content management.


## Features

- **User Authentication**:
  - Secure login and logout functionality.
  - User session tracking for test attempts.
- **Quiz Functionality**:
  - A randomly generated 20-question quiz with a 20-minute timer.
  - Score calculation based on correct answers.
  - Results are stored for each user.
- **Admin Content Management**:
  - Admins can manage:
    - Questions.
    - Answers with correctness flags.
    - User test results.
- **Responsive Design**:
  - Optimized for both desktop and mobile devices.
- **Secure Practices**:
  - Protection of user data and HTTPS enforcement for production.

---

## Installation

### Requirements

- Python 3.10+
- Django 5.1.3
- SQLite (default) or another database engine for production
- `pytest` for testing
- `django-environ` for environment variable management

---

### Step-by-Step Guide

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/driving-test-app.git
   cd driving-test-app
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root with the following content:

   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=*
   ```

5. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the application:**

   - Main page: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Testing

Run tests using `pytest`:

   ```bash
   pytest
   ```

---



---

## Deployment Notes

For production, ensure the following:

- **Security Settings**:
  - Set `DEBUG=False` in `settings.py`.
  - Use a strong, unique `SECRET_KEY`.
  - Configure `ALLOWED_HOSTS` appropriately.
- **HTTPS**:
  - Enable `SECURE_SSL_REDIRECT` and `CSRF_COOKIE_SECURE`.
- **Static Files**:
  - Use a service like AWS S3, or configure WhiteNoise for static file serving.
- **Database**:
  - Use a production-ready database like PostgreSQL.

---

## License

This project is licensed under the MIT License.

Developed by Walery.#   d j a n g o - t e s t - a p p _ c o r e  
 