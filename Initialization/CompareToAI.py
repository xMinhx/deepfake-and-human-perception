import json

file = open(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Videos_Selected\\metadata.json')
metadata_dict = json.load(file)

file = open(
    'F:\\H-BRS\\Vorlesungen, Skripts, Notizen, Übungen\\Visual Computing\\Project Deepfake\\Website\\Initialization\\metadata_ai.json')
metadata_ai = json.load(file)

counter_correct = 0
counter_wrong = 0
wrong_label = []

for x in metadata_dict:
    if metadata_ai[x]["label_ai"] == metadata_dict[x]["label"]:
        counter_correct += 1
    else:
        counter_wrong += 1
        wrong_label.append(x)

print("Genauigkeit: " + str(counter_correct / len(metadata_dict)))
print("Falsch klassifiziert: ")
for x in wrong_label:
    print(x + ":")
    print("Guess: " + metadata_ai[x]["label_ai"] + " sollte aber " + metadata_dict[x]["label"] + " sein.")
    print("Guess probability: " + str(metadata_ai[x]["value"] / 100))
    print("=======================================================")

# ============= Output ===========
# Genauigkeit: 0.96
# ================================
# Falsch klassifiziert:
# bbhtdfuqxq.mp4:
# Guess: REAL sollte aber FAKE sein.
# Guess probability: 0.47
# =======================================================
# degpbqvcay.mp4:
# Guess: REAL sollte aber FAKE sein.
# Guess probability: 0.36
# =======================================================

