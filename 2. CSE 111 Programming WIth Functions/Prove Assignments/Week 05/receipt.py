import csv
from datetime  import datetime
import math

def main():
    
    try:
        
        # Indexes for the lists in the dictionary, products_dict:
        PRODUCT_KEY_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRICE_INDEX = 2
        
        # Call the read_dict function that returns a dictionary.
        products_dict = read_dict('products.csv', PRODUCT_KEY_INDEX)
        
        # Print the dictionary.
        for product_key in products_dict:
            print (products_dict[product_key])
        
        
        # Index for the qunatity of products requested in the
        # request.csv list
        REQUEST_PRODUCT_KEY_INDEX = 0
        QUANTITY_INDEX = 1
        
        # Open the request.csv file for reading
        file_name = 'request.csv'
        with open(file_name, 'rt') as requests_file:
            
            # Use the csv reader object to convert the contents
            # of the file into a list.
            file_reader = csv.reader(requests_file)
            next(file_reader)
            
            # Print the name of the store.
            print ('\nGrocer Guru\n')
            
            subtotal = 0
            sales_tax = 0
            total = 0
            
            # Loop through the request.csv file
            for requested_product in file_reader:
                
                # Find the index of the product key in the request.csv file list.
                requested_product_key = requested_product[REQUEST_PRODUCT_KEY_INDEX]
                
                # Use the product key from the request.csv file list to find & the
                # retrieve the corresponding values of the product key keys in the
                # dictionary.
                product_info = products_dict[requested_product_key]
                
                # Get the indexes of the items in the dictonary list and the request.csv
                # list and store them in variables.
                product_name = product_info[PRODUCT_NAME_INDEX]
                quantity = int(requested_product[QUANTITY_INDEX])
                price = float(product_info[PRICE_INDEX])
                
                # Get the subtotal, sales tax and total prices from the items that were
                # ordered. Sales tax is 6% in this case.
                subtotal += price * quantity
                sales_tax = subtotal * 0.06
                total = subtotal + sales_tax
                
                # Print the desired indexes.
                print (f'{product_name}: {quantity} @ ${price:.2f}')
    
        # Call the tally_quantity function that returns the
        # total quantity of a list of quantites stored in a
        # csv file. 
        # SPECIAL NOTE: If you know how long your list is and
        # you are familiar enough with how the lists are indexed
        # it is not necessary to store those indexes in variables
        # such as QUANTITY_INDEX = 1. If you know the length of your
        # list and at index the specified value is that you are seeking,
        # you need only specify the index itself in the parameter when you
        # call the function. Another way would be to set a default value for
        # the index in the parameter when you define the fuction if you know
        # the index of what you are looking for in the list.
        total_quantity = tally_quantity('request.csv', 1)
        
        # Print the total quantity.
        print (f'\nNumber of Items: {total_quantity} ')
        
        # Print the subtotal, sales tax and grand total.
        print (f'Subtotal: ${subtotal:.2f}')
        print (f'Sales Tax: ${sales_tax:.2f}')
        print (f'Total: ${total:.2f}')
        
        # Request the user to enter the amout of money they'll be
        # paying.
        user_amount = validate_amount_input('\nPlease enter payment amount: $', total)
        
        # Print the amount paid.
        print (f'Amount paid: ${user_amount:.2f}')
        
        # calculate the change and print it too.
        change = user_amount - total
        
        print (f'Change: ${change:.2f}')
        
        # Print a thank you message and the current date and time.
        print ('\nThank you for choosing Grocer Guru for your '\
            'shopping needs! PLease shop with us again!')
        
        # Get the current date and time from the computer's
        # operating system to print on the receipt.
        current_datetime = datetime.now()
        
        # Print the current date and time.
        print (f'{current_datetime:%a %b %d %H:%M:%S %Y}')
        
    except KeyError as wrong_key_err:
        print (f'\nError: Unknown product ID in the {file_name} file: {wrong_key_err} ')
        
    except PermissionError as unauthorised_err:
        print (f'\nYou do not have permission to acces this file.\n{unauthorised_err}')
        

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    try:
        # Create an empty dictionary.
        products = {}
        
        # Open the csv file to be read.
        with open(filename, 'rt') as products_file:
            
            # Use the csv reader object to read the csv file in
            # list form.
            file_reader = csv.reader(products_file)
            
            # Skip over the first line in the file as it does not
            # contain any data.
            next(file_reader)
            
            # Loop through the list one row at a time.
            for product in file_reader:
                
                # Get the index in the list at which the
                # product number is stored.
                product_key = product[key_column_index]
                
                # Update/append to the created dictionary
                # using the product number as a key and the
                # whole list as its value.
                products[product_key] = product
                
        # Return the dictionary    
        return products
    
    except FileNotFoundError as file_absence_err:
        print (f'Error: Missing file\n{file_absence_err}')
        
    except PermissionError as unauthorised_err:
        print (f'You do not have permission to acces this file.\n{unauthorised_err}')

def tally_quantity(filename, list_index):
    '''
    Read through a csv file and add up the 
    quantities from said file and return
    the total quantity.
    
    Parameters:
        filename: the name of the csv file to be read.
        list_index: The index in a list at which a
            quantity is stored.
        return: the total quantity of all the quantities
            in the csv file.
    '''
    
    try: 
        # open the csv file to be read.
        with open(filename, 'rt') as file:
            
            # Use the csv file reader object to
            # read the file in list form.
            file_reader = csv.reader(file)

            # skip over the first line of the file
            # as it contains no data.
            next(file_reader)

            total_quantity = 0

            # Loop through the list on row at a time
            for quantities in file_reader:

                # get the index in the list at which 
                # the quantites are stored.
                quantity = int(quantities[list_index])
                
                # Tally all qunatities in the list.
                total_quantity += quantity
                
        # Return the total computed quantity.   
        return total_quantity
    
    except FileNotFoundError as file_absence_err:
        print (f'\nError: Missing file\n{file_absence_err}')
        
    except PermissionError as unauthorised_err:
        print (f'\nYou do not have permission to acces this file.\n{unauthorised_err}')
    
    
def validate_amount_input(user_input, min_amount):
    '''
    Get a float from the user and validate 
    that the number entered is indeed a float
    and not any other characters. Repeat the prompt
    until the user enters just a number.
    
    Parameters:
        user_input: an input to display to the user
            which must then be filled out.
        min_amount: the smallest number the user can
            input in order for it to be valid.
    Return: The user's actual input.
    '''

    while True:
        try:
            inp = input(user_input)
            amount = float(inp)
            
            if amount < min_amount:
                print (f'Insufficient amount.\n'
                       'Please enter at least the total '
                       'of what is displayed.')
            else:
                break
            
        except ValueError as val_err:
            # The user entered at least one character
            # that isn't part of the floating point number
            # so request the user to enter a number.
            print (f'{inp} is not a number.\n'
               'Please enter a number.')
    
    return amount        

if __name__ == '__main__':
    main()