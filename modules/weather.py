import requests

def get_weather(city):

    API_key = "7edc45d7a71d2d798d8e6510ee7ec1bd"
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={10}&appid={API_key}"
    geo_response = requests.get(geo_url)
    if geo_response.status_code == 200:
        geo_data = geo_response.json()
        if geo_data:
            global lat,lon
            lat = geo_data[0]['lat']
            lon = geo_data[0]['lon']
        else:
            print("geo data not found")
    else:
        print("Geo response not coming")
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
    weather_response = requests.get(weather_url)
    if lat and lon :
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            if weather_data:
                temp = weather_data['main']['temp']
                print("Temprature in ",city," is ",temp)
            else:
                print("weather data not found")
        else:
            print("weather response not coming")
    else:
        print("lat or lon are not found")
