import folium

map = folium.Map(location=[23.914349, 90.229943], zoom_start=17, tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.")

# List of coordinates for the markers (latitude, longitude)
locations = [
    [23.916030, 90.226487],
    [23.914349, 90.229943],
    [23.913620, 90.230415],
    [23.912843, 90.231070],
    [23.914500, 90.228200]
]
for location in locations:
    folium.Marker(location=location, 
                  tooltip="Click to show more",
                  popup="Marker at{}".format(location),
                  icon=folium.Icon(color="green", icon="info-sign")).add_to(map)

#folium.Marker(location=[23.914349, 90.229943], popup="Portland, OR", tooltip="Dhaka Range").add_to(map)
map.save("map2.html")