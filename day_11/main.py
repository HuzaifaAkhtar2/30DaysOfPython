# Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_number(a,b):
    sum = a + b
    return sum
print(add_two_number(5,8))
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 22/7
    area = pi * r ** 2
    return area
print(area_of_circle(7))
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the lst items are number types. If not do give a reasonable feedback.
def sum_all(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum
print(sum_all(12,23,34,45))
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(temp):
    f = (temp * 9/5) + 32
    return f
print(convert_celsius_to_fahrenheit(0))
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month == "January" or month == "February" or month == "December":
        return "Winter"
    if month == "March" or month == "April" or month == "May":
        return "Spring"
    if month == "June" or month == "July" or month == "August":
        return "Summer"
    if month == "September" or month == "October" or month == "November":
        return "Autumn"
print(check_season("January"))
# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,y1,x2,y2):
    m = (y2-y1) / (x2-x1)
    return m
print(calculate_slope(8,6,7,9))
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_equation(a,b,c):
    print("Equation is {}x2 + {}x + {}".format(a,b,c))
    s1 = (-b + (b**2 - 4*a*c)**0.5) / 2 * a
    s2 = (-b - (b**2 - 4*a*c)**0.5) / 2 * a
    return "And the solutions of the equation are {} and {}".format(s1, s2)
print(solve_quadratic_equation(1,-2,1))
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)
print(print_list([6,5,3,6,73,2]))
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    lst.reverse()
    return lst
print(reverse_list(["A", "B", "C"]))
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized_lst = []
    for i in lst:
        letter = i.capitalize()
        capitalized_lst.append(letter)
    return capitalized_lst
print(capitalize_list_items(["lorem", "ipsum", "dolor"]))
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst
food_stuff = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_stuff, "Meat"))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
        return lst
    else:
        return "Please Enter a valid item check if there aren't any typos"
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num_range):
    sum = 0
    for i in range(num_range + 1):
        sum += i
    return sum
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num_range):
    sum = 0
    for i in range(num_range + 1):
        if i % 2 == 1:
            sum += i
    return sum
print(sum_of_odds(100))
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(num_range):
    sum = 0
    for i in range(num_range + 1):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_evens(100))
# Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num_range):
    num_of_odds = 0
    num_of_evens = 0
    for i in range(num_range + 1):
        if i % 2 == 0:
            num_of_evens += 1
        else:
            num_of_odds += 1
    return "The number of odds are {}.\nThe number of evens are {}.".format(num_of_odds, num_of_evens)
print(evens_and_odds(100))
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    factor = 1
    for i in range(1, number + 1):
        factor *= i
    return factor
print(factorial(10))
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    if type(value) == str:
        return value == ""
    else:
        return not len(value) > 0
print(is_empty([21]))
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviartion).
demo_lst = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
def calculate_mean(lst):
    mean = sum(lst) / len(lst)
    return mean
print(calculate_mean(demo_lst))
def calculate_median(lst):
    if len(lst) % 2 == 0:
        median = (lst[(len(lst) - 1) // 2] + lst[len(lst) // 2]) / 2
    else:
        median = lst[len(lst) // 2]
    return median
print(calculate_median(demo_lst))
def calculate_mode(lst):
    lst_set = set(lst)
    mode = 0
    largest_count = 0
    for i in lst_set:
        count = lst.count(i)
        if count > largest_count:
            largest_count = count
            mode = i
    return mode
print(calculate_mode(demo_lst))
def calculate_variance(lst):
    mean = calculate_mean(lst)
    s_variance = 0
    for i in lst:
        s_variance += (mean - i) ** 2
    variance = s_variance / len(lst)
    return s_variance
print(calculate_variance(demo_lst))
def calculate_std(lst):
    variance = calculate_variance(lst)
    std = variance ** 0.5
    return std
print(calculate_std(demo_lst))
def calculate_range(lst):
    lst.sort()
    min = lst[0]
    max = lst[len(lst) - 1]
    range = max - min
    return range
print(calculate_range(demo_lst))
# Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    if num > 1:
        divisor = int(num**0.5)
        for i in range(2, divisor):
            if num % i == 0:
                return False
            else:
                return True
print(is_prime(11))
# Write a functions which checks if all items are unique in the lst.
def are_unique(lst):
    if len(lst) == len(set(lst)):
        return True
    else:
        return False
print(are_unique(demo_lst))
# Write a function which checks if all the items of the lst are of the same data type.
def are_sameDataType(lst):
    for i in lst:
        if type(lst[0]) == type(i):
            value = True
        else:
            return False
    return value
print(are_sameDataType(demo_lst))
# Write a function which check if provided variable is a valid python variable
def is_valid_variable(name):
    if not type(name) == str:
        return False
    if not name.isidentifier():
        return False
    return True
print(is_valid_variable("name"))