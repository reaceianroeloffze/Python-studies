# # Import the sleep function from the time module, so
# # that the sleep function can be used in this program.
# from time import sleep

# # Prompt the user to enter her name.
# name = input("Hello! What is your name? ")

# # Print the numbers 3, 2, 1.
# for i in range(3, 0, -1):
#     print(i, flush=True)
#     sleep(0.5)  # Pause for 1/2 second

# # Use a Python f-string to format a greeting
# # for the user and then print the greeting.
# print(f"Welcome to CSE 111, {name}!")

# # To get current date and time, import from datetime library
# from calendar import month
# from datetime import datetime, timedelta

# current_date = datetime.now() # Now method returns date and time at exact moment as a datetime object

# # timedalta selects given range of time
# period = timedelta(weeks=2)
# april = current_date + period

# # print current date and time
# print (f'current date and time: {current_date.time()} ')
# # print date and time 2 months from now
# print (f'currrent date 2 weeks from now: {april.date()} ')

# birdate = input('enter date of birth (YYYY/MM/DD): ')
# date = datetime.strptime(birdate, '%Y-%m-%d')
# print (date)

# --- Dictionaires ---

# -- Defining a dictionary --
# - Syntax: variable_name = {'key1': 'value1', 'key2': 'value2', 'key_n': 'value_n' }
# weapons = {
#     'Dante': 'Rebellion',
#     'Vergil': 'Yamato',
#     'Lady': 'Kalina-Ann'
# }
# # - adding and changing/updating keys and values -
# weapons['Sparda'] = 'Sword of Sparda'
# weapons['Dante'] = 'Ebony & Ivory'

# # - deleting a dictionary entry -
# del weapons['Lady']

# # - retrieve a dictionary value by specifying its key -
# print (weapons)
# print (weapons['Sparda'])
# print (weapons['Dante'])
# print (weapons['Vergil'])

# Syntax errors - programs will not run at all if there is one.
# Runtime errors - programs will fail when run. Work your way up from the line on which the error occurred to figure out what's wrong. 99% of all runtime errors are because of something you wrote in your code.
# Logic errors - when a program runs diffenently that what we expected or wanted.

x = 32
y = 0

try:
    print(x/y)
except ZeroDivisionError as e:
    print('\ndividing by zero is a math error and not allowed.')
else:
    print('Something else is wrong')
finally:
    print('Cleanup Code\n')