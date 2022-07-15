
import random
import math

def main():
    
    numbers = [16.2, 75.1, 52.3]
    print (f'Numbers: {numbers} ')

    append_random_numbers(numbers)
    print (f'After calling append_numbers_list with only one parameter: {numbers}')
    
    append_random_numbers(numbers, 3)
    print (f'After calling append_numbers_list with 2 parameters: {numbers}\n')
    
    words = []
    
    append_random_words(words)
    print(f'Words: {words}')
    
    append_random_words(words, random.randint(1, 10))
    print(f'Words: {words}')

def append_random_numbers(numbers_list, quantity=1):
    '''
    Append randomly chosen
    numbers to an existing list
    
    Parameters:
        numbers_list: a list
            containing numbers
        quantity: an integer
    Returns: Nothing
    '''
    for _ in range(quantity):
        quantity = random.uniform(0, 100)
        final_number = round(quantity, 1)
        numbers_list.append(final_number)
        
def append_random_words(words_list, quantity=1):
    '''
    Append randomly chosen 
    words from a list and
    and appends them to a
    designated list (words_list)
    
    parameters:
        words_list: a list to which
            words will be randomly appended
        quantity: An Integer which will decide
            how many words get appended to the list.
    
    return: Nothing
    '''
    
    selection = [
        'fist', 'rabbit', 'cleanse', 'fury', 'baroque',
        'horn', 'horror', 'anger', 'yaa-hoo!', 'cathedral',
        'minigun', 'caramel', 'cheesecake', 'fudge', 'Versailles',
        'carrot', 'quicksilver', 'vetkoek', 'Fluttershy', 'timbre',
        'angel', 'harp', 'froze', 'skeleton', 'cha-ching!', 'allegro'
        'gold', 'Arlind', 'Thompson', 'nature', 'gothic'
    ]
    
    for _ in range(quantity):
        quantity = random.choice(selection)
        words_list.append(quantity)
    
if __name__ == '__main__':
    main()