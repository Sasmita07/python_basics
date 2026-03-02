basket = {"apple", "mango", "pineapple", "apple", "orange", "kiwi", "mango"}
print(basket)

a = set()
a.add("apple")
a.add("apple")
a.add("orange")
print(a)

a = {}
print(type(a))
a = {"something"}
print(type(a))

# frozen set
fs = frozenset([1,2,2,4,5,6,6])
print(fs)
# can't modify frozen set
#fs.add(8)
#print(fs)

x = {"a", "b", "c"}
print('a' in x)

for i in x:
    print(i)

y = {"c", "e", "f"}
print(x|y)
print(x&y)
print(x-y)
print(x<y)

# subset
x = {"a", "b", "c", "e", "f"}
print(x>y)
