from functools import *
# Level 1
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use for loop to print each country in the countries list.
for i in countries:
    print(i)
# Use for to print each name in the names list.
for i in names:
    print(i)
# Use for to print each number in the numbers list.
for i in numbers:
    print(i)

# Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
uppercase_country_names = map(lambda string: string.upper(), countries)
print(list(uppercase_country_names))

# Use map to create a new list by changing each number to its square in the numbers list
squared_list = map(lambda number: number ** 2, numbers)
print(list(squared_list))

# Use map to change each name to uppercase in the names list
uppercase_names = map(lambda string: string.upper(), countries)
print(list(uppercase_names))

# Use filter to filter out countries containing "land".
country_land = filter(lambda string: 'land' in string, countries)
print(list(country_land))

# Use filter to filter out countries having exactly six characters.
country_six = filter(lambda string: len(string) == 6, countries)
print(list(country_six))

# Use filter to filter out countries containing six letters and more in the country list.
country_six_or_more = filter(lambda string: len(string) >= 6, countries)
print(list(country_six_or_more))

# Use filter to filter out countries starting with an "E"
country_with_e = filter(lambda string: string.startswith("E"), countries)
print(list(country_with_e))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
chained_function_lst = reduce(lambda x, y: x + y, filter(lambda number: number >= 1, map(lambda number: number**2, numbers)))
print(chained_function_lst)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return list(filter(lambda string: type(string) == str, lst)) 
print(get_string_lists(numbers))
print(get_string_lists(names))

# Use reduce to sum all the numbers in the numbers list.
summation = reduce(lambda x, y: x + y, numbers)
print(summation)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
all_countries = reduce(lambda x, y: x + ", " + y if y != countries[-1] else x + ", and " + y, countries) + " are north European countries"
print(all_countries)

countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central African Republic","Chad","Chile","China","Colombi","Comoros","Congo (Brazzaville)","Congo","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor (Timor Timur)","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia, The","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea, North","Korea, South","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia and Montenegro","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"];

# Declare a function called categorize_countries that returns a list of countries with some common pattern (eg "land", "ia", "island", "stan")
def categorize_countries(pattern):
    pattern = pattern.lower()
    return list(filter(lambda country: pattern in country.lower(), countries))
print(categorize_countries("ia"))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def letter_count(lst):
    dictionary = {}
    for i in lst:
        letter = i[0]
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary
print(letter_count(countries))

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries list.
def get_first_ten_countries(lst):
    return list(map(lambda x: x, lst[:10]))
print(get_first_ten_countries(countries))

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(lst):
    return list(map(lambda x: x, lst[-10:]))
print(get_last_ten_countries(countries))