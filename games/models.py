from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

class Game(models.Model):
    sequence = models.IntegerField(verbose_name="Game number", default=0, unique=True)
    title = models.CharField(max_length=255, null=False)
    authors = models.ManyToManyField(User)
    players = models.ManyToManyField(Group, blank=True)
    start_time = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    # the place the game related to (i.e. city name)
    place = models.CharField(max_length=255, null=True, blank=True)
    # game_type 
    def __str__(self):
        return 'Game #' + ' ' + str(self.sequence) + ' ' + self.title

class Level(models.Model):
    sequence = models.IntegerField(verbose_name="Level number", default=1)
    title = models.CharField(max_length=255, null=False)
    game = models.ForeignKey('Game',on_delete=models.CASCADE)
    mission = models.TextField(null=True)
    duration = models.DurationField(verbose_name="Level duration", null=True) # A field for storing periods of time - modeled in Python by timedelta.
    level_next = models.OneToOneField('self', blank=True, null=True, on_delete=models.CASCADE, related_name="previous")
    level_parent = models.OneToOneField('self', blank=True, null=True, on_delete=models.CASCADE, related_name="child")
    LEVEL_TYPES = (
        ("Standart", "Standart level"),            # has no parent, must be completed to go further (level.next)
        ("Required", "Required child level to complete standart level"), # has a parent and must be completed to complete "Parent level"
        ("Timeout", "Timeout level for waiting in a line"),
        ("Bonus", "Bonus level"), # has a parent, but not required to be completed
    )
    level_type = models.CharField(max_length=255, choices=LEVEL_TYPES)
    # MANAGERS:
    # 1. create different types of levels
    # 
    def __str__(self):
        return self.title

class Code(models.Model):
    level = models.ForeignKey('Level',on_delete=models.CASCADE)
    code = models.CharField(max_length=255, null=False)
    checkpoint_required = models.BooleanField(verbose_name="Checkpoint required", default=False)
    
    def __str__(self):
        return self.level + " " + self.code

class Register(models.Model):
    team = models.ForeignKey(Group, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    code_input = models.CharField(max_length=255, null=False)
    timestamp = models.DateTimeField(verbose_name="Timestamp", auto_now=True)
    match = models.BooleanField(verbose_name="Input matchet the code", null=True)
    level_start = models.BooleanField(verbose_name="Level started", null=True)    
    level_complete = models.BooleanField(verbose_name="Level completed", null=True)
    checkpoint = models.BinaryField(verbose_name="Checkpoint data", blank=True, null=True)

    def __str__(self):
        return self.code_input


# rating model