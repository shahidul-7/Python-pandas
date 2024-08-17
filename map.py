import folium
import pandas

map = folium.Map(location=[23.810331,90.412521], zoom_start=7, tiles="OpenStreetMap", attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.")

# List of coordinates for the markers (latitude, longitude)
location_data = pandas.read_csv("bd-location.txt")
lat = location_data["LAT"]
lon = location_data["LON"]
name = list(location_data["NAME"])
address = list(location_data["LOCATION"])
elevation = list(location_data["ELEV"])

# HTML template for the popup
html = """
<h4>BD Location Info</h4>
<strong>District:</strong> %s<br>
<strong>Division:</strong> %s<br>
<!-- <strong>Elevation:</strong> %s <br>-->
"""
def marker_color(elevation):
    if elevation < 1000:
        return "red"
    elif 1000 <= elevation <= 2000:
        return "blue"
    elif 2000 <= elevation <= 3000:
        return "green"
    elif 3000 <= elevation <= 4000:
        return "darkpurple"
    elif 4000 <= elevation <= 5000:
        return "orange"
    elif 5000 <= elevation <= 6000:
        return "black"
    elif 6000 <= elevation <= 7000:
        return "darkblue"
    else:
        return "purple"



fg = folium.FeatureGroup(name="My Map")

for lati, longi, nam, addre, elv in zip(lat, lon, name, address, elevation):
    iframe = folium.IFrame(html=html % (nam, addre, elv), width=250, height=100)
    fg.add_child(folium.Marker(
        location=[lati, longi], 
        tooltip="Click to show more",
        popup=folium.Popup(iframe),
        icon=folium.Icon(color=marker_color(elv), icon="info-sign")
        )
    )

#Different Marken with different style
# for lati, longi, nam, addre, elv in zip(lat, lon, name, address, elevation):
#     iframe = folium.IFrame(html=html % (nam, addre, elv), width=250, height=100)
#     fg.add_child(folium.CircleMarker(
#         location=[lati, longi],
#         radius=12,
#         tooltip="Click to show more",
#         popup=folium.Popup(iframe),
#         fill= True,
#         color=marker_color(elv),
#         opacity=0.8,
#         fill_opacity=0.5,
#         icon=folium.Icon(color=marker_color(elv), icon="info-sign"),
#         )
#     )


map.add_child(fg)


#folium.Marker(location=[23.914349, 90.229943], popup="Portland, OR", tooltip="Dhaka Range").add_to(map) #Diffeent way to add to the Map variable
map.save("map2.html")
