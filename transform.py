import zipfile
import os

# Chemin vers le fichier ZIP téléchargé
zip_file_path = "gtfs-tan.zip"

# Dossier de destination pour l'extraction
extract_folder = "gtfs_extracted"

# Assurez-vous que le fichier ZIP existe avant de le manipuler
if os.path.exists(zip_file_path):
    # Ouvrez le fichier ZIP
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Liste des fichiers dans le ZIP
        print("Fichiers dans l'archive ZIP:")
        for file in zip_ref.namelist():
            print(file)

        # Extraction de tous les fichiers
        zip_ref.extractall(extract_folder)
        print(f"Les fichiers ont été extraits dans le dossier '{extract_folder}'.")

        # Lecture d'un fichier spécifique (par exemple "stops.txt") s'il existe
        if "stops.txt" in zip_ref.namelist():
            with zip_ref.open("stops.txt") as file:
                content = file.read().decode('utf-8')  # Décodez en UTF-8
                print("\nContenu de stops.txt :")
                print(content[:500])  # Affiche les 500 premiers caractères
        else:
            print("Le fichier 'stops.txt' n'est pas présent dans l'archive ZIP.")
else:
    print(f"Le fichier {zip_file_path} n'existe pas.")
