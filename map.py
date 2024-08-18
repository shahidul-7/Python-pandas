import folium
import pandas

#Create the map
map = folium.Map(location=[23.810331,90.412521], zoom_start=7, tiles="OpenStreetMap", attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.")

# Load the location data
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

# Function to determine marker color based on elevation
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


# Add markers to the map
m_marker = folium.FeatureGroup(name="Map Marker")

for lati, longi, nam, addre, elv in zip(lat, lon, name, address, elevation):
    iframe = folium.IFrame(html=html % (nam, addre, elv), width=250, height=100)
    m_marker.add_child(folium.Marker(
        location=[lati, longi], 
        tooltip="Click to show more",
        popup=folium.Popup(iframe),
        icon=folium.Icon(color=marker_color(elv), icon="info-sign")
        )
    )

# Combine coordinates into a list of tuples
#route = list(zip(lat, lon))
route = [
    (22.701002,90.353451),  # Barishal
    (22.845641,89.540329),  # Khulna
    (24.3636, 88.6241),  # Rajshahi
    (25.7439, 89.2752),  # Rangpur
    (24.747149,90.420273),  # Mymenshing
    (24.894930,91.868706),  # Sylhet
    (23.8103, 90.4125),  # Dhaka
    (22.3569, 91.7832)   # Chittagong
]

# Add a single PolyLine for the entire route
m_line = folium.FeatureGroup("Road on Map")
m_line.add_child(folium.PolyLine(
    locations=route,
    color="green",
    weight=3,
    opacity=0.7,
    tooltip="Route connecting major locations"
))

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
style_function = lambda x: {
    "fillColor": (
        "#red" if x["properties"]["POP2005"] < 10000000
         else "green" if 10000000 <= x["properties"]["POP2005"] <= 20000000 
         else "yellow" if 30000000 <= x["properties"]["POP2005"] <= 40000000
         else "purple" if 40000000 <= x["properties"]["POP2005"] <= 50000000
         else "darkblue" if 50000000 <= x["properties"]["POP2005"] <= 60000000
         else "black" if 70000000 <= x["properties"]["POP2005"] <= 80000000
         else "darkpurple" if 90000000 <= x["properties"]["POP2005"] <= 100000000
         else "orange"
     )
 }
m_population = folium.FeatureGroup("Color by Population")
m_population.add_child(folium.GeoJson(data=open("files/world.json", "r", encoding="utf-8-sig").read(),
             style_function=style_function))

# Add all the feature groups to the map
map.add_child(m_marker)
map.add_child(m_line)
map.add_child(m_population)
map.add_child(folium.LayerControl())


#folium.Marker(location=[23.914349, 90.229943], popup="Portland, OR", tooltip="Dhaka Range").add_to(map) #Diffeent way to add to the Map variable
# Save the map to an HTML file
map.save("map2.html")
