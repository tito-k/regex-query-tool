# Regex Query Tool

This is a Django-based tool that matches a string based on a user-provided regular expression. The tool offers options for a Full Match of the String and First Match of the String. The project also includes Swagger for API documentation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python3, Pip and Virtualenv installed on your system.

### Installing

Follow these steps to run this project on your local machine:

1. First, clone the repository to your local machine:

```bash
git clone https://github.com/tito-k/regex-query-tool
```

2. Navigate to the project directory:
```bash
cd regex-query-tool
```

3. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `.\venv\Scripts\activate.bat`
```

4. Install the project dependencies:
```bash
pip install -r requirements.txt
```

5. Run the migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Start the server:
```bash
python manage.py runserver
```

Now, you can navigate to http://localhost:8000/regex-query in your browser to view the application, and http://localhost:8000/docs/ to view the Swagger API documentation.

## Built With
- [Python](https://www.python.org/) - The programming language used
- [Django](https://www.djangoproject.com/) - The web framework used
- [Django REST Framework](https://www.django-rest-framework.org/) - Toolkit for building Web APIs
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) - Yet Another Swagger Generator for Django REST Framework
