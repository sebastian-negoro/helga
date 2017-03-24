from django.contrib import admin

from .models import HockeyMatch, HockeyTeam

class TeamAdmin(admin.ModelAdmin):
	list_display = ('id', 'standard_name', 'marathon_name', 'bet_name')

class HockeyMatchAdmin(admin.ModelAdmin):
	list_display = ('id', 'match_id', 'first_team', 'second_team', 'created_time')

admin.site.register(HockeyMatch, HockeyMatchAdmin)
admin.site.register(HockeyTeam, TeamAdmin)

# Register your models here.
