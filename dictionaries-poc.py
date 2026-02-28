d = {"x": 123, "y": 456, "z": 789}
print(d)

# fetch using key
print(d["y"])

# delete the key
del d["x"]
print(d)

# iterate over the dictionary
for key in d:
    print("key:", key, "value:", d[key])

# tuples
for k,v in d.items():
    print("key:", k, "value:", v)

print("x" in d)

# clear the dictionary
d.clear()
print(d)