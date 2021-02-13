from django.db import models
from django.contrib.sessions.models import Session
import django.contrib.postgres.fields



#Domain for gender
class Gender(models.Model):
    label_name = models.TextField(unique=True)
    label_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'gender'

#Domain for difficulty
class Difficulty(models.Model):
    label_id = models.IntegerField(primary_key=True)
    label_name = models.TextField(unique=True)

    class Meta:
        db_table = 'difficulty'

#Domain for class
class Class(models.Model):
    label_id = models.IntegerField(primary_key=True)
    label_name = models.TextField(unique=True)

    class Meta:
        db_table = 'class_label'

#Domain for testgroups
class Testgroup(models.Model):
    label_id = models.IntegerField(primary_key=True)
    label_name = models.TextField(unique=True)

    class Meta:
        db_table = 'testgroup'

#Definition of userdata set
class User(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    testgroup = models.ForeignKey(Testgroup, on_delete=models.PROTECT)
    device = models.TextField(default=None, blank=True, null=True)
    age = models.IntegerField()
    pixel_width = models.IntegerField()
    pixel_height = models.IntegerField()
    fps = models.IntegerField()

    class Meta:
        db_table = 'user'

#Definition of scoreboard dataset
class Scoreboard(models.Model):
    id = models.AutoField(primary_key=True)
    scores = models.JSONField()
