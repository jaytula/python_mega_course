import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

df = pandas.read_csv('Volcanoes_USA.txt')

lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])


# Adding some markers
map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

# Using Feature Groups
fg = folium.FeatureGroup(name="My Map")

coordinates = [
  [37.2, -93.1],
  [36.2, -94.1],
  [39.8, -92.3],
  [40, -90]
]

for lt, ln, el in zip(lat, lon, elev):
  fg.add_child(folium.Marker(location=[lt, ln], popup=f"{el} m", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")