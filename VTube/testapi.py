import requests
import json

class ApiTester(object):
    def __init__(self, url_1 = None, url_2 = None, url_3 = None, url_4 = None, token = None):
        self.list_url = url_1
        self.detail_url = url_2
        self.register_url = url_3
        self.login_url = url_4
        self.token = token
    
    def post(self, data):
        json_data = json.dumps(data)
        if self.token:
            r = requests.api.post(self.list_url, json_data, headers = {
                "Content-type": "application/json",
                "Authorization": "Token " + self.token
            })
            return r.text

        r = requests.api.post(self.list_url, json_data, headers = {
            "Content-type": "application/json"
        })
        return r.text

    def put(self, data):
        json_data = json.dumps(data)
        r = requests.api.put(self.detail_url, json_data, headers = {
            "Content-type": "application/json"
        })
        return r.text
    
    def delete(self):
        r = requests.api.delete(self.detail_url)
        return r.text


# testerVideo = ApiTester('http://127.0.0.1:8000/api/videos/?format=json', 'http://127.0.0.1:8000/api/videos/<pk>/?format=json')

# result = testerVideo.post({
#     "vid_title":"Don.t be Teared",
#     "vid_publish_date":"2013-05-5",
#     "vid_views":123000,
# })

# testerUser = ApiTester('http://127.0.0.1:8000/api/users/?format=json', 'http://127.0.0.1:8000/api/users/<pk>/?format=json', token = "09e240bb485a23efb3b21129b223597eb488872a")

# result = testerUser.post({
#     "usr_username":"Arushi99",
#     "usr_password":"arsh#@#991",
#     "usr_email":'arushi991@gmail.com',
# })

# testerComment = ApiTester('http://127.0.0.1:8000/api/comments/?format=json', 'http://127.0.0.1:8000/api/comments/<pk>/?format=json')

# result = testerComment.post({
#     "cmt_text":"Fun to watch",
#     "cmt_vid_id":2,
#     "cmt_usr_id":2,
# })

# tester = ApiTester('http://127.0.0.1:8000/api/register/?format=json')
# result = tester.post({
#     'username': 'mahesh',
#     'password': '12345'
# })

# tester = ApiTester('http://127.0.0.1:8000/api/authtoken/?format=json')
# result = tester.post({
#     'username': 'mahesh',
#     'password': '12345'
# })

# print(result)
token = '09e240bb485a23efb3b21129b223597eb488872a'