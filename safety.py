import csv
import json
import sys

SEUIL = -2.5
evenements = []

fichier_csv = "data/accelerometer_data.csv"
if len(sys.argv) > 1:
    fichier_csv = sys.argv[1]

with open(fichier_csv) as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        try:
            acc_y = float(ligne["acc_y"])
        except (KeyError, TypeError, ValueError):
            print("[ATTENTION] Mesure", ligne.get("timestamp", "?"), ": valeur invalide, ignorée")
            continue
        if acc_y < SEUIL:
            print("[FREINAGE VIOLENT]", ligne["timestamp"], acc_y)
            evenements.append({"timestamp": ligne["timestamp"], "acc_y": acc_y}) 

 
score = 100 - 10 * len(evenements)

resultat = {
    "nb_freinages_violents": len(evenements),
    "evenements": evenements,
    "score": score
}

with open("daily_score.json", "w") as fichier:
    json.dump(resultat, fichier, indent=2)

print("Score du jour :", score)