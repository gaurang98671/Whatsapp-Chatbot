import requests

def get_corona_updates(country):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "17fd2932a3msh3bf2c273aca32f4p183c1bjsncb974202eeed"
    }


    response = requests.request("GET", url, headers=headers)

    data=response.json()['response']['country' == country]

    parsed_data=''

    new_cases=data['cases']['new']
    active_cases = data['cases']['critical']
    critical_cases = data['cases']['recovered']
    recoverd_cases=data['cases']['total']
    new_deaths=data['deaths']['new']
    total_deaths=data['deaths']['total']

    parsed_data="New cases : "+str(new_cases)+"\nActive cases : "+str(active_cases)+"\nCritical cases : "+str(critical_cases)+"\nRecovered cases : "+str(recoverd_cases)+"\nNew deaths : "+str(new_deaths)+"\nTotal deaths : "+str(total_deaths)

    return parsed_data

