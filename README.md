# inerG API
Ohio Quarterly production data API for inerG Technical Test

## Installation
Clone the repo `git clone https://github.com/AlfredConlan/inerg-api.git`

Open the project in your editor

In the terminal enter `pipenv install` to make sure you have the dependencies

In the terminal enter `pipenv shell` to start the virtual environment

## Running and Testing

In the terminal enter `python main.py`

Look for the message `Running on http://localhost:8080` in the terminal

Test the app by calling the API in the following format `http://localhost:8080/data?well=34059242540000`

You may use any valid well number in the call
