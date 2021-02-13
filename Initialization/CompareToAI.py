import json

#Open the metadata of the original and the A.I based evaluation
file = open(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Videos_Selected\\metadata.json')
metadata_dict = json.load(file)

file = open(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Website\\Initialization\\metadata_ai.json')
metadata_ai = json.load(file)


counter_correct = 0
counter_wrong = 0
wrong_label = []

#Check of values provided by the A.I are the same as the video label
#Count wrong and correct answers
for x in metadata_dict:
    if metadata_ai[x]["label_ai"] == metadata_dict[x]["label"]:
        counter_correct += 1
    else:
        counter_wrong += 1
        wrong_label.append(x)

print("Sample of 50 Videos")
print("Genauigkeit: " + str(counter_correct / len(metadata_dict)))
print("================[Falsch klassifiziert]=================")
for x in wrong_label:
    print(x + ":")
    print("Guess: " + metadata_ai[x]["label_ai"] + " sollte aber " + metadata_dict[x]["label"] + " sein.")
    print("Guess probability: " + str(metadata_ai[x]["value"] / 100))
    print("=======================================================")

# ======== OUTPUT ===============
# Sample of 50 Videos
# Genauigkeit: 0.96
# ================[Falsch klassifiziert]=================
# bbhtdfuqxq.mp4:
# Guess: REAL sollte aber FAKE sein.
# Guess probability: 0.47
# =======================================================
# degpbqvcay.mp4:
# Guess: REAL sollte aber FAKE sein.
# Guess probability: 0.36
# =======================================================


#Same as above with the new iteration of 25 videos
file = open(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Final Video Selection\\metadata.json')
metadata_dict_25 = json.load(file)

counter_correct = 0
counter_wrong = 0
wrong_label = []

for x in metadata_dict_25:
    if metadata_ai[x]["label_ai"] == metadata_dict_25[x]["label"]:
        counter_correct += 1
    else:
        counter_wrong += 1
        wrong_label.append(x)

print("\n===============[Sample of 25 Videos:]===================")
print("Genauigkeit: " + str(counter_correct / len(metadata_dict_25)))
print("===============[Falsch klassifiziert:]================== ")
for x in wrong_label:
    print(x + ":")
    print("Guess: " + metadata_ai[x]["label_ai"] + " sollte aber " + metadata_dict_25[x]["label"] + " sein.")
    print("Guess probability: " + str(metadata_ai[x]["value"] / 100))
    print("=======================================================")

# ========= OUTPUT =============
# ===============[Sample of 25 Videos:]===================
# Genauigkeit: 0.96
# ===============[Falsch klassifiziert:]==================
# degpbqvcay.mp4:
# Guess: REAL sollte aber FAKE sein.
# Guess probability: 0.36
# =======================================================
