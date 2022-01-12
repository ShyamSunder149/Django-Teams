from django.db import models

# Create your models here.
class TeamsList(models.Model):
    name = models.CharField(max_length=200)
    no_of_members = models.IntegerField()
    team_type = models.CharField(max_length=200)
