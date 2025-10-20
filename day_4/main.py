str1 = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
str2 = 'Coding ' + 'For ' + 'All'
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.index("Coding"))
print(company.replace("Coding", "Python"))
str3 = "Python for Everyone"
print(str3.replace("Everyone", "All"))
print(company.split( ))
print(company[0])
print(len(company)-1)
print(company[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
str4 = "Python For Everyone"
word11, word12, word13 = str4.split( )
print(word11[0] + word12[0] + word13[0])
# Create an acronym or an abbreviation for the name 'Coding For All'.
word21, word22, word23 = company.split( )
print(word21[0] + word22[0] + word23[0])

str5 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str5.split(", "))
print(company.index("C"))
print(company.index("F"))
str6 = "Coding For All People"
print(str6.rfind("l"))
str7 = "You cannot end a sentence with because because because is a conjunction"
print(str7.index("because"))
print(str7.rindex("because"))
print(company.startswith("Coding"))
print(company.endswith("coding"))
str8 = "   Coding For All      "
print(str8.strip(" "))
"""
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python  <== (This One)
"""
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
pythonLibs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry \tCity\nHuzaifa\t16\tPakistan\tMianwali")

r = 10
a = 3.14 * r ** 2
print("The area of a circle with radius {} is {} meters square.".format(r, a))
# The area of a circle with radius 10 is 314 meters square.
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""
x = 8
y = 6
print('{} + {} = {}'.format(x, y, x + y))
print('{} - {} = {}'.format(x, y, x - y))
print('{} * {} = {}'.format(x, y, x * y))
print('{} / {} = {}'.format(x, y, x / y))
print('{} % {} = {}'.format(x, y, x % y))
print('{} // {} = {}'.format(x, y, y // y))
print('{} ** {} = {}'.format(x, y, x ** y))