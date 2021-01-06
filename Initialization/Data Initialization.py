import os
import random
import shutil
import json

# ====================================================
# Nur beim Setup ausführen
# ===================================================


# Erstelle Liste aller Videos im Ordner train_sample_videos ohne die metadata.json
file_list = os.listdir(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Filtered Videos')
file_list.remove("metadata.json")

# Passe metadaten an Video Grundlage an.
file = open(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Filtered Videos\\metadata.json')
metadata_original = json.load(file)

new_dict = {}

for x in file_list:
    if x in metadata_original:
        new_dict[x] = metadata_original.get(x)

# Ersetzte alte Json mit veränderten Einträgen
with open(
        "F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Filtered Videos\\metadata.json",
        'w') as fp2:
    json.dump(new_dict, fp2)

# Es werden 50 Videos zufällig ausgewählt und in eine neue Liste gepackt, alte Liste wird angepasst
file_list_selected = []
for i in range(0, 50):
    num = random.randint(0, len(file_list) - 1)
    name = file_list[num]
    shutil.copy(
        "F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Filtered Videos\\" + name,
        "F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Videos_Selected\\" + name)
    file_list.remove(name)
    file_list_selected.append(name)

# Schaue, welche Videos ausgewählt wurden und füge sie einer neue json Datei hinzu
new_dict = {}
for x in file_list_selected:
    if x in metadata_original:
        new_dict[x] = metadata_original.get(x)

# Speichere die neue Dictionary als JSON unter metadata.json
with open(
        'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Videos_Selected\\metadata.json',
        'w') as fp:
    json.dump(new_dict, fp)
