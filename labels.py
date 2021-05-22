import json

with open('data.json', 'rb') as f:
    rekresp = json.load(f)
#-------------------------------------------------------------------------------------------
resplist = rekresp['Labels']

def match_labels(label):
    labellist = [index['Name'].lower() for index in resplist]
    return label in labellist
