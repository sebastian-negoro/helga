import uuid
from django.db import models
from datetime import datetime

class HockeyMatch(models.Model):
	match_id = models.UUIDField(default=uuid.uuid4, editable=False)
	marathon_link = models.CharField(max_length=100, blank=True)
	bet_link = models.CharField(max_length=100, blank=True)
	first_team = models.CharField(max_length=100)
	second_team = models.CharField(max_length=100)
	has_ended = models.BooleanField(default=False)
	created_time = models.DateTimeField(auto_now=False, auto_now_add=True)

class HockeyTeam(models.Model):
	standard_name = models.CharField(max_length=100, default='')
	marathon_name = models.CharField(max_length=100)
	bet_name = models.CharField(max_length=100)


# Create your models here.
