# List Comprehensions
numbers = [1,2,3,4,5,6,7,8,9]

even_num = [i for i in numbers if i % 2 == 0]
print(even_num)

square_num = [i*i for i in numbers]
print(square_num)

# Set Comprehensions
s = set([1,2,2,3,4,5,6,7,7,8,9])

even_num_set = {i for i in numbers if i % 2 == 0}
print(even_num_set)

# Map Comprehensions
cities = ["Mumbai", "Amsterdam", "London"]
countries = ["India", "Netherlands", "United Kingdom"]

z = zip(cities, countries)
d = {city:country for city, country in z}
print(d)