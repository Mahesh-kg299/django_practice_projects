import requests
import json
import base64

url_1 = "http://127.0.0.1:8000/api/companies/?format=json"
url_2 = "http://127.0.0.1:8000/api/companies/1/?format=json"
url_3 = "http://127.0.0.1:8000/api/signup/?format=json"
url_4 = "http://127.0.0.1:8000/api/api-token/?format=json"

company = {
    "c_name": "Boeing",
    "c_founded": "1916-07-15",
    "c_industry": [
        1,
        2
    ],
}

industry = {
    'ind_name': 'Defense'
}

json_data = json.dumps(company)

# r = requests.api.post(url_1, json_data, headers = {
#     "Content-type": 'application/json'
# })

# r = requests.api.put(url_2, json_data, headers = {
#     "Content-type": 'application/json'
# })


# r = requests.api.post(
#     url_4,
#     json.dumps({
#         "username": "akash",
#         "password": "123"
#     }),
#     headers={
#         "Content-type": "application/json"
#     }
# )

# r = requests.api.get(url_1, headers={
#     # "Content-type": "application/json",
#     # "Authorization": "Token 36fb153c5e0a23b21fe1e7df858456a1f59031e3"
#     "Authorization": "Basic YWthc2g6MTIz"
# })

# print(r.text)
dc = base64.b64decode("YWthc2g6MTIz").decode("utf-8")
print(dc)