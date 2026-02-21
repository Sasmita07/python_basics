items = ["apple", "orange", 1]

print(items)
print(items[2])
print(items[0:2])
print(items[-1])

items.append("butter")
print(items)
items = ["apple", "orange", 1]
items.insert(1, "butter")
print(items)

sizeList = ["S", "M", "L"]
clothList = ["Shirt", "Pant", "Top"]
items = sizeList+clothList
print(items)
print(len(items))
print("S" in items)