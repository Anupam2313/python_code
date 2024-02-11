import json
d={
    'anu':'anupam',
    'ti':'tiwari',
    'roll':1002
}
with open('demo.json','w') as l:
    json.dump(d,l)