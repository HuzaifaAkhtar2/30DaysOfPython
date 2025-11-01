# Level 1

"""
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""
input1 = int(input("Enter your age: "))
print("You are old enough to learn to drive") if input1 >= 18 else print("You need ", 18 - input1 ,"more years to learn to drive.")

"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
Enter your age: 30
You are 5 years older than me.
"""
my_age = 16
print("My age is 16, what's yours?")
your_age = int(input("Enter your age: "))
if your_age > my_age:
    print("You are", your_age - my_age ," year(s) older than me")
elif your_age < my_age:
    print("You are", my_age - your_age, " year(s) younger than me")
else:
    print("We both have the same age!")

"""
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print(a, "is equal to", b)

# Level 2
"""
Write a code which gives grade to students according to theirs scores:
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""

marks = int(input("Enter your marks: "))
if marks <= 100 and marks > 79:
    print("Your grade is A")
elif marks <= 79 and marks > 69:
    print("Your grade is B")
elif marks <= 69 and marks > 59:
    print("Your grade is C")
elif marks <= 59 and marks > 49:
    print("Your grade is D")
else:
    print("Your grade is F")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = int(input("Enter the current month number: "))
if month == 1 or month == 2 or month == 12:
    weather = "Winter"
    print("The current season is", weather)
elif month == 3 or month == 4 or month == 5:
    weather = "Spring"
    print("The current season is", weather)
elif month == 6 or month == 7 or month == 8:
    weather = "Summer"
    print("The current season is", weather)
elif month == 9 or month == 10 or month == 11:
    weather = "Autumn"
    print("The current season is", weather)
else:
    print("Please enter a number between 1 to 12! There are 12 months in a year")

"""
The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_list = input("Enter a fruit: ")
if fruit_list in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit_list)
    print(fruits)

# Level 3

print("Enter 5 skills. Make sure that there are no typos and first alphabet is capital.")
skill1 = input("Enter your first skill: ")
skill2 = input("Enter your second skill: ")
skill3 = input("Enter your third skill: ")
skill4 = input("Enter your fourth skill: ")
skill5 = input("Enter your fifth skill: ")

# Here we have a person dictionary. Feel free to modify it!
person = {
"first_name": "Muhammad",
"last_name": "Huzaifa",
"age": 16,
"country": "Pakistan",
"is_married": False,
"skills": [skill1, skill2, skill3, skill4, skill5],
"address": "PAF Colony, Mianwali"
}

skills = person["skills"]
if "skills" in person:
    print(skills)
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
    print(skills[len(skills) // 2])
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    print("True") if "Python" in person["skills"] else print("False")
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
    if "JavaScript" in skills or "React" in skills:
        print("You're a front-end developer")
    elif "Node" in skills or "Python" in skills or "MongoDB" in skills:
        print("You're a back-end developer")
    elif "React" in skills and "Node" in skills or "MongoDB" in skills:
        print("You're a full-stack developer")
    else:
        print("unknown title")
else:
    print("You don't have any skills!")
"""
If the person is married and if he lives in Finland, print the information in the following format:
Asabeneh Yetayeh lives in Finland. He is married.
"""
if "country" in person and "is_married" in person:
    print("{} {} lives in {}. He is married".format(person["first_name"], person["last_name"], person["country"])) if person["is_married"] == True else print("{} {} lives in {}. He is not married".format(person["first_name"], person["last_name"], person["country"]))
