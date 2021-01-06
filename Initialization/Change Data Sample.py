import os
import random
import shutil
import json
from Classification.models import Video



# ============= DO NOT USE ANYMORE =================
# This file was only used to reduce the amount of samples
# from 50 to 25 using the random lib. Reexecuting this
# file may break this project
# ==================================================


file_list = os.listdir(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Videos_Selected')
file_list.remove("metadata.json")

file_list_selected = []
for i in range(0, 25):
    num = random.randint(0, len(file_list)-1)
    name = file_list[num]
    shutil.copy("F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Videos_Selected\\" + name,
                "F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Final Video Selection\\" + name)
    file_list.remove(name)
    file_list_selected.append(name)


file = open('F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Filtered Videos\\metadata.json')
metadata = json.load(file)

new_dict = {}

for x in file_list_selected:
    if x in metadata:
        new_dict[x] = metadata.get(x)

with open(
        "F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Final Video Selection\\metadata.json",
        'w') as fp2:
    json.dump(new_dict, fp2)

for x in file_list:
    Video.objects.filter(video_id=x).delete()