# Create an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Buddy",
    "color": "Golden",
    "breed": "Golden Retriever",
    "legs": 4,
    "age": 3
}
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Muhammad",
    "last_name": "Huzaifa",
    "gender": "Male",
    "age": 16,
    "marital status": "Single",
    "skills": ["HTML", "CSS", "JS", "Python"],
    "country": "Pakistan",
    "city": "Mianwali",
    "address": "PAF Colony"
}

print(student)
# Get the value of skills and check the data type, it should be a list
print(student["skills"])
# Modify the skills values by adding one or two skills
student["skills"].append("Python")
student["skills"].append("Next.js")
print(student["skills"])
# Get the length of the student dictionary
print(len(student))
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
student.pop("marital status")
print(student)
# Delete one of the dictionaries
del student