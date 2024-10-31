import requests
import json

# URL de l'API pour obtenir les données
api_url = "https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_tan-arrets-horaires-circuits/records"
params = {"limit": 20}

# Envoyez la requête pour obtenir les données JSON
response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()

    # Obtenez l'URL du fichier depuis les données de la réponse
    file_url = data["results"][0]["fichier"]["url"]

    # Téléchargez le fichier
    file_response = requests.get(file_url)

    # Vérifiez si le téléchargement a réussi
    if file_response.status_code == 200:
        # Enregistrez le fichier localement
        with open("gtfs-tan.zip", "wb") as file:
            file.write(file_response.content)
        print("Le fichier a été téléchargé et enregistré sous 'gtfs-tan.zip'.")
    else:
        print(f"Erreur lors du téléchargement du fichier : {file_response.status_code}")
else:
    print(f"Erreur {response.status_code} lors de l'appel API.")
