x = input('Enter number1:')
y = input('Enter number2:')
try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print("Zero Division Error occured:", e)
    z = None
except TypeError as e:
    print("Type Error:", e)
    z = None
except Exception as e:
    print("Exception type:", type(e).__name__)
    z = None
print("Division is: ", z)