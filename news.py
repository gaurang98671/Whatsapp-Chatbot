import requests
#21f1e0290080452784b4ffeb9869f130

def news():
    message=''
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=21f1e0290080452784b4ffeb9869f130')
    response = requests.get(url)
    json_response=response.json()
    for i in json_response['articles'][:5]:
        message+='\n'+i['title']
        #message+='\n'+i['description']
        message+='\n'+i['url']
    return message

