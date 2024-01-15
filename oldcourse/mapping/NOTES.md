## 115. Creating an HTML Map with Python

```python
import folium

# -90 to 90 and -180 to 180
map = folium.Map(location=[80, -100])
map.save("Map1.html")

map= folium.Map(location=[0, 0], zoom_start=6)
map.save("Map1.html")
```