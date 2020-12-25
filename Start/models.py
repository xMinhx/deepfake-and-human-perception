from django.db import models
from django.contrib.sessions.models import Session
# Create your models here.


class Gender(models.Model):
    label_name = models.TextField(unique=True)
    label_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'gender'


class Difficulty(models.Model):
    label_id = models.IntegerField(primary_key=True)
    label_name = models.TextField(unique=True)

    class Meta:
        db_table = 'difficulty'


class Class(models.Model):
    label_id = models.IntegerField(primary_key=True)
    label_name = models.TextField(unique=True)

    class Meta:
        db_table = 'class_label'

class Testgroup(models.Model):
    label_id = models.IntegerField(primary_key=True)
    label_name = models.TextField(unique=True)

    class Meta:
        db_table = 'testgroup'


class User(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    testgroup = models.ForeignKey(Testgroup, on_delete=models.PROTECT)
    age = models.IntegerField()
    pixel_width = models.IntegerField()
    pixel_height = models.IntegerField()
    fps = models.DecimalField(max_digits=4, decimal_places=3)

    class Meta:
        db_table = 'user'
