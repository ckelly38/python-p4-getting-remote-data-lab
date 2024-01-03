import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        res = requests.get(self.url);
        return res.content;

    def load_json(self):
        return json.loads(self.get_response_body());

#get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
#print(get_requester.load_json());
