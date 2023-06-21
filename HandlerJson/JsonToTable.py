import pandas as pd
import json
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

class JsonToTable:
    def __init__(self, json):
        self.json = json
        self.df = None
    def jsonToDataFrame(self, rootName):
        data = json.loads(self.json)
        self.df = pd.json_normalize(data[rootName])
        return self.df