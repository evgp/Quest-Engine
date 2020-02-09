from django.shortcuts import render
from django.utils import timezone
from games.models import Game


def upcoming(request):
    qs = Game.objects.all().filter(start_time__lte=timezone.now())
    context= {'games': qs}
    return render(request, template_name='games/index.html', context=context)

# Create your views here.

# list all the games available
# with a button to join and start the game

