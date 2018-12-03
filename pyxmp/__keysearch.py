import re

def keysearch(namespaced_dict, ns):
    for k in namespaced_dict.keys():
        if re.match(ns+':.+', k):
            yield k
