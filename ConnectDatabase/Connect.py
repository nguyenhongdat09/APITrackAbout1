import pyodbc
import pandas as pd
from Constant.Constant import Constant as ct
import os
class Connect:
    def __init__(self):
        self.connect_string = 'DRIVER={SQL Server};SERVER=' + ct.server + ';DATABASE=' + ct.database_app + ';UID=' + ct.username + ';PWD=' + ct.password
        self.conn = pyodbc.connect(self.connect_string)
        self.cursor = self.conn.cursor()
    def execute_query(self, query):
        query = 'SET NOCOUNT ON; ' + query
        rows = self.cursor.execute(query).fetchall()

        columns = [column[0] for column in self.cursor.description]
        list_df = [pd.DataFrame.from_records(rows, columns=columns)]
        if self.cursor.nextset() == True:
            rows = self.cursor.fetchall()
            df = pd.DataFrame.from_records(rows, columns=[column[0] for column in self.cursor.description])
            list_df.append(df)
        self.cursor.close()
        return list_df
    def list_Xml_Store(self):
        list_df = self.execute_query(ct.Store_check)
        cells = []
        for df in list_df:
            try:
                for cell in df['controller'].values:

                    if self.checkFileXML(cell):
                        cells.append(cell)
            except KeyError as ex:
                continue

        return cells
    def checkFileXML(self, XMLFileName):
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_xml = project_path + '\\XML\\' + XMLFileName + '.XML'
        return os.path.exists(path_xml)
