<H1>**Electronic Retail Network**</H1>

<h2>Technology</h2>

* python = "^3.10"
* django = "^4.2.1"
* envparse = "^0.2.0"
* psycopg2-binary = "^2.9.6"
* djangorestframework = "^3.14.0"
* django-filter = "^23.2"
* drf-spectacular = "^0.26.2"
* django-extensions = "^3.2.1"
* pre-commit = "^3.3.2"
* PostgreSQL
* Docker-compose

<h2>Start app</h2>

* Create .env file using .env.template
* Run docker container with database
` docker-compose up -d`
* Make migrate
`./manage.py migrate`

* Create superuser
`./manage.py createsuperuser`

* Runserver
`./manage.py runserver`
