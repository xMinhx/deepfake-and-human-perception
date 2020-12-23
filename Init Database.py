from Classification.models import Video, Classification
from Start.models import User,Testgroup,Difficulty,Gender,Class

import os
import json

list_videos = os.listdir('F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Filtered Videos')

for x in list_videos:
    video = Video(video_id=x,
                  )