from Constant.Constant import Constant as ct
import pandas as pd
from ConnectDatabase.Connect import Connect as cn
import os
import sys
import xml.etree.ElementTree as ET

import json


class XMLParse:
    def __init__(self):
        self.xml_to_json = {}
        self.connection = cn()
        self.list_xml = self.connection.list_Xml_Store()

    def getXMLParse(self, XMLFileName):
        # Lấy đường dẫn tuyệt đối của tệp đang thực thi
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_xml = project_path + '\\XML\\' + XMLFileName + '.XML'
        tree = ET.parse(path_xml)
        root = tree.getroot()
        return root

    def tableInfo_Xml(self):
        dataframes = []
        dataframes_xml = []
        for xml in self.list_xml:
            xmlRootContent = self.getXMLParse(xml)
            tables = xmlRootContent.findall('.//ns:tables/ns:table', ct.namespace)
            for table in tables:
                table_name = table.attrib['name']
                fields = table.findall('ns:field', ct.namespace)
                data = []
                for field in fields:
                    record = {'pathJson': field.attrib['pathJson'], 'fastName': field.attrib['fastName'],
                              'typesql': field.attrib['typesql'], 'table_name': table_name}
                    data.append(record)
                dataframes.append(pd.DataFrame(data))
            dataframes_xml.append(dataframes)
        return dataframes_xml

    def Controller_info(self):
        controllerInfo = []
        for xml in self.list_xml:
            xmlRootContent = self.getXMLParse(xml )
            tables = xmlRootContent.findall('.//ns:tables', ct.namespace)
            for table in tables:
                controllerInfo.append(table.attrib['controllerInfo'])
        return controllerInfo

    def Parameters_XML(self):
        data = []
        for xml in self.list_xml:
            xmlRootContent = self.getXMLParse(xml)
            tables = xmlRootContent.findall('.//ns:tables/ns:paramerters', ct.namespace)
            for paramerters in tables:
                prs = paramerters.findall('ns:partameter', ct.namespace)
                record = {}
                for parameter in prs:
                    record[parameter.attrib['Key']] = parameter.attrib['Value']
                data.append(record)
        return data

    def set_xml_to_json(self):
        xmlInfo = []
        for xml in self.list_xml:
            xmlInfo.append(xml)

        self.xml_to_json['xml_info'] = xmlInfo
        self.xml_to_json['controller_info'] = self.Controller_info()
        self.xml_to_json['table_info'] = self.tableInfo_Xml()
        self.xml_to_json['parameter_info'] = self.Parameters_XML()
        return self.xml_to_json
