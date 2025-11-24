from statistics import *
from collections import *

# Level 1
# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class.
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
    def __init__(self, data):
        self.data = data
        self.count = len(data)
        self.sum = sum(data)
        self.min = min(data)
        self.max = max(data)
        self.range = self.max - self.min
        self.mean = mean(data)
        self.median = median(data)
        self.mode = mode(data)
        self.var = variance(data)
        self.std = stdev(data)
        self.freq_dist = Counter(data)

data = Statistics(ages)
print("Count:",data.count)
print("Sum: ",data.sum)
print("Min: ",data.min)
print("Max: ",data.max)
print("Range: ",data.range)
print("Mean: ",data.mean)
print("Median: ",data.median)
print("Mode: ",data.mode)
print("Standard Deviation: ",data.std)
print("Variance: ",data.var)
print("Frequency Distribution: ",data.freq_dist)

# Level 2
# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        if description in self.incomes:
            old_amount = self.incomes[description]
            new_amount = old_amount + amount
            self.incomes[description] = new_amount
        else:
            self.incomes[description] = amount

    def add_expense(self, description, amount):
        if description in self.expenses:
            old_amount = self.expenses[description]
            new_amount = old_amount + amount
            self.expenses[description] = new_amount
        else:
            self.expenses[description] = amount

    def total_income(self):
        total = 0
        for i in self.incomes.values():
            total += i
        return total

    def total_expense(self):
        total = 0
        for i in self.expenses.values():
            total += i
        return total

    def account_balance(self):
        income = self.total_income()
        expense = self.total_expense()
        balance = income - expense
        return balance

    def account_info(self):
        info = "Account holder: {} {}\n".format(self.firstname, self.lastname)
        info += "Incomes:\n"
        for i, j in self.incomes.items():
            info += "  {}: {}\n".format(i, j)
        info += "Total income: {}\n".format(self.total_income())
        info += "Expenses:\n"
        for i, j in self.expenses.items():
            info += "  {}: {}\n".format(i, j)
        info += "Total expense: {}\n".format(self.total_expense())
        info += "Account balance: {}\n".format(self.account_balance())
        return info

p = PersonAccount("Muhammad", "Huzaifa")
p.add_income("Salary", 100000)
p.add_expense("Rent", 100000)
print(p.account_info())