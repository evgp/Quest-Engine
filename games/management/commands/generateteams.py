from django.core.management.base import BaseCommand, CommandError
from django.db import models
from django.contrib.auth.models import Group, User  
import names

class Command(BaseCommand):
    help = 'Create ARG teams x ARG players'

    def add_arguments(self, parser):
        # parser.add_argument('args') # to use *args
        parser.add_argument('teams', type=int)
    
    def handle(self, *args, **options):
        i = 0
        while i < options['teams']:
            j = 0
            new_group = Group.objects.create(name='Team ' + names.get_first_name())
            new_group.save()
            self.stdout.write(self.style.SUCCESS(new_group.name + ' successfuly created.'))
            i += 1
            while j < options['teams']:
                new_user = User.objects.create_user(username=names.get_last_name(), password=1)
                new_user.groups.add(new_group.id)
                new_user.save()
                self.stdout.write(self.style.SUCCESS(new_user.get_username() + ' added to ' + new_group.name))
                j += 1
