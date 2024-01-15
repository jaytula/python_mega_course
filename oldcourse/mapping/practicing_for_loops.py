import folium

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

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

for coordinate in coordinates:
  fg.add_child(folium.Marker(location=coordinate, popup="Hi I am a Marker from Feature Group", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")