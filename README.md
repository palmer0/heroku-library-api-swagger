# Library REST API with Swagger docs

[![CircleCI](https://circleci.com/gh/jesuscg/library-api-swagger/tree/master.svg?style=shield)](https://circleci.com/gh/jesuscg/library-api-swagger/tree/master) [![Coverage Status](https://coveralls.io/repos/github/jesuscg/library-api-swagger/badge.svg?branch=master)](https://coveralls.io/github/jesuscg/library-api-swagger?branch=master) [![Code Health](https://landscape.io/github/jesuscg/library-api-swagger/master/landscape.svg?style=flat)](https://landscape.io/github/jesuscg/library-api-swagger/master)



This project is intended to handle library books and authors.

This example includes all **CRUD** operations needed for both models built with the Django Rest Framework. Also, it is documented with a pretty **Swagger UI**. All requests are made taking care about CORS headers using **django-cors-headers** django package, making easier testing in localhost.

## Getting Started

### Requirements

* [Python](https://www.python.org/): 2.7, 3.5
* [Django](https://www.djangoproject.com/): 1.8, 1.9, 1.10
* [Django REST Framework](http://www.django-rest-framework.org/): 2.4+
* [django-cors-headers](https://github.com/ottoyiu/django-cors-headers)

### Installing

Clone or fork the repo to your local directory.

For a quick local test, you can install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html) to create a **virtual environment**.

Install the **requirements/local.txt** file by using `pip` inside the virtualenv:

```
$ cd library-api-swagger
$ pip install -r requirements/local.txt
```

Create database models:
```
$ python manage.py migrate --settings=config.settings.local
```

Finally, run the localhost server:

```
$ python manage.py runserver --settings=config.settings.local
```

### Start Example

If you are in a local environment, visit:

* ```localhost:8000/api/v1/``` to see your browsable API from Django REST Framework interface.

* ```localhost:8000/api/v1/docs/``` to see Swagger UI documentation scheme.

## Running the tests

To execute the application tests, run:
```
$ cd library-api-swagger/api
$ python manage.py test --settings=config.settings.local
```

## Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/palmer0/heroku-library-api-swagger)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
