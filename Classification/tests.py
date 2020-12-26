from django.test import TestCase

# Create your tests here.
from Start import models
from Classification import models
from django.contrib.sessions.models import Session

#x = models.Video.objects.values_list("video_id")

#for i in range(len(x)):
#    print(x[i][0])

user = models.User.objects.get(session_id="zglhb0u3v530cdpt509a5b8cfs5dwq32")
video_user_liste = models.Classification.objects.filter(session_id=user).exists()
print(video_user_liste)