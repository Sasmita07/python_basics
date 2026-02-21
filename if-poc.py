num = input("Enter a number:")
num = int(num)
if num % 2 == 0:
    print("It's an even number")
else:
    print("It's an odd number")

isValid = 1 > 2 and 3 > 4
print(isValid)
isValid = 1 > 2 or 4 > 3
print(isValid)
isValid = not 6 == 6
print(isValid)

indian = ["chat", "biryani", "soda"]
chinese = ["egg roll", "fried rice", "pot sticker"]
italian = ["pizza", "olives", "pasta"]

dish = input("Enter a dish name: ")
if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("Not from the list")
