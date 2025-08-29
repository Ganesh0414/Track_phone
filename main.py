import phonenumbers
import opencage
import folium
from phonenumbers import geocoder,carrier

number="+919150358522"

pepnumber=phonenumbers.parse(number)
# country location
location = geocoder.description_for_number(pepnumber , "en")
print(carrier.name_for_number(pepnumber, "en")) 

from opencage.geocoder import OpenCageGeocode

key="03f7938012734340b069d50e8a88540b"
geocoder=OpenCageGeocode(key)
query=str(location)
res= geocoder.geocode(query)
# print(res)
lat=res[0]['geometry']['lat']
lng=res[0]['geometry']['lng']
print(lat,lng)
print(location)

myMap=folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("myLocation.html")