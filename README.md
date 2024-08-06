# Django Mysite

This is a simple Django application for creating and voting on polls. Users can create questions with multiple choices, and others can vote on their favorite choices.

## Features

- Create new poll questions.
- Add multiple choices to each question.
- Vote on choices for each question.
- View poll results.

## Prerequisites

- Python 3.12.4
- Django 5.0.7
- SQLite (default database)

## Setup Python and Django
- Install Pip
Open the command prompt and enter the following command
`
  python -m pip install -U pip
`

- Download Python 
Go to the [[Python website](https://www.python.org/downloads/)] and download the latest version of Python.

- Install Python
Follow the instructions to install Python on your system. Make sure to check the box to add Python to your PATH during the installation.

-Verify Python Installation
`
    python --version
`

- Install Pip
pip is included with Python, but you can ensure you have the latest version by running:
`
    python -m ensurepip --upgrade
`

- Install Django:
Install django by giving following command:
 
`
  pip install django
`

## Installation

Clone the repository
```
    git clone (https://github.com/Minyasei/my-site.git)
```
Apply migrations:
```
    python manage.py migrate
```
Create a superuser to access the admin interface:
```
    python manage.py createsuperuser
```
Run the development server:
```
    python manage.py runserver
```
- Open your web browser and go to `http://127.0.0.1:8000` to see the app.

## Usage

1. Log in to the admin interface at `http://127.0.0.1:8000/admin` using the superuser account you created.
2. Create new poll questions and add choices.
3. Go to the main polls page to vote on the questions.

## Project Structure

  - `polls/`: Contains the main app for the polls.
  - `models.py`: Contains the data models for the polls app.
  - `views.py`: Contains the view logic for the app.
  - `urls.py`: URL routing for the polls app.
  - `templates/polls/`: Contains the HTML templates for the app.
  - `my-site/`: Contains project-wide settings and configurations.
  - `settings.py`: Django settings for the project.
  - `urls.py`: URL routing for the project.
  - `manage.py`: Command-line utility for administrative tasks.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

