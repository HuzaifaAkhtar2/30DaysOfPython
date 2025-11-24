# Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Lenovo", "Nvidia", "Ryzen"])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)

"""
What is the difference between remove and discard?
In Python, remove means to get of one or multiple item(s) in sets, lists, or tuples. However discard means to get rid of it completely using the del operator
"""

# Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Join A and B
print(A.union(B))
# Find A intersection B
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Join A with B and B with A
A.update(B)
print(A)
B.update(A)
print(B)
# Delete the sets completely
del A
del B

# Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(age))
print(age)
age_set = set(age)
print(len(age_set))
print(age_set)

"""
Explain the difference between the following data types: string, list, tuple and set
String: It is plain text surrounded by quotations single '' or double "" or triple '''. It consists of characters i.e. numbers, alphabets, symbols etc.

List: It consist of diffrent data types and a group or collection of data. It is written in square brackets []. Every item has it's index.

Tuples: Tuples serve the same purpose as lists but unlike lists they can't be changed and are immutable. They are written within parenthisis ()

Sets: Sets are similar to lists but they have unique elements in it. If a number 21 is inside a set you can't add another number 21 cause Sets consist of unique elements or items. They are written within braces {}
"""

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
sentence_list = sentence.split()
sentence_set = set(sentence_list)
print(sentence_set)
print(len(sentence_set))