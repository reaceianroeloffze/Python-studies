# --- Team Assignemt 01: Writing a Program to determine a discounted price for a client's submitted Subtotal based on a certain day ---

# --- Problem Statement ---
"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.
"""

user_price = 1
user_subtotal = 0

# -- Create Loop for customer to list prices and quantities of items to buy until customer types 0 --
while True:
    user_price = float(input('Enter price (type 0 to quit): $'))
    if user_price != 0:
        quantity = int(input('Enter quantity: '))
        # -- Compute the Subtotal --
        user_subtotal += user_price * quantity
    else:
        break

print ()  
# -- Print the subtotal --
print (f'Subtotal: ${user_subtotal:.2f}')

# -- import datetime class from datetime module to acquire the current date and time of a computer's operating system --
from datetime import datetime

# -- Acquire the current date and time by using the now method and store it in a variable --
current_datetime = datetime.now()

# -- Use the weekday method to call the specific weekday on the computer's operating system --
current_day = current_datetime.weekday()
# current_day = 2

# -- Set condition to obtain and display discount when applicable, in this case on Tuesdays and Wednesdays and when subtotal is $50 or more --
if user_subtotal >= 50 and (current_day == 1 or current_day == 2):
    
    # -- Obtain and sisplay Discount --
    user_discount = user_subtotal * 0.1
    print (f'Discount amount: ${user_discount:.2f}')
    
    # -- Obtain and display Sales Tax --
    sales_tax = (user_subtotal - user_discount) * 0.06
    print (f'Sales tax amount: ${sales_tax:.2f}')

    # -- Obtain and display Total --
    user_total = (user_subtotal - user_discount) + sales_tax
    print (f'Total: ${user_total:.2f} ')

else:
    # -- Obtain and display Sales Tax --
    sales_tax = user_subtotal * 0.06
    print (f'Sales tax amount: ${sales_tax:.2f}')

    # -- Obtain and display Total --
    user_total = user_subtotal + sales_tax
    print (f'Total: ${user_total:.2f} ')
    
    # -- Set a condtion for the customer to be notified when they make a purchase on a Tuesday or a Wednesday and it is just short of the $50 in order to receive the discount:
    if user_subtotal < 50 and (current_day == 1 or current_day == 2):
        missing_amount = 50 - user_subtotal
        print (f'You short ${missing_amount} in order to receive our Tuesday/Wednesday 10% discount.')
