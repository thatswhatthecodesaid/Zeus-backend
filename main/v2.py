import requests, json
import time

def Tempc2(city, ac_bool, ac_temp):
    api_key = "5aac8d7e066c9171f11fe957c064b0c6"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x['cod'] != 404:
        y = x['main']
        temp = y['temp']
        print(f"y = {y}")
        avg_temp = (float(y['temp_max']) + float(y['temp_min']))/2
        print(f'avg = {avg_temp}')
        print(f'temp = {temp}')
        if (avg_temp - y['temp']) < 5:
            if ac_bool == True:
                op = "toff"
            elif ac_bool == False:
                op = "off"
        else:
            op = "on"
        return op


def json_convert(h, k):
    x = {}
    x[h] = k
    x = json.dumps(x)
    return x