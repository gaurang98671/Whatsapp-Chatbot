
import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"eminem"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "17fd2932a3msh3bf2c273aca32f4p183c1bjsncb974202eeed"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)