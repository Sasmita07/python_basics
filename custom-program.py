import dummymodules as dm

area = dm.calculate_rectanagle_area(2,3)
print(area)
area = dm.calculate_square_area(5)
print(area)

import submodule.subdummod as sdm

area = sdm.calculate_triangle_area(2,3)
print(area)

# To read a file from system path
# import sys
# sys.path.append()