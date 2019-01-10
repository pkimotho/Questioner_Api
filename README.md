
[![Build Status](https://travis-ci.org/pkimotho/Questioner_Api.svg?branch=develop)](https://travis-ci.org/pkimotho/Questioner_Api) [![codecov](https://codecov.io/gh/pkimotho/Questioner_Api/branch/develop/graph/badge.svg)](https://codecov.io/gh/pkimotho/Questioner_Api) 

# Questioner_Api
This is a version one api of Questioner application. With this api, users can send requests to application and render data.
### Installation

1. Clone the repository

    `git clone https://github.com/pkimotho/Questioner_Api.git`

2. Change to Questioner_Api directory

    `cd Questioner_Api`

3. Install virtual environment

    `virtualenv env`

4. Install the application requirements

    `pip install -r requirements.txt`

5. Export the Flask environment variable

    `export FLASK_APP=run.py`

6. Run the Application

    `flask run`

### Meetup Endpoints

| Method | Endpoint | Function |
| --- | --- | --- |
| POST | /api/v1/meetups/ | Adds a meetup |
| GET | /api/v1/meetups/upcoming | Gets all meetups |
| GET | /api/v1/meetups/meetup_id | Gets a specific meetup |
| PUT | /api/v1/meetups/meetup_id | Edits a meetup by an admin user |
| DELETE| /api/v1/meetups/ | Deletes a meetup by an admin user |


##### Author

[Kimotho](https://github.com/pkimotho)