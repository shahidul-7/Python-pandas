import folium
import pandas

map = folium.Map(location=[34.80018861447608, -108.00101022886365], zoom_start=6, tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.")

# List of coordinates for the markers (latitude, longitude)
location_data = pandas.read_csv("Volcanoes.txt")
lat = location_data["LAT"]
lon = location_data["LON"]
name = list(location_data["NAME"])
address = list(location_data["LOCATION"])
elevation = list(location_data["ELEV"])

# HTML template for the popup
html = """
<h4>Volcano Information</h4>
<strong>Name:</strong> %s<br>
<strong>Location:</strong> %s<br>
<strong>Elevation:</strong> %s <br>
"""
def marker_color(elevation):
    if elevation < 1000:
        return "red"
    elif 1000 <= elevation <= 2000:
        return "blue"
    else:
        return "green"



fg = folium.FeatureGroup(name="My Map")

for lati, longi, nam, addre, elv in zip(lat, lon, name, address, elevation):
    iframe = folium.IFrame(html=html % (nam, addre, elv), width=220, height=120)
    fg.add_child(folium.Marker(
        location=[lati, longi], 
        tooltip="Click to show more",
        popup=folium.Popup(iframe),
        icon=folium.Icon(color=marker_color(elv), icon="info-sign")
        )
    )

map.add_child(fg)


#folium.Marker(location=[23.914349, 90.229943], popup="Portland, OR", tooltip="Dhaka Range").add_to(map)
map.save("map2.html")
