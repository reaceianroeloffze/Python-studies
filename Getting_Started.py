# print('Hello World')
# # name = input('Please Enter Name: ')
# # print(name)
# print()
# print('There are Words on this line!')
# print('Jump this line! \nMore words here!')
# print('adding numbers')
# x = 56 +1002
# print('performing division')
# y = x/0
# print('math complete')

# -- Week 2

# -- Tutorial --

# first_name = input ('First Name? ')
# last_name = input ('Last Name? ')
# first_name = 'Reace'
# last_name = 'Roeloffze'
# output = 'Greetings, ' + first_name + ' ' + last_name
# output = 'Salutations, {} {}'.format(first_name.capitalize(), last_name.capitalize())
# output = '{} {}'.format(first_name.upper(), last_name.upper())
# output = 'Howdy, {1}, {0}'.format(first_name.capitalize(), last_name.capitalize())
# output = f'Wassup, {first_name.capitalize()} {last_name.capitalize()}'
# print (output)

# -- Checkpoint Assignment --

# first_name = input('State your first name: ')
# last_name = input ('Sate your last name: ')
# name_display = f'I am known as {last_name}, {first_name} {last_name}.'
# print (name_display)


# print ('Please input the following: ')

# Adjective = input ('adjective: ')
# Noun1 = input ('Noun: ')
# Noun2 = input ('Noun: ')
# print (f'Wow! That is a very {Adjective} {Noun1}! Boy, I feel like a {Noun2}!')

# --- Working with Numbers ---

#  -- Operators --

# + Addition
# - Subtraction
# * multiplication
# / Division
# ** Exponent
# // Divide and drop remainder
# % Remainder or Modulus
# Input function always returns strings
# Int converts numbers stored in strings to integers
# Float converts numbers stored in strings to real/rational numbers

# My_Birthday = 22
# print (str(My_Birthday) + ' Is My Birthday')

# Num1 = 7
# num2 = 35
# print (num2 / Num1)
# Saving Data in new variable for future use
# Num_Tot = num2 / Num1
# print (Num_Tot)

# -- Data-type Conversion --

# Val1 = input ('Enter first number: ')
# Val2 = input ('Enter second number: ')
# Val3 = input ('Enter third number: ')
# Val4 = input ('enter fourth number: ')
# print (int(Val1) * int(Val2))
# print (float(Val3) ** float(Val4))

# Easiest way to display numbers alongside text is to use this format function.
# num = 22
# print (f'My birtday is March {num}')

# Strings - Stored sequences of any kind of characters (letters, numbers, symbols, spaces, etc.) in functions.
# Concatenation - The combining or "gluing" of 2 or more strings together.
# Type-casting or "Casting" - The coversion of data from one type to another.

# -- Checkpoint assignment --

# Age = int(input('Please enter your age: '))
# print ('Next year you will be:', int(Age + 1))
# print ()
# Egg_qnt = (input('Please specify number of egg cartons: '))
# Egg_qnt_Tot = int(Egg_qnt)
# print ('Your total eggs =',(Egg_qnt_Tot * 12))
# print ()
# Cookies = float(input('How much cookies are available? '))
# People = float(input('How many people are there? '))
# Div_Cok_Pep = (Cookies / People)
# print ('Each individual gets', Div_Cok_Pep, 'cookies each')

# --- Complex Conditions ---

# gpa = float(input('Input GPA Average: '))
# lg = float(input('input lowest grade: '))

# if gpa >= .85 and lg >= .7:
# # -- Boolean Variable -- 
#     pass_grade = True
# else:
#     pass_grade = False

# if pass_grade:
#     print ('you have passed. Congratulations!')

# -- Checkpoint Assignment: Loan --

# loan_size = float(input('How large is your loan? '))
# credit_history = float(input('Do you have good credit history? '))
# income = float(input('How high is your income? '))
# down_payment = float(input('How large is your down payment? '))

# if loan_size >= 5:
#     if credit_history >= 7 and income >= 7:
#         if (credit_history or income) >= 5 and down_payment >= 5:
#             can_issue_loan = True
#     else:
#         can_issue_loan = False
# else:
#     if loan_size < 4:
#         can_issue_loan = False
#     if income or down_payment >= 7:
#         if down_payment >= 4 and income >= 4:
#             can_issue_loan = True
#     else:
#         can_issue_loan = False
# if can_issue_loan:
#     print ('Yes.')
# if not can_issue_loan:
#     print ('No.')

# --- W7: Loops ---

# gratuity = float(input('Gratuity: '))

# # if tip < 0:
# #   print ("There's no such thing as negative money!")
# #   gratuity = float(input('Gratuity: '))
# while gratuity < 0:
#     print ("There's no such thing as negative money!")
#     gratuity = float(input('Gratuity: '))

# print (f'Gratuity: R{gratuity:.2f}')

# -- Checkpoint Assignment --

# value = int(input('enter positive number: '))

# while value < 0:
#     print ('no positive number detected.')
#     value = int(input('enter positive number: '))
# print (f'The number is: {value}')

# plea = input('May I please have a piece of candy? ')

# while plea in ('no', 'nope', 'uh-uh'):
#     plea = input('May I please have a piece of candy? ')
# print ('Thank you very much!')

#  --- Week 08 ---

# -- Checkpoint Assignment --

# colors = ["red", "blue", "green", "yellow"]
# for color in colors:
#     print (color)
# print ()
# for i in range(1,9):
#        print (i)
# print ()
# for i in range(2,22,2):
#        print (i) 

# --- Week 09: Lists ---

# Use plural variable names when working with lists
# characters = ['Lisbeth','Diane','Fluttershy','Rarity','Sunset Shimmer']

# --- Checkpoint Assignment ---

# friend_name = ''

# friends = []

# while friend_name != 'End':
#        friend_name = input('Enter Friend Name: ').capitalize()
#        if friend_name != 'End':
#               friends.append(friend_name)
# print ()
# print ('Friend Names: ')
# print ()

# for friend in friends:
#        print (friend)

# --- Week 10: Solving problems with lists ---

# --- Checkpoint Assignment ---

# shoppting_items = []

# item_purchase = ''

# while item_purchase != 'Quit':
#        item_purchase = input('Please enter Item of Purchase: ').capitalize()
#        if item_purchase != 'Quit':
#               shoppting_items.append(item_purchase)

# --- Normal 'for' loop ---
           
# for item in shoppting_items:
#        print (f'Item: {item}')

# --- Printing the index next to the number ---

# for i in range(len(shoppting_items)):
#        item = shoppting_items[i]
#        print (f'{i}. {item}')

# replace_choice = int(input('Which Item would you like to replace? '))
# item_replace = input('What new item do you want? ')
# shoppting_items[replace_choice] = item_replace

# for i in range(len(shoppting_items)):
#        item = shoppting_items[i]
#        print (f'{i}. {item}')

# --- Week 11: Files ---

# open_file = open('mock_file.txt')

# with open('mock_file.txt') as open_file: # Make sure you have the specified folder containing the file open in VS Code, otherwise you must specify the path to the folder. Files have to be closed once opened.
#     for letter in open_file:
#         let_split = letter.split(' - ')
#         characters = let_split[0]
#         char_description = let_split[1]
#         char_strip = char_description.strip()
        
# characters = ('Dante, Trish, Lady, Fluttershy, Rarity, Rainbow, Dash')
# singles = characters.split(',')

# print (characters)
# print (singles)

# whitespace_name = 'Reace       '

# no_whitespace_name = whitespace_name.strip()

# print(f'====={whitespace_name}=====')
# print(f'====={no_whitespace_name}=====')

# --- Checkpoint Assignment ---

# with open('books.txt') as bom_books:
    
#     for book in bom_books:
#         book = book.strip()
#         print (book)

# --- Week 12: Files continuted ---

# --- Checkpoint assignment ---

# people = [
#     "Stephanie 36",
#     "John 29",
#     "Emily 24",
#     "Gretchen 54",
#     "Noah 12",
#     "Penelope 32",
#     "Michael 2",
#     "Jacob 10"
# ]
# age = []
# # # -- 01: Interate through list and print it --
# # for peron in people:
# #     print (peron)
    
# # -- 02: Split strings into name and age and print --
# for person in people:
#     person_split = person.split(' ')
#     single_person = person_split[0]
#     person_age = int(person_split[1])
#     age.append(person_age)
#     for i in range(len(age)):
#         age_pos = age[i]
#     print (f'{i}. {single_person}, {person_age}')

# print (f'Youngest person in list is: {people[6]}')

# --- Week 13: Intro to functions ---

# 2 advantages of using functions:
# 1. It makes code more readable
# 2. When code needs to be edited, editing only tskes place in one place rather than having to change it everywhere when you copy-paste code.
# Setting parameters in functions allow for different executions of the same code defined by a function.
# always add comments to explain the purpose of your function.

from datetime import datetime

# --- Function to print date/time ---
# def print_random(task_name):
#     print (task_name)
#     print (datetime.now())
#     print ()
# fictional_crush = 'Fluttershy'
# print_random(f'{fictional_crush} is the best')

# for x in range(0,10):
#     print (x)
# print ()
# print_random('End of List')

# # --- function to retrieve information about a character ---
# def get_characters(info):
#     character = info.title()
#     return character
    

# crush = input('Input crush here: ')
# my_crush = get_characters(crush)

# franchise = input('Input franchise of crush: ')
# franchise_crush = get_characters(franchise)

# print (f'My crush is {my_crush} from {franchise_crush}.')

# --- Checkpoint assignment ---

# Function to print strings in different cases:
def display_strings(sentence, force_upper = True, force_lower = True):
    if force_upper:
        phrase = sentence.upper()
    elif force_lower:
        phrase = sentence.lower()
    else:
        phrase = sentence
    return phrase

input_sentence = input('say anything: ')
input_sentence_prhase1 = display_strings(input_sentence, force_upper=True, force_lower=False)
input_sentence_prhase2 = display_strings(input_sentence, force_upper=False, force_lower=True)
input_sentence_prhase3 = display_strings(input_sentence, force_upper=False, force_lower=False)
print (input_sentence_prhase1)
print (input_sentence_prhase2)
print (input_sentence_prhase3)

