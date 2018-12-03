import xml.etree.ElementTree as ET
from .__keysearch import keysearch
from .__attribute import Attribute

class XMP(object):
    def __init__(self, filepath, **namespaces):
        self.filepath = filepath
        with open(self.filepath, 'rb') as f:
            data = f.read()
        xmp_start = data.find(b'<x:xmpmeta')
        xmp_end = data.find(b'</x:xmpmeta')
        self.__namespaces = namespaces
        self.__xmp_string = data[xmp_start:xmp_end+12]
        try:
            self.__root = ET.fromstring(self.__xmp_string)
            self.__rdf_el = self.__root[0][0]
            self.__attrib_dict = self.__rdf_el.attrib
        except ET.ParseError:
            self.__attrib_dict = {}
        self.__namespaced_dict = {}
        self.__update_namespaced_dict()
        self.__create_namespace_attributes()

    def __update_namespaced_dict(self):
        for k, v in self.__attrib_dict.items():
            nk = k
            for ns, url in self.__namespaces.items():
                nk = k.replace('{'+ url +'}', ns+':')
                if k != nk:
                    break
            self.__namespaced_dict[nk] = v
            
    def __create_namespace_attributes(self):
        for k in self.__namespaces.keys():
            setattr(self, k, Attribute())
            obj = getattr(self, k)
            for key in keysearch(self.__namespaced_dict, k):
                attr_name = key.replace(k+':', '')
                setattr(obj, attr_name, self.__namespaced_dict[key])
