if __name__ == "__main__":
    print("I am in special-variable-name.py __name__", __name__)
    print(10*10)

import dummymodules as dm

area = dm.calculate_rectanagle_area(2,3)
print(area)