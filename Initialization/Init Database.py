from Classification.models import Video
from Start.models import Testgroup, Difficulty, Gender, Class, Scoreboard
import json

# ============================
# USE ONLY FOR INIT OF DATABASE
# =============================

#Generate difficulty domains
easy = Difficulty(label_id=1, label_name="Easy")
medium = Difficulty(label_id=2, label_name="Medium")
difficult = Difficulty(label_id=3, label_name="Difficult")
easy.save()
medium.save()
difficult.save()

#Generate classification domains
class_real = Class(label_id=1, label_name="Real")
class_fake = Class(label_id=2, label_name="Fake")
class_real.save()
class_fake.save()

#Generate gender domains
male = Gender(label_id=1, label_name="Male")
female = Gender(label_id=2, label_name="Female")
other = Gender(label_id=3, label_name="Other")
male.save()
female.save()
other.save()

#Generate testgroup domains
feedback_group = Testgroup(label_id=1, label_name="Feeback")
no_feedback = Testgroup(label_id=2, label_name="No Feedback")
feedback_group.save()
no_feedback.save()

#Open the metadata of the videos
file = open(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Final Video Selection\\metadata.json')
list_videos = json.load(file)

#Generate an instance of every video.
for x in list_videos:
    tmp_label_id = Class.objects.get(label_id=1)
    if list_videos[x]["label"] == "FAKE":
        tmp_label_id = Class.objects.get(label_id=2)
    video = Video(video_id=x,
                  label=tmp_label_id,
                  gdrive_id=list_videos[x]["GDriveID"][32:65],
                  onedrive_id=list_videos[x]["OneDriveID"])
    video.save()

#Generate scoreboard instance with A.I performance
scoreboard = Scoreboard(id=1,
                        scores={"AI": {"username": "User AI", "correct": 24, "user_score": 2400}})
scoreboard.save()
