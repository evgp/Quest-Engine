import datetime
from django.core.management.base import BaseCommand, CommandError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group, User  
from games.models import *
import names

# Command to generate 3 arbitrary number of games
# with a few levels and sublevels to see how it's look in the django admin 
# this is a prototype for the future tests

class Command(BaseCommand):
    def handle(self, *args, **options):
        i = 0
        while i < 3:
            new_game = Game()
            new_game.title = names.get_last_name() + ' game'
            # query objects with no place
            new_game.sequence = Game.objects.filter(place__exact=None).count()
            # game start time 1 day ahead
            new_game.start_time = timezone.now() + datetime.timedelta(1)
            new_game.save()
            new_game.authors.add(i)
            new_game.save()
            self.stdout.write(self.style.SUCCESS(new_game.title + ' created'))
            i += 1