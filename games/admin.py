from django.contrib import admin

# Register your models here.
from .models import Game, Level, Register, Code

# admin.site.register(Game)
# admin.site.register('Register')
admin.site.site_header = 'Quest Engine'


# class AuthorsInline(admin.TabularInline):
#     model = Game.authors.through

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # inlines = [
    #     AuthorsInline,
    # ]
    list_display = ('title', 'sequence')

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'game', 'level_next')

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('level', 'code', 'checkpoint_required')

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('player', 'level', 'timestamp', 'code_input')