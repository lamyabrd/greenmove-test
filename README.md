# GreenMove Logistics : du POC à une version robuste

Ce projet reprend le POC du moteur embarqué de la tablette installée dans les camions.
Le pilote sur 50 camions a montré que le code n'était pas adapté au terrain. Cette nouvelle version corrige les causes des crashs pour préparer le déploiement sur les 5 000 camions.

Ce qui est repris du POC

- "zfe.py" : détecte si le camion entre dans la zone à faibles émissions de Lyon
- "safety.py" : repère les freinages violents et calcule un score de conduite
- le dossier "data" : les données de test

Ces deux modules fonctionnaient bien. Ils sont gardés tels quels.

Ce qui est nouveau

Le fichier "agent.py" est la nouvelle version du code de l'Annexe 1, qui a causé les crashs du pilote.

Voici les 4 corrections :
- Correction 1 : la clé secrète n'est plus écrite dans le code, elle est lue dans la configuration de la tablette. L'adresse passe aussi en https.
- Correction 2 : la liste des mesures est limitée à 3000 (5 minutes). Avant, elle grossissait sans fin et saturait la mémoire de la tablette sur un trajet de 8 heures.
- Correction 3 : le programme n'attend jamais le réseau plus de 3 secondes. Avant, il pouvait attendre une minute quand la 4G captait mal. Si le réseau ne répond pas, le programme ne plante pas.
- Correction 4 : les alertes sont envoyées en arrière-plan. La boucle continue de lire les capteurs pendant l'envoi, donc aucun freinage n'est ignoré.

Pour utiliser la nouvelle version, il faut installer l'outil requests en entrant : pip3 install requests

Tests automatiques

Le fichier "test_agent.py" contient 2 tests :
- le premier simule un trajet de 8 heures et vérifie que la mémoire ne dépasse jamais 3000 mesures
- le second vérifie que la boucle lit les capteurs sans être bloquée par le réseau

Afin de lancer les tests, il faut entrer : python3 -m unittest -v

Résultat obtenu : les 2 tests passent (OK).
