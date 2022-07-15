def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    # 1. Add code to reverse and print fruit_list.
    fruit_list.reverse()
    print (f'\nreversed fruit list: {fruit_list}')
    
    # 2. Add code to append "orange" to the end of fruit_list and print the list.
    fruit_list.append('orange')
    print (f'\nAppend orange: {fruit_list}')
    
    # 3. Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
    i = fruit_list.index('apple')
    fruit_list.insert(i, 'cherry')
    print (f'Insert cherry: {fruit_list}')
    
    # 4. Add code to remove "banana" from fruit_list and print the list.
    fruit_list.remove('banana')
    print (f'\nRemove banana: {fruit_list}')
    
    # 5. Add code to pop the last element from fruit_list and print the popped element and the list.
    popped_item = fruit_list.pop()
    print (f'\npop {popped_item}: {fruit_list}')
    
    # 6. Add code to sort and print fruit_list.
    fruit_list.sort()
    print (f'\nSorted fruit list: {fruit_list}')
    
    # 7. Add code to clear and print fruit_list.
    fruit_list.clear()
    print (f'\nCleared fruit list: {fruit_list}')

main()