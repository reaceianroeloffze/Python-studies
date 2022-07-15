import csv

def main():
    
    PRODUCT_NUMBER_INDEX = 0
    
    # Read the contents of the dentists.csv file
    # into a compound list.
    products_dict = read_dict("products.csv", PRODUCT_NUMBER_INDEX)

    print()
    
    # Print the entire list.
    print("PRODUCTS : ")
    print(products_dict)

    #print the grocery list
    # grocery_list = read_list("request.csv")
    print()
    print("list groce")
    # print(grocery_list)
    
    #indices
    #KEY COLUMN INDEX IS ALSO A PRODUCT NUMBER
    products_dict = read_dict("products.csv", PRODUCT_NUMBER_INDEX)
    
    PRODUCT_NAME_IDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX = 1

    # Opening the file and storing it in a variable.
    with open('request.csv', "rt") as requests_file:

        # Use the csv module to create a reader objec
        # that will read from the opened CSV file.
        readit = csv.reader(requests_file)
        
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(readit)

        # Reading the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for column_list in readit:

            # From the current row, retrieving the data
            # from the column that contains the product number, name and price.
            product_num = column_list[PRODUCT_NUMBER_INDEX]
            
            product_list = products_dict[product_num]
            product_name = product_list[PRODUCT_NAME_IDEX]
            product_price = product_list[PRICE_INDEX]
            
            quantity = column_list[QUANTITY_INDEX]
            

            # #print(t_items, product_num)
            # value = products_dict[product_num]
            # #print (value)
            # #Storing the data from the current row
            # #into a list.                                                                           
            # product_name = value[1]
            # price = value[2]

            #print("Requested items")
            the_products = (f"{product_name}: {quantity} @ {product_price}")
            # if item in 
            print(the_products)

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

    # Creating an empty dictionary that will
    # store the data from the CSV file.
    products = {}

    # Opening the file and storing it in a variable.
    with open(filename, "rt") as products_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(products_file)
        
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Reading the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # From the current row, retrieving the data
            # from the column that contains the product number, name and price.
           product_number = row[key_column_index]
           products[product_number] = row

            # Storing the data from the current row
            # into the dictionary.                                                                                                      ``ccccccXj
           

    # Return the dictionary.
    return products

# def read_list(filename):

#     """Read the contents of a csv into a
#     compound list and return the list

#     Parameters:
#         filename: the name of the cvs file to read.
#         key_column_index: the index of the column we will use 
#         as keys in the compund list.

#         Return: a compound list that contains the 
#         contents of the csv file."""

    
    
            
#         return the_products

#             #the_products = (f"{key_column_index},{product_name} : {product_price}")
#         #print(the_products)

#         # for row in "request.csv":
#         #     ordered_products.append("request.csv")

# #         #     print(ordered_products)        
# # # Call main to start this program.6
if __name__ == "__main__":
    main()

 
