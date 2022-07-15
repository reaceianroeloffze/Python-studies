import csv

def main():
    
    students_dict = read_dict('students.csv', 0)
    
    i_num = validate_number('Please enter an I-Number (xxxxxxxxx). Type 0 to quit: ')
        
    # while True: 
    #     if i_num != '0':
            
    #         true_i_num = i_num.replace('-', '')
        
    #         if not true_i_num.isdigit():
    #             print ('Invalid I-Number.')

    #         else:
    #             if len(true_i_num) > 9 or len(true_i_num) < 9:
    #                 print ('I-Number must be 9 digits. You have either '
    #                 'input too few or too many digits')
                    
    #             else:
    #                 if i_num in students_dict or true_i_num in students_dict:
                            
    #                     student = students_dict[true_i_num]
                            
    #                     student_name = student[1]
                            
    #                     print (f'{student_name}')
    #                 else:
    #                     print ('No such student')

    #     else:
    #         print ('Thank you.')
    #         break
    
        
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
    
    with open(filename, 'rt') as students_file:
        
        dictionary = {}
        
        file_reader = csv.reader(students_file)
        
        next(file_reader)
        
        for student in file_reader:
            i_number = student[key_column_index]
            dictionary[i_number] = student
    
    return dictionary

def validate_number(input_number):
    '''
    Validates whether a number entered by a user
    exists and loops through the input until a valid
    number is entered.
    
    Parameters:
        input_number: A number entered by a user.
    '''
    students_dict = read_dict('students.csv', 0)
    
    while True: 
        inp = input(input_number)
        
        if inp != '0':
            
            true_inp = inp.replace('-', '')
        
            if not true_inp.isdigit():
                print ('Invalid I-Number.')

            else:
                if len(true_inp) > 9 or len(true_inp) < 9:
                    print ('I-Number must be 9 digits. You have either '
                    'input too few or too many digits')
                    
                else:
                    if inp in students_dict or true_inp in students_dict:
                            
                        student = students_dict[true_inp]
                            
                        student_name = student[1]
                            
                        print (f'{student_name}')
                    else:
                        print ('No such student')

        else:
            print ('Thank you.')
            break
        
        return true_inp

if __name__ == '__main__':
    main()