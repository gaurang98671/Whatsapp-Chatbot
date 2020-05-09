import requests

def get_weather(city):
    response = requests.get("https://community-open-weather-map.p.rapidapi.com/forecast?q={}".format(city),
                            headers={
                                "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
                                "X-RapidAPI-Key": "17fd2932a3msh3bf2c273aca32f4p183c1bjsncb974202eeed"
                            }
                            )

    cod=response.json()['cod']
    if(cod=='404'):
        return "City not found"
    else:
        return "Temperature:"+str(int(response.json()['list'][0]['main']['temp']-273))+"\nWeather:"+str(response.json()['list'][0]['weather'][0]['description'])+"\nHumidity"+str(response.json()['list'][0]['main']['humidity'])

