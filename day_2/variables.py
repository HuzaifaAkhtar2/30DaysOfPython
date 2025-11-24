# Day 2: 30 Days of python programming

# Level 1
firstName = "Muhammad"
LastName = "Huzaifa"
fullName = "Muhammad Huzaifa"
country = "Pakistan"
city = "Mianwali"
age = 16
year = 2025
is_married = False
is_true = True
is_light_on = True
a, b, c, d = 15, 8, 23, 16

# Level 2
print(type(firstName))
print(type(LastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(firstName))
print(len(LastName))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = (22/7)*(radius**2)
circum_of_circle = 2*(22/7)*radius
print("Area of Circle: ", area_of_circle)
print("Circumference of Circle: ", circum_of_circle)

input_radius = int(input("Enter the radius of the circle: "))
area_of_circle = (22/7)*(input_radius**2)
circum_of_circle = 2*(22/7)*input_radius
print("Area of Circle: ", area_of_circle)
print("Circumference of Circle: ", circum_of_circle)

input_firstName = input("Enter your first name: ")
input_lastName = input("Enter your last name: ")
input_country = input("Enter your country name: ")
input_age = int(input("Enter your age: "))

keywords = help("keywords")
print(keywords)