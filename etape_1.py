import pandas as pd
import folium

# Chemin du fichier stops.txt (à partir du dossier extrait précédemment)
stops_file = "gtfs_extracted/stops.txt"

# Charger les arrêts de bus dans un DataFrame pandas
stops_df = pd.read_csv(stops_file)

# Création d'une carte centrée sur Nantes
nantes_map = folium.Map(location=[47.2184, -1.5536], zoom_start=13)

# Ajout des marqueurs pour chaque arrêt de bus
for _, row in stops_df.iterrows():
    stop_lat = row["stop_lat"]
    stop_lon = row["stop_lon"]
    stop_name = row["stop_name"]
    
    # Ajouter un marqueur pour chaque arrêt de bus
    folium.Marker(
        location=[stop_lat, stop_lon],
        popup=stop_name,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(nantes_map)

# Sauvegarder la carte dans un fichier HTML
nantes_map.save("nantes_bus_stops_map.html")
print("La carte des arrêts de bus a été enregistrée sous 'nantes_bus_stops_map.html'.")
