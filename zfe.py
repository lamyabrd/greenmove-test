import json

with open("data/lyon_polygon.json") as fichier:
    polygone = json.load(fichier)

with open("data/truck_gps.json") as fichier:
    trajet = json.load(fichier)

lat_min = min(p["lat"] for p in polygone)
lat_max = max(p["lat"] for p in polygone)
lon_min = min(p["lon"] for p in polygone)
lon_max = max(p["lon"] for p in polygone)       

for point in trajet:
    lat = point["lat"]
    lon = point["lon"]
    dans_zone = False

    if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
        compteur = 0
        for i in range(len(polygone) - 1):
            A = polygone[i]
            B = polygone[i + 1]
            if (A["lat"] > lat) != (B["lat"] > lat):
                lon_croisement = A["lon"] + (lat - A["lat"]) * (B["lon"] - A["lon"]) / (B["lat"] - A["lat"])
                if lon_croisement > lon:
                    compteur = compteur + 1
        if compteur % 2 == 1:
            dans_zone = True

    if dans_zone:
        print("[ALERT ZFE] Point", point["id"], ": IN")
    else:
        print("Point", point["id"], ": OUT")