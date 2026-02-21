exp = [2300, 2500, 5600, 7654, 2900]
total = 0

# for loop
for item in exp:
    total +=item
print(total)

# range
for i in range(1, 11):
    print(i)

# len function
for i in range(len(exp)):
    print("Month:",i+1,"Expense:",exp[i])
    total +=exp[i]
print(total)

find_key = "table"
items = ["chair", "table", "tea pot", "wardrobe"]

# break
for i in items:
    if i == find_key:
        print("key is found:", i)
        break
    else:
        print("key is not found:", i)

# continue
for i in range(1, 6):
    if i % 2 == 0:
        continue
    else:
        print("square is:", i * i)

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1