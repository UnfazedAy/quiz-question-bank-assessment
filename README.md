# Quiz question bank API

This is a simple API for a quiz question bank. It is built using Django and Django Rest Framework. It is a simple API with the following features.

This project is build using **Python Django** Framework.

## Features

- Add, Update, Delete and View Questions
- Can only delete questions if you are authenticated
- Automatically delete associated options and answers when a question is deleted

## Installation

### Requirements

- Python 3.7 or above

### Clone the repository

```bash
git clone https://github.com/ilyasbabu/question-bank-management-system.git
cd question-bank-management-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Setup the eviornment variables

Create a file named `.env` in the root directory of the project and add the following lines to it

```bash
# Database configuration
DB_NAME = "<database_name>"
DB_USER = "<database_user>"
DB_PASSWORD = "<database_password>"
DB_HOST = "<database_host>"
DB_PORT = "<database_port>"

### Create the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create the admin user

```bash
python manage.py createsuperuser
```

### Start the server

```bash
python manage.py runserver
```

# Quiz Bank

A simple quiz question bank API which contains simple CRUD operations on Questions, options and answers.

## End-point: Create question

Takes a raw body content and creates the question, options and answer associated with it.

### Method: POST
>
>```
>http://localhost:8000/quiz/create-question/
>```
>
### Body (**raw**)

```json
{
  "question_text": "What is the capital of France?",
  "options": [
    {"A": "Berlin", "is_correct": false},
    {"B": "Paris", "is_correct": true},
    {"C": "Madrid", "is_correct": false}
  ],
  "answer": {"B": "Paris"}
}

```

## Documentation

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get all questions

Get all questions in the database alongside their options and answer

### Method: GET
>
>```
>http://localhost:8000/quiz/get-questions/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get single question

Retrieves a single question with associated options by the question ID

### Method: GET
>
>```
>http://localhost:8000/quiz/get-question/647202da65974cde8770ddce7bdc7870
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete single question by ID

Deletes a single question based on it's ID and delete all options and example related to it

### Method: DELETE
>
>```
>http://localhost:8000/quiz/delete-question/6fdfda1d0ba243d5900790bc9d735c97
>```
>
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|

### Headers

|Content-Type|Value|
|---|---|
|Authorization|Token dummy_token|

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Question by ID

Updates the question or it's associated options and answer based on the question id

### Method: PUT
>
>```
>http://localhost:8000/quiz/update-question/6fdfda1d0ba243d5900790bc9d735c97/
>```
>
### Body (**raw**)

```json
{
  "question_text": "What is the capital of Nigeria?",
  "options": [
    {"A": "Lagos", "is_correct": false},
    {"B": "Abuja", "is_correct": true},
    {"C": "Madrid", "is_correct": false}
  ],
  "answer": {"B": "Abuja"}
}

```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete all questions

Takes in a token / dummy token and as some autorization and deletes all questions in DB.

### Method: DELETE
>
>```
>http://localhost:8000/quiz/delete-all-questions/
>```
>
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|

### Headers

|Content-Type|Value|
|---|---|
|Authorization|Token dummy_token|

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
