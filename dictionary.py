import requests

def get_definition(word):
    definition= word+":"
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term": word}

    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "17fd2932a3msh3bf2c273aca32f4p183c1bjsncb974202eeed"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    for i in response.json()['list'][:3]:
        definition+="\nDefinition:"+i['definition']+"\nExample:"+i['example']

    return definition
