import os
import json

# =========== DO NOT USE ANYMORE ===================
# This File was only used, to assign the retrieved values
# to it's respective video. The result can be found in
# metadata_ai.json
# ==================================================

videos = os.listdir(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Videos_Selected')
videos.remove("metadata.json")

checked_videos = ["REAL", "FAKE", "REAL", "FAKE", "FAKE", "FAKE", "FAKE",
                  "FAKE", "FAKE", "FAKE", "FAKE", "FAKE", "REAL", "FAKE",
                  "REAL", "FAKE", "REAL", "REAL", "REAL", "REAL", "REAL",
                  "FAKE", "FAKE", "REAL", "FAKE", "FAKE", "FAKE", "FAKE",
                  "REAL", "FAKE", "FAKE", "REAL", "REAL", "REAL", "REAL",
                  "FAKE", "FAKE", "REAL", "REAL", "FAKE", "REAL", "REAL",
                  "REAL", "FAKE", "REAL", "FAKE", "REAL", "REAL", "REAL",
                  "REAL"]
checked_values = [3, 97, 0, 99, 99, 97, 99,
                  97, 99, 100, 99, 100, 1, 84,
                  47, 98, 1, 0, 3, 0, 22,
                  97, 99, 5, 99, 99, 99, 55,
                  9, 98, 99, 4, 0, 21, 24,
                  100, 100, 0, 36, 99, 0, 0,
                  4, 93, 0, 99, 5, 2, 2,
                  2]

new_dict = {}
counter = 0
for x in videos:
    new_dict.update({x: {"label_ai": checked_videos[counter],
                         "value": checked_values[counter]}})
    counter += 1

with open(
        'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Website\\Initialization\\metadata_ai.json',
        'w') as fp:
    json.dump(new_dict, fp)
