from re import *
# Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
def lines_and_words(filename):
    file = open(filename)
    txt = file.read()
    num_of_words = len(txt.split())
    num_of_lines = len(txt.splitlines())
    file.close()
    output = "Number of words: {}\nNumber of lines: {}".format(num_of_words, num_of_lines)
    return output

print(lines_and_words(filename="./data/obama_speech.txt"))
print(lines_and_words(filename="./data/michelle_obama_speech.txt"))
print(lines_and_words(filename="./data/donald_speech.txt"))
print(lines_and_words(filename="./data/melina_trump_speech.txt"))

# Level 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
file = open("./data/email_exchanges_big.txt")
text = file.read()
emails = findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
emails = set(emails)
# print(emails)

def find_most_frequent_words(filename, num_of_words):
    file = open(filename)
    string = file.read()
    words = findall(r'\b[A-Za-z]+\b', string)
    frequent_words = {}
    for i in words:
        if i in frequent_words:
            frequent_words[i] += 1
        else:
            frequent_words[i] = 1
        frequent_words_list = [(x, y) for y, x in frequent_words.items()]
    sorted_words = sorted(frequent_words_list, reverse=True)
    file.close()
    return sorted_words[:num_of_words]

# Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
print(find_most_frequent_words("./data/obama_speech.txt", 10))
print(find_most_frequent_words("./data/michelle_obama_speech.txt", 10))
print(find_most_frequent_words("./data/donald_speech.txt", 10))
print(find_most_frequent_words("./data/melina_trump_speech.txt", 10))

# Find the 10 most repeated words in the romeo_and_juliet.txt
print(find_most_frequent_words("./data/romeo_and_juliet.txt", 10))

# Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
def lines(filename):
    file = open(filename)
    txt = file.read()
    file.close()
    lines_with_python = 0
    lines_with_js = 0
    lines_with_java = 0
    for i in txt.splitlines():
        if "python" in i.lower():
            lines_with_python += 1
        if "javascript" in i.lower():
            lines_with_js += 1
        if ("java" in i.lower()) and ("script" not in i.lower()):
            lines_with_java += 1
    output = "Lines with Python in it: {}\nLines with Java in it: {}\nLines with JavaScript in it: {}".format(lines_with_python, lines_with_java, lines_with_js)
    return output
print(lines("./data/hacker_news.csv"))
