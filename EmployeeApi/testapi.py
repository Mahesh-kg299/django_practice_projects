import requests
import json

url = "http://127.0.0.1:8000/api/employees/?format=json"

emp = json.dumps({
    "e_name": "Radhika Yadav",
    "e_gender": "f",
    "e_salary": 125000,
    "e_dob": "2001-06-22",
    "e_email": "radhikaYd255@gmail.com",
    "e_dprt": 1,
})

# r = requests.api.get(url)
# r = requests.api.post(url, emp, headers={
#     "Content-type": "application/json"
# })
# r = requests.api.put("http://127.0.0.1:8000/api/employees/3/", emp, headers={
#     "Content-type": "application/json"
# })
# print(r.text)
f = open("test.html", "w")
f.write(r.text)
f.close()