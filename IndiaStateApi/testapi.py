import requests
import json

url = 'http://127.0.0.1:8000/api/states/'
# r = requests.api.get(url)
# result_list = json.loads(r.text)
# for i in result_list:
#     print(i)

data = (
    {
        'name': 'Madhya Pradesh	',
        'capital': 'Bhopal',
        'population': 1000000
    },
    {
        'name': 'Maharashtra',
        'capital': 'Mumbai',
        'population': 1000000
    },
    {
        'name': 'Manipur',
        'capital': 'Imphal',
        'population': 1000000
    },
    {
        'name': 'Meghalaya',
        'capital': 'Shillong',
        'population': 1000000
    },
    {
        'name': 'Mizoram',
        'capital': 'Aizawl',
        'population': 1000000
    },
    {
        'name': 'Nagaland',
        'capital': 'Kohima',
        'population': 1000000
    },
    {
        'name': 'Odisha',
        'capital': 'Bhubaneswar',
        'population': 1000000
    },
    {
        'name': 'Punjab',
        'capital': 'Chandigarh',
        'population': 1000000
    },
    {
        'name': 'Sikkim',
        'capital': 'Gangtok',
        'population': 1000000
    },
    {
        'name': 'Telangana',
        'capital': 'Hyderabad',
        'population': 1000000
    },
    {
        'name': 'West Bengal',
        'capital': 'Kolkata',
        'population': 1000000
    }
)



for i in data:
    data_json = json.dumps(i)
    r = requests.api.post(url, data_json, headers={
        'Content-Type': 'application/json'
    })
    print(r.text)