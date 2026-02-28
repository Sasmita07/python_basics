# json object

book = {}
book["tom"] = {
    "name": "tom",
    "address": "xyz street 1",
    "phone": 909876
}

book["bob"] = {
    "name": "bob",
    "address": "xyz street 2",
    "phone": 909875
}

import json
result = json.dumps(book);
print(result)

with open("/Users/sas_vsCodeWorkspace/python_basics/file1.txt", "w") as f:
    f.write(result)

f = open("/Users/sas_vsCodeWorkspace/python_basics/file1.txt", "r")
s = f.read()
f.close()
print(s)

parsedata = json.loads(s)
print(parsedata)
print(type(parsedata))
print(parsedata['bob']['phone'])

for person in parsedata:
    print(parsedata[person])