### Application setup
#### Steps:

- Create a new directory $ mkdir ~/projects
- Go to the projects folder $ cd projects
- git clone this repository
- Create a virtualenv
- Install dependencies 
- Configure your .env variables
- Run migrations ./manage.py migrate
- Create superuser ./manage.py createsuperuser
- The .env file is actually a text file with a pairs VARIABLE=VALUE. This file should contain the following VARIABLE=VALUE pairs:
````
SECRET_KEY=django-insecure-@bg2x8^-wbe7qk%m7fa!d+kx7*m&&)=x=v^n-(@7crh)=mlbz^
DEBUG=True
ALLOWED_HOSTS=*
````