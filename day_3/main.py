age = 16
height = 1.6
complex_number = 1+1j

# Area of triangle
base = int(input("Enter the base of a triangle: "))
height = int(input("Enter the height of a triangle: "))
areaOfTriangle = 0.5*base*height
print("The area of triangle is", areaOfTriangle)

# Perimeter of triangle
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeterOfTriangle = a+b+c
print("The perimeter of triangle is", perimeterOfTriangle)

# area and perimeter of rectangle
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))
areaOfRectangle = length*width
perimeterOfRectangle = 2*(length+width)
print("The area of rectangle is", areaOfRectangle)
print("The perimeter of rectangle is", perimeterOfRectangle)

# area and circumference of circle
radius = int(input("Enter the radius of the circle: "))
areaOfCircle = 3.14*(radius**2)
circumference = 2*3.14*radius
print("The area of circle is", areaOfCircle)
print("The circumference of rectangle is", circumference)

# find the slope and Euclidean distance 
# slope = y2-y1/x2-x1
x = [2,3]
y = [6,10]
slope = (y[1]-y[0]) / (x[1]-x[0])
distance = ((y[0] - x[0])**2 + (y[1] - x[1])**2)**0.5
print("The slope is ",slope)
print("The Euclidean distance is ",distance)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = input("Enter x: ")
y = 2*x-2
print(y)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# by letting x = -3 the value of y will be 0
x = -3
y = x**2 + 6*x + 9
print(y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") != len("dragon"))
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "dragon" and "on" in "python")
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jagron" in "I hope this course is not full of jargon")
# There is no 'on' in both dragon and python
print(not "on" in "dragon" and "on" in "python")
# Find the length of the text python and convert the value to float and convert it to string
print(float(len("Python")))
print(str(float(len("Python"))))
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input("Please enter a number: "))
print("If output is true the number is even else it is odd!")
evenOrOdd = num % 2 == 0
print(evenOrOdd)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 // 3 == int(2.7))
# Check if type of '10' is equal to type of 10
print(type(10) == type("10"))
# Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print("Your weekly earning is", hours * rate)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds ,"seconds.")

# Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)