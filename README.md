# django-package-example

## Overview

This provides a Django project which can be used as a 'container' to test re-usable Django applications.

This is intentionally a very basic Django project; it includes just enough code and configuration to allow another application to be added to `settings.INSTALLED_APPS`. It includes a `base.html` template and the settings for a functional `{% static %}` tag.

## Requirements

- Any Python environment capable of running Django.
- I think the Python environment will require building with SQlite support (which is the default in almost all cases); however I've not tested running without.

## Installation

This is designed to be checked out into an existing Django application tree:

    $ cd myapp
    $ git clone --depth 1 https://github.com/jonatkinson/django-package-example example/

## Usage

I expect this will be run as part of a CI job, to test a Django application. The subject application can be added to the project using the `ADDITIONAL_APPS` environment variable:

    $ ADDITIONAL_APPS=myapp1,myapp2 ./manage.py test

This will run the project tests with the following configuration:

    INSTALLED_APPS = [
        ...
        "myapp1",
        "myapp2",
    ]

## Todo

- Document a minimal Github workflow for checking this out into an existing package CI job.
