with open('Day1_Puzzle_Input.txt') as sonar_sweep:
    
    current_max_reading = 131
    current_min_reading = 9999
    readings = []
    
    for i in sonar_sweep:
        i_clean = int(i.strip())
        # print (i_clean)
            
        if current_min_reading > current_max_reading:
            current_max_reading = current_min_reading
            
            readings.append(current_max_reading)

        # else:
        #     print(f'{max_reading} - \033[32;1mDecreased\033[0m')
    
    if current_max_reading > current_min_reading:       
        print (f'\nRThe total amount of readings that increased are {len(readings)} ')