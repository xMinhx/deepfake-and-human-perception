import os
import random
import shutil
import json

amount_selected_videos = 50

file = open("F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Videos_Selected\\metadata.json")
metadata_select = json.load(file)

count_manipulated = 0
count_real = 0

for x in metadata_select:
    if metadata_select[x].get("label") == "REAL":
        count_real += 1
    else:
        count_manipulated += 1

if count_real + count_manipulated == amount_selected_videos:
    print("Manipulierte Videos: " + str(count_manipulated) + " - " + str(count_manipulated/amount_selected_videos*100) + "%")
    print("Nicht manipulierte Videos: " + str(count_real) + " - " + str(count_real/amount_selected_videos*100) + "%")
else:
    print("Fehler bei der Initialisierung")


# ===== OUTPUT =====
# Manipulierte Videos: 27 - 54.0%
# Nicht manipulierte Videos: 23 - 46.0%
