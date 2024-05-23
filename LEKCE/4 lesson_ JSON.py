
'''JSON виглядає майже так само, як словники Python. 
Він відрізняється лише тим, що завжди використовує подвійні лапки і 
значення True і False пишеться з малої літери, тобто true a false. '''

# 1 úprava absolventů

import json
from pprint import pprint
# from moje_scf import print_s_hvezdickama

with open('absolventi.json', 'r', encoding='utf-8') as file:
    absolvents = json.load(file)


modified_absolvents = []
for one_absolvent in absolvents:
    one_absolvent['vyznameni'] = False
    one_absolvent['dochazka'] = 0.0
    modified_absolvents.append(one_absolvent)
    

pprint(modified_absolvents)

with open('upraveni_absolventi.json', mode ='w', encoding='utf-8') as out_file:
    json.dump(modified_absolvents, out_file, indent = 4, ensure_ascii=False)

# 2 Zavod

import json
from pprint import pprint

with open('zavod.json', 'r', encoding='utf-8') as file:
    race_data = json.load(file)

# muzu takhle, ale brzy se zamotam do zavorek
print(race_data[0]['casy']['oficialni'])

# nebo si to rozepisu
winner = race_data[0]
race_times = winner['casy']
winning_time = race_times['oficialni']
print(winning_time)

# 3 Stahování dat z internetu

import requests
import json

# mus existovat slozka "restaurants"

restaurants_ids_to_scrape = {97, 54, 35, 36,}

index = 0

while restaurants_ids_to_scrape:
    this_id = restaurants_ids_to_scrape.pop()

    response = requests.get(f'https://gastromapa.hejlik.cz/api/v1/restaurants/{this_id}')

    if response.status_code == 200:
        data = response.json()

        name = data['data']['name'].replace(' ', '_')
        print(f'ukladam restauraci s nazvem {name}')

        with open(f'restaurants/{index}_{name}.json', 'w', encoding='utf-8') as file_out:
            json.dump(data, file_out, indent=4, ensure_ascii=False)

        index += 1
    
    else:
        print(f'restaurace s id {this_id} neexistuje')
    

    
        
        