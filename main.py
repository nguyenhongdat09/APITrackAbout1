from API.API import API
from HandlerJson.JsonToTable import JsonToTable
api = API()
jsons = []
for item in api.get_fill_new():
    jsons.append(item.content.decode(item.encoding))
for json in jsons:
    jtb = JsonToTable(json)
    print(jtb.jsonToDataFrame('rows').to_string(index=False))