# --- Calculating tyre volume ---
import math

# -- Ask the user for the width, aspect ratio and diameter of tire --
w = int(input('Enter the width of the tire in mm (ex 205): '))
a = int(input('Enter the aspect ratio of the tire (ex 60): '))
d = int(input('Enter the diameter of wheel in inches (ex 15): '))
# v = ?

# -- Set function to obtain tyre volume (v) --
def v(a, w, d):
    return (math.pi*(math.pow(w, 2))*a*(w*a + 2540*d)) / 10000000000

# -- Print volume of tyre --
print (f'\nThe approximate volume is {v(a, w, d):.2f} liters')

# -- Ask user if they wish to purchase tyres of specified size --
while True:
    tyre_buy = input('Would you like to purchase tyres with the specified dimensions (Yes/No)? ')
    # -- acquire purchase details of user --
    client_name = ''
    client_surname = ''
    client_phone_number = ''
    tyre_brand = ''
    tyre_quantity = ''
    
    if tyre_buy.capitalize() == 'Yes':
        client_name = input('Please enter your name: ').title()
        client_surname = input('Please enter your surname: ').title()
        client_phone_number = input('Please enter your phone number: ')
        tyre_quantity = int(input('How many tyres would you like to buy? '))
        while True:
            tyre_brand = input("Please choose the tyre brand you'd to buy the size from (Dunlop/Bridgstone/Firestone): ").title()
            if tyre_brand == 'Dunlop' or tyre_brand == 'Bridgestone' or tyre_brand == 'Firestone':
                print ('Thank you for your purchase.')
                break
            else:
                print ('invalid option')
        break
    elif tyre_buy.capitalize() == 'No':
        print ('Goodbye.')
        break
    else:
        print ('Invalid option')

# --- Storing recorded data in a file ---
"""
Many companies wish to understand the needs and wants of their customers more deeply so the company can create products that fill those needs and wants. One way to understand customers more deeply is to record the values entered by customers while they are using a program and then to analyze those values. One common way to record values is for a program to store them in a file.
"""

# -- Import datetime library modules and appropriate members --
from datetime import datetime

current_date = datetime.now()

with open('volumes.txt', 'at') as volume_data: # 'at' is an opening mode that allows appending to the end of a text file
    # -- Print the width, aspect ratio, diameter & volume of tire as well as the date and append all to volumes.txt --
    print (f'{current_date:%Y-%m-%d}, {w}, {a}, {d}, {v(a, w, d):.2f}', file=volume_data)
    
# -- Print out purchase information and store it in a text file --
if tyre_buy.capitalize() == "Yes":
    with open('tyre_purchase.txt', 'at') as tyre_purchase:
        print (f'{client_name} {client_surname} ({client_phone_number}) purchased {tyre_quantity} {tyre_brand} tyres of width {w} mm, aspect ratio {a} and diameter {d} in on {current_date:%Y-%m-%d.}', file=tyre_purchase)
