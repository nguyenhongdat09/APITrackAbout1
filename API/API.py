from ConnectDatabase.Connect import Connect as cn
from XMLParse.XMLParse import XMLParse as xmlp
from Constant.Constant import Constant as ct
import requests


class API:
    def __init__(self):
        self.json = None
        self.connection = cn()
        self.xml_parse = xmlp()

    def get_fill_new(self):
        url, responses, params = [], [], []

        for items in self.xml_parse.set_xml_to_json().items():
            if items[0] == 'controller_info':
                for request_link in items[1]:
                    url.append(f"{ct.ApiLink}{request_link}")
            if items[0] == 'parameter_info':
                params = items[1]
        if not url:
            return requests.Response()
        for i in range(len(url)):
            response = requests.get(url[i], params=params[i], headers=ct.headers)
            responses.append(response)
        return responses


# api = API()
# for item in api.get_fill_new():
#     print(item.content.decode(item.encoding))
