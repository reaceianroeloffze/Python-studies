import csv

# define main function
def main():
    
    provinces_list = get_province_list('provinces.txt')
    print (provinces_list)
    
    # Remove the first and last item of the list   
    provinces_list.pop(0)
    provinces_list.pop()
        
    # Replace AB with Alberta
    for i in range(len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'
    
    albertas = provinces_list.count('Alberta')
    
    print (f'\nAlberta appears {albertas} times in the modified list.')

def get_province_list(provinces):
    '''
    Read through the Canadian Provinces
        in the provinces.txt file and return
        a modified version of the file in a list.
    Parameter:
        provices: the name of the file to be
            read through.
    Return: A list of strings.
    '''
    
    # Open the text file provinces.txt to read
    with open('provinces.txt', 'rt') as canadian_provinces:
        
        # Call the csv.reader method to read through the text file.
        file_reader = csv.reader(canadian_provinces)
        
        provinces = []
        
        # loop through the list and print it
        for province in canadian_provinces:
            clean_list = province.strip()
            provinces.append(clean_list)
            
    return provinces
    
main()