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
            j = 0 # levels loop
            new_game = Game()
            new_game.title = names.get_last_name() + ' game'
            # query objects with no place
            new_game.sequence = Game.objects.filter(place__exact=None).count()
            # game start time 1 day ahead
            new_game.start_time = timezone.now() + datetime.timedelta(1)
            new_game.save()
            new_game.authors.add(i+1)
            new_game.authors.add(5)
            new_game.save()
            self.stdout.write(self.style.SUCCESS(new_game.title + ' created'))
            while j < 10:
                new_lvl = Level(title=names.get_full_name() + ' level', game=new_game)
                new_lvl.level_type = 'Standart'
                new_lvl.duration = datetime.timedelta(hours=1)
                new_lvl.sequence = Level.objects.filter(game__exact=new_game).count()
                new_lvl.save()
                j += 1
            i += 1

            # add levels with timedelta
            # add child levels with timedelta
            # add codes
