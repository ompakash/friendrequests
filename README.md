# Django Friend Request System

This project is a Django-based backend system that implements user authentication, friend request functionality, and rate limiting on friend requests. It uses Django REST Framework for API endpoints.

### Postman Documentation = https://documenter.getpostman.com/view/23480640/2sA3kXCzMt

## Features

- User signup and login
- Search users by email or name
- Friend request sending, accepting, and rejecting
- List of friends and pending friend requests
- Rate limiting on sending friend requests (max 3 requests per minute)

## Installation

- create a virtual env "python -m virtualenv demoEnv"
- activte virtual env "demoEnv\Scripts\activate"
- clone repo "git clone https://github.com/ompakash/friendrequests.git"
- "cd friendrequests"
- install requirements "pip install -r requirements.txt "
- run server "python manage.py runserver"

### Prerequisites

- Python 3.12.4
- Django 5.0.7
- Django REST Framework 3.15.2

### Setup Instructions

1. **Clone the repository**
   git clone [<repository-url>](https://github.com/ompakash/friendrequests.git)
   
