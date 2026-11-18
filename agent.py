import os
import threading
import time
from collections import deque

import requests

# Correction 1 : la clé secrète n'est plus dans le code, et l'adresse passe en https
API_URL = "https://api.gml.com/alert"
API_KEY = os.environ.get("GML_API_KEY")

# Correction 2 : la liste est limitée à 3000 mesures (5 minutes)
data_buffer = deque(maxlen=3000)


def envoyer_alerte(val):
    try:
        # Correction 3 : on n'attend jamais le réseau plus de 3 secondes
        requests.post(API_URL, json=val, headers={"Authorization": API_KEY}, timeout=3)
    except requests.RequestException:
        print("Réseau indisponible, alerte non envoyée")


def main_loop(nb_tours=None):
    tour = 0
    while nb_tours is None or tour < nb_tours:
        val = {"x": 12, "y": -3.0}  # Acquisition capteur (simulation)
        data_buffer.append(val)

        if val["y"] < -2.5:
            # Correction 4 : l'alerte part en arrière-plan, la boucle continue
            threading.Thread(target=envoyer_alerte, args=(val,), daemon=True).start()

        time.sleep(0.1)
        tour += 1


if __name__ == "__main__":
    main_loop()