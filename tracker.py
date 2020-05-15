import requests
import pandas as pd
from bs4 import BeautifulSoup 
from prettytable import PrettyTable

def tracker():
    url = 'https://www.mohfw.gov.in/'

    web_content = requests.get(url).content
    
    soup = BeautifulSoup(web_content, "html.parser")
    
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    
    stats = [] 
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_contents(row.find_all('td')) 
    
        if len(stat) == 5:
            stats.append(stat)
    
    new_cols = ["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]
    state_data = pd.DataFrame(data = stats, columns = new_cols)
    
    state_data['Confirmed'] = state_data['Confirmed'].map(int)
    state_data['Recovered'] = state_data['Recovered'].map(int)
    state_data['Deceased'] = state_data['Deceased'].map(int)
    
    table = PrettyTable()
    table.field_names = (new_cols)

    for i in stats:
        table.add_row(i)
    
    print(table)    

if __name__ == '__main__':
    print(tracker())
