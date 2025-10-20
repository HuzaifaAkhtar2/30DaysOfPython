# Level 1
# Create an empty tuple
tuple1 = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Ahmed", "Hanzala")
print(brothers)
sisters = ("Zainab", "Lorem Ipsum")
print(sisters)
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Akhtar", "Rahila")
print(parents)
family_members = siblings + parents
print(family_members)

# Level 2
# Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print(siblings)
print(father)
print(mother)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple", "Banana", "Orange", "Mango", "Lemon")
print(fruits)
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
print(vegetables)
animal_products = ("Eggs", "Milk", "Honey", "Meat", "Beef")
print(animal_products)
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[6:9])
# Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[12:15])
# Delete the food_stuff_tp tuple completely
del food_stuff_tp
"""
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country
"""
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries) # False
print("Iceland" in nordic_countries) # True