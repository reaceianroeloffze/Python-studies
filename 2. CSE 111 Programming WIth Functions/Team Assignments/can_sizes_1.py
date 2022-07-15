import math

def main():
    can_sizes = [
        ['#1 Picnic', 6.83, 10.16, 0.28],
        ['#1 Tall',	7.78, 11.91, 0.43],
        ['#2',	8.73, 11.59, 0.45],
        ['#2.5', 10.32,	11.91, 0.61],
        ['#3 Cylinder',	10.79, 17.78, 0.86],
        ['#5',	13.02,	14.29, 0.83],
        ['#6Z',	5.40, 8.89,	0.22],
        ['#8Z short', 6.83, 7.62, 0.26],
        ['#10',	15.72, 17.78, 1.53],
        ['#211', 6.83, 12.38, 0.34],
        ['#300', 7.62, 11.27, 0.38],
        ['#303', 8.10, 11.11, 0.42]
    ]
    
    best_storage_efficiency = None
    best_cost_efficiency = None
    max_storage_efficiency = -1
    max_cost_efficiency = -1
    
    for name, r, h, cost in can_sizes:
        v = compute_volume(math.pi * math.pow(r, 2) * h)
        sa = compute_surface_area(2 * math.pi * r * (r + h))
        storage_efficiency = compute_storage_efficiency(v / sa)
        cost_efficiency = compute_cost_efficiency(v / cost)
        print (f'{name} {storage_efficiency:.1f} ${cost_efficiency:.2f} ')
        
        if storage_efficiency > max_storage_efficiency:
            best_storage_efficiency = name
            max_storage_efficiency = storage_efficiency
            
        if cost_efficiency > max_cost_efficiency:
            best_cost_efficiency = name
            max_cost_efficiency = cost_efficiency
    
    print (f'\nBest can size for storage efficient is: {best_storage_efficiency}')
    print (f'Best can size for cost efficient is: {best_cost_efficiency}')
           
# -- Define fuction to compute can volumes --
def compute_volume(v):
    '''Compute the volume of cans with
        different dimensions and return it
    parameter v: a stored calculated volume
        for x amount of can sizes
    return: said calculated volume in cm^3
        for each can
    '''
    volume = v
    return volume

# -- Define function to compute surface area of cans --
def compute_surface_area(sa):
    '''Compute the surface area
        of various can sizes and return it
    parameter sa: a stored calculated
        surface area for x amount of can sizes
    return: said calculated surface area
        for each can
    '''
    surface_area = sa
    return surface_area

# -- Define function to compute storage efficiency of cans --
def compute_storage_efficiency(storage_efficiency):
    '''Compute and return the storage effiency
        of cans with differing dimensions
    parameter efficiency: stored and calculated 
        storage efficiency for x amount of can sizes from x amount
        of volumes calculated / x amount of surface areas
        calculated
    return: said calculated storage efficiency
        for each can'''
    efficiency = storage_efficiency
    return efficiency

# -- Define a function that computes the cost efficiency of cans --
def compute_cost_efficiency(cost_efficiency):
    '''Compute and return the cost efficiency
       of cans with differing dimensions
    parameter cost efficiency: store a calculated
        cost efficiency for x amount can sizes from
        x amount of volumes calculated / x amount of
        costs per can
    return: said calculated and stored cost efficiency
        for each can
    '''
    ce = cost_efficiency
    return ce

main()