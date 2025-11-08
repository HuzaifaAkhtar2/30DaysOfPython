from re import *
# Level 1
# What is the most frequent word in the following paragraph?
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
def most_frequent_words(string):
    words = findall(r'\b[A-Za-z]+\b', string)
    frequent_words = {}
    for i in words:
        if i in frequent_words:
            frequent_words[i] += 1
        else:
            frequent_words[i] = 1
        frequent_words_list = [(x, y) for y, x in frequent_words.items()]
    sorted_words = sorted(frequent_words_list, reverse=True)
    return sorted_words
print(most_frequent_words(paragraph))

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
def calculate_distance(lst):
    int_lst = list(map(lambda x: int(x), lst))
    int_lst.sort()
    distance = int_lst[0] - int_lst[len(int_lst) - 1]
    return distance
print(calculate_distance(points))

# Level 2
# Write a pattern which identifies if a string is a valid python variable
valid_python_variable_pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"
def is_valid_variable(string):
    return bool(match(valid_python_variable_pattern, string))
print(is_valid_variable("first_name"))
print(is_valid_variable("firstname"))
print(is_valid_variable("first-name"))
print(is_valid_variable("1first_name"))

# Level 3
# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
def clean_text(text):
    cleaned_text = sub(r'[^A-Za-z\s]', '', text)
    return cleaned_text
cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text)[:3])