from os import *
from sys import *
from statistics import *
from math import *
from string import *
from random import *

# Level 1
# Writ a function which generates a six digit/character random_user_id.
def random_user_id():
    id = ""
    for _ in range(6):
        id += choice(ascii_letters + digits)
    return id
print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    number = int(input("Enter the number of IDs to generate: "))
    length = int(input("Enter the length of each ID: "))
    id_list = []
    for _ in range(number):
        id = ""
        for _ in range(length):
            id += choice(ascii_letters + digits)
        id_list.append(id)
    return id_list
for i in user_id_gen_by_user():
    print(i)

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = "rgb({}, {}, {})".format(r,g,b)
    return rgb
# Write a function named hexa_color_gen. It will generate hexadecimal colors (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
def hexa_color_gen():
    hex_characters = "1234567890ABCDEF"
    hexcode = "#"
    for _ in range(6):
        hexcode += choice(hex_characters)
    return hexcode
# Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array.
def list_of_hexa_colors(number_of_colors):
    hex_list = []
    for _ in range(number_of_colors):
        hex_list.append(hexa_color_gen())
    return hex_list

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(number_of_colors):
    rgb_list = []
    for _ in range(number_of_colors):
        rgb_list.append(rgb_color_gen())
    return rgb_list

# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type, number):
    if type == "hexa":
        return list_of_hexa_colors(number)
    elif type == "rgb":
        return list_of_rgb_colors(number)
    else:
        return "Please enter the correct type of color format!"
print(generate_colors("hexa", 3))
print(generate_colors("hexa", 1))
print(generate_colors("rgb", 3))
print(generate_colors("rgb", 1))

# Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
demo_list = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
def shuffle_list(lst):
    shuffle(lst)
    return lst
print(shuffle_list(demo_list))

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def print_random_list():
    lst = []
    while len(lst) < 7:
        number = randint(0, 9)
        if number not in lst:
            lst.append(number)
    return lst
print(print_random_list())