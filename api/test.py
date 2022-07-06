from geopy.geocoders import Nominatim

address = "Moscow"
geolocator = Nominatim(user_agent="Your_Name")
location = geolocator.geocode(address)
print(location.address)
print((location.latitude, location.longitude))
