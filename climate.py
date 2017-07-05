import requests

api_key = "f008574df2dfaee547da4e4dd339685f"

def check_for_tempereture(city_qry):
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city_qry+"&appid="+api_key)
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = temp_k - 273.15
    weather_list = json_object['weather']
    return temp_c,weather_list[0]['description']


