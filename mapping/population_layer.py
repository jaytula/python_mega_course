from branca.element import IFrame
import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

df = pandas.read_csv('Volcanoes_USA.txt')

lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

def color_producer(elevation: float):
  if elevation < 1000:
    return 'green'
  elif elevation < 3000:
    return 'orange'
  else:
    return 'red'

html = """<h4>Volcano inofrmation:</h4>
Height: %s m"""

# Adding some markers
map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

# Using Feature Groups
fgv = folium.FeatureGroup(name="Volanoes")

coordinates = [
  [37.2, -93.1],
  [36.2, -94.1],
  [39.8, -92.3],
  [40, -90]
]

for lt, ln, el in zip(lat, lon, elev):
  iframe = folium.IFrame(html=html % str(el), width=200, height=100)
  # Lecture 126 lacks explanation of how to discover the kwargs
  # Ultimately a successful search should lead to https://python-visualization.github.io/folium/modules.html#folium.vector_layers.path_options
  fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, color="grey", popup=folium.Popup(iframe), fill_color=color_producer(el), fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
  style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if x['properties']['POP2005'] < 20000000 else 'red'}
))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")