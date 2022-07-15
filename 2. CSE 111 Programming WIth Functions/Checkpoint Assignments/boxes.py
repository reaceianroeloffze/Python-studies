# --- Checkpoint Assigment 02: Calling Functions ---

# --- Notes ---
# -- Calling a built-in Python function: --
# variable_name = function_name(arg1, arg2, … argN)

# -- Calling a Module: --
# import module_name

# variable_name = module_name.function_name(arg1, arg2, … argN)

# -- Calling a Method: --
# variable_name = object_name.method_name(arg1, arg2, … argN)

# --- Programming assignment & instructions ---
"""
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers: 1) the number of manufactured items and 2) the number of items that the user will pack per box. Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
"""
# -- Import the Math Library to access math modules --
import math

# -- Get number of manufatured items and number of items contained within each box --
manufactured_items = int(input('How many items were manufactured? '))
items_per_box = int(input('How many items will each box contain? '))

# -- Calculate how many boxes will be needed for all the items --
boxes_needed = math.ceil(manufactured_items / items_per_box)

# -- print the number of boxes that will be needed to contain all manufactured items --
print (f'\nFor {manufactured_items} items, {boxes_needed} boxes will be needed.')


