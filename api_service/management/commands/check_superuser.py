from django.core.management.base import CommandParser
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


# python manage.py check_superuser --username=${DJANGO_SUPERUSER_USERNAME} --email=${DJANGO_SUPERUSER_EMAIL}
# --password=${DJANGO_SUPERUSER_PASSWORD}
class Command(BaseCommand):
    help = 'Creates a superuser non-interactively if it does not exist'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--username', help='Username of the superuser')
        parser.add_argument('--email', help='Email of the superuser')
        parser.add_argument('--password', help='Password of the superuser')

    def handle(self, *args, **kwargs):
        user = get_user_model()
        if not user.objects.filter(username=kwargs['username']).exists():
            try:
                user.objects.create_superuser(username=kwargs['username'],
                                              email=kwargs['email'],
                                              password=kwargs['password'])
                print('The superuser is successfully created.')
            except Exception as ex:
                print(f'An error has happened while creating the superuser: {ex}')
        else:
            print(f'The superuser with the name {kwargs["username"]} is already registered.')
