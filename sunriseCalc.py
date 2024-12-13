from astral import LocationInfo
from astral.sun import sun
import datetime

def get_sun_times(city_name):
    city = LocationInfo(city_name)
    s = sun(city.observer, date=datetime.date.today())
    return s['sunrise'], s['sunset']

city_name = "London"
sunrise, sunset = get_sun_times(city_name)
print(f"Sunrise: {sunrise}, Sunset: {sunset}")
