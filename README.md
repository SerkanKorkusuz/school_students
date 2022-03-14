## API School & Students

This work up is a challenging project and intended to show a broad array of topics of the backend technologies. It is also aimed to create and build APIs with Django.
## Remarks
- Before starting, [install Pipenv](https://pipenv.pypa.io/en/latest/install/)
- Use the Python dependency manager [Pipenv](https://pipenv.pypa.io/en/latest/install/) to create the virtual environment and install all of the dependencies as needed.
```bash
pipenv install
```
- Insert the variables of the secret key, postgresql credientials and django admin user ``SECRET KEY``, ``DATABASE_USER``, ``DATABASE_PASSWORD``, ``DATABASE_NAME``, ``DATABASE_HOST``, ``DATABASE_PORT``, ``DJANGO_SUPERUSER_USERNAME``, ``DJANGO_SUPERUSER_EMAIL`` and ``DJANGO_SUPERUSER_PASSWORD`` into ``./school_students/.env`` directory.
- Execute the command below from the project's root directory to source the variables newly added into the environment file:
```bash
source ./school_students/.env
```
- Another way to set environment variables can be done by exporting or setting them on the operating system
- After setting the virtual environment and environment variables, execute the commands respectively:
```bash
python manage.py makemigrations
python manage.py migrate
```
- There are three management commands to be used:
  - ``python manage.py check_superuser --username=${DJANGO_SUPERUSER_USERNAME} --email=${DJANGO_SUPERUSER_EMAIL} --password=${DJANGO_SUPERUSER_PASSWORD}`` (to check and create a superuser non-interactively if it does not exist)
  - ``python manage.py loaddata initial_school_data`` (to insert the initial load data instances of the class ``School``)
  - ``python manage.py loaddata initial_student_data`` (to insert the initial load data instances of the class ``Student``)
- To start the program, run the command below after completing the steps above:
```bash
python manage.py runserver 
```
- Go to [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) for Django administration.
- Go to [127.0.0.1:8000/api/schools/](http://127.0.0.1:8000/api/schools/) ``[GET, POST]`` for the browsable API of the model ``School``.
- Go to [127.0.0.1:8000/api/students/](http://127.0.0.1:8000/api/students/) ``[GET, POST]`` for the browsable API of the model ``Student``.
- Other available endpoints:
  - ``api/schools/:id`` ``[GET, PUT, PATCH, DELETE]``
  - ``api/students/:id`` ``[GET, PUT, PATCH, DELETE]``
  - ``api/schools/:id/students`` ``[GET, POST]``
  - ``api/schools/:id/students/:id`` ``[GET, PUT, PATCH, DELETE]``

## Guideline Notes
- Delivering this work up of the test assignment took around 6 hours for me to complete along with creating and populating fake initial data. It can be distributed as one hour for Step One, two hours for Step Two, one hour for Step Three and two hours for some Bonus items. 
## Contact
Pull requests are welcome. You can also email to korkusuzs18@itu.edu.tr