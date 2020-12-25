from django.db import models
from Start.models import User
from Start.models import Class
from Start.models import Difficulty


# Create your models here.


class Video(models.Model):
    video_id = models.TextField(primary_key=True)
    label = models.ForeignKey(Class, on_delete=models.PROTECT)
    video_link_id = models.TextField(unique=True)

    class Meta:
        db_table = 'video'


class Classification(models.Model):
    session_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    class_field = models.ForeignKey(Class, on_delete=models.PROTECT)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT)
    play_pause = models.IntegerField()
    replay = models.IntegerField()
    fullscreen = models.IntegerField()
    playback = models.IntegerField()
    duration_in_sec = models.IntegerField()
    text = models.TextField()

    class Meta:
        db_table = 'classification'
        unique_together = (("session_id", "video_id"),)
