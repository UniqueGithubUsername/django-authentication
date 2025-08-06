<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/UniqueGithubUsername/django-authentication">
    <img src="main/static/main/django.png" alt="Logo" width="80" height="80">
  </a>
</div>

# Django Authentication

This is a django application which uses a customized setup of the django user authentication __django.contrib.auth__.

This repository is mainly for documentation of the implementation of the authentication system.

While for many applications writing an own authentication backend can be handy or necessary, here the initial authentication backend model is used and not changed. The focus is on extending the existing user model and implementing the _registration_, _login_ and _logout_ functionalities.

## Installation

Before using this repository please make sure you have the following dependencies installed.

### Dependencies

[![Python][Python]][Python-url]
[![Django][Django]][Django-url]

### Usage

Usage of the repo:

```sh
git clone https://github.com/UniqueGithubUsername/django-authentication.git
cd DjangoAuthentication
python manage.py runserver
```

## About me

Lukas Lenz

[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/lukas-lenz

[Python]: https://img.shields.io/badge/python-yellow?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/

[Django]: https://img.shields.io/badge/django-092e20?style=for-the-badge&logo=django
[Django-url]: https://www.djangoproject.com/

[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/