#id for the api = 9ac2f3f12584eebe9098bd2286e9a598

import requests
from speak import speech
from speak import pyspeak

import time;

def month_get(month):
        if(month==1):
            return 'january'
        if (month == 2):
            return 'february'
        if (month == 3):
            return 'march'
        if (month == 4):
            return 'april'
        if (month == 5):
            return 'may'
        if (month == 6):
            return 'june'
        if (month == 7):
            return 'july'
        if (month == 8):
            return 'august'
        if (month == 9):
            return 'september'
        if (month == 10):
            return 'october'
        if (month == 11):
            return 'november'
        if (month == 12):
            return 'december'

localtime = time.localtime(time.time())
year=int(localtime[0])
month=month_get(int(localtime[1]))
day=int(localtime[2])
hour=str(localtime[3])
mins=str(localtime[4])
#print(date,hour,mins)
api_address='http://api.openweathermap.org/data/2.5/weather?appid=9ac2f3f12584eebe9098bd2286e9a598&q='


def weather_info(loc):
    url = api_address + loc
    json_data = requests.get(url).json()

    print(json_data)
    w_description = json_data['weather'][0]['description']
    
    m_tempmax = str(float(json_data['main']['temp_max'])-273.15)
    m_tempmin = str(float(json_data['main']['temp_min'])-273.15)
    m_humidity = str(json_data['main']['humidity'])
    m_presure = str(json_data['main']['pressure'])
    
    wind_speed = str(json_data['wind']['speed'])
    #wind_dir = str(json_data['wind']['deg'])
    #print('max temp ='+m_tempmax+'min temp='+m_tempmin)
    text = 'hello today is %d %s %d time is '% (day,month,year)
    text2= hour+'hours'+mins+'minutes.'+' todays weather will be' + w_description + ', max temperature will be ' + m_tempmax + 'degree celsius, minimum temperature will be ' + m_tempmin + 'degree celsius,the humidity in air will be ' + m_humidity + 'percentage and wind flowing' + wind_speed + "kilometer per hour"
    texts=text+text2
    #hitext=speech.translation(texts)
    print(texts)
    #speech.speak(texts)
    pyspeak.speakup(texts)

