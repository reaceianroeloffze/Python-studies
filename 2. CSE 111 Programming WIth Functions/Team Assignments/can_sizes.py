# --- Team Activity: Calculating Can Efficiency ---
import math

# -- Begin by defining main function --
# def main():
#     volume = compute_volume((math.pi * math.pow(6.83, 2) * 10.16), 
#                             (math.pi * math.pow(7.78, 2) * 11.91),
#                             (math.pi * math.pow(8.73, 2) * 11.59), 
#                             (math.pi * math.pow(10.32, 2) * 11.91), 
#                             (math.pi * math.pow(10.79, 2) * 17.78),
#                             (math.pi * math.pow(13.02, 2) * 14.29),
#                             (math.pi * math.pow(5.4, 2) * 8.89),
#                             (math.pi * math.pow(6.83, 2) * 7.62),
#                             (math.pi * math.pow(15.72, 2) * 17.28),
#                             (math.pi * math.pow(6.83, 2) * 12.38),
#                             (math.pi * math.pow(7.62, 2) * 11.27),
#                             (math.pi * math.pow(8.1, 2) * 11.11))
    
#     surface_area = compute_surface_area((2 * math.pi * 6.83 * (6.83 + 10.16)),
#                                         (2 * math.pi * 7.78 * (7.78 + 11.91)),
#                                         (2 * math.pi * 8.73 * (8.73 + 11.59)),
#                                         (2 * math.pi * 10.32 * (10.32 + 11.91)),
#                                         (2 * math.pi * 10.79 * (10.79 + 17.78)),
#                                         (2 * math.pi * 13.02 * (13.02 + 14.29)),
#                                         (2 * math.pi * 5.4 * (5.4 + 8.89)),
#                                         (2 * math.pi * 6.83 * (6.83 + 7.62)),
#                                         (2 * math.pi * 15.72 * (15.72 + 17.28)),
#                                         (2 * math.pi * 6.83 * (6.83 + 12.38)),
#                                         (2 * math.pi * 7.62 * (7.62 + 11.27)),
#                                         (2 * math.pi * 8.1 * (8.1 + 11.11)))
    
#     efficiency = compute_storage_efficency((math.pi * math.pow(6.83, 2) * 10.16) / (2 * math.pi * 6.83 * (6.83 + 10.16)),
#                             (math.pi * math.pow(7.78, 2) * 11.91) / (2 * math.pi * 7.78 * (7.78 + 11.91)),
#                             (math.pi * math.pow(8.73, 2) * 11.59) / (2 * math.pi * 8.73 * (8.73 + 11.59)),
#                             (math.pi * math.pow(10.32, 2) * 11.91) / (2 * math.pi * 10.32 * (10.32 + 11.91)),
#                             (math.pi * math.pow(10.79, 2) * 17.78) / (2 * math.pi * 10.79 * (10.79 + 17.78)),
#                             (math.pi * math.pow(13.02, 2) * 14.29) / (2 * math.pi * 13.02 * (13.02 + 14.29)),
#                             (math.pi * math.pow(5.4, 2) * 8.89) / (2 * math.pi * 5.4 * (5.4 + 8.89)),
#                             (math.pi * math.pow(6.83, 2) * 7.62) / (2 * math.pi * 6.83 * (6.83 + 7.62)),
#                             (math.pi * math.pow(15.72, 2) * 17.78) / (2 * math.pi * 15.72 * (15.72 + 17.78)),
#                             (math.pi * math.pow(6.83, 2) * 12.38) / (2 * math.pi * 6.83 * (6.83 + 12.38)),
#                             (math.pi * math.pow(7.62, 2) * 11.27) / (2 * math.pi * 7.62 * (7.62 + 11.27)),
#                             (math.pi * math.pow(8.1, 2) * 11.11) / (2 * math.pi * 8.1 * (8.1 + 11.11)))
    
#     print(f'{efficiency}')

# def compute_volume(picnic, tall, two, two_five, cylinder, five, six_z, eight_z_short, ten, two_eleven, three_hundred, three_zero_three):
#     volume = picnic, tall, two, two_five, cylinder, five, six_z, eight_z_short, ten, two_eleven, three_hundred, three_zero_three
#     return volume

# def compute_surface_area(picnic, tall, two, two_five, cylinder, five, six_z, eight_z_short, ten, two_eleven, three_hundred, three_zero_three):
#     surface_area = picnic, tall, two, two_five, cylinder, five, six_z, eight_z_short, ten, two_eleven, three_hundred, three_zero_three
#     return surface_area

# def compute_storage_efficency(picnic, tall, two, two_five, cylinder, five, six_z, eight_z_short, ten, two_eleven, three_hundred, three_zero_three):
#     efficiency = picnic, tall, two, two_five, cylinder, five, six_z, eight_z_short, ten, two_eleven, three_hundred, three_zero_three
#     return efficiency
# main()

def main():
    name = '#1 Picnic'
    v = compute_volume(math.pi * math.pow(6.83, 2) * 10.16)
    sa = compute_surface_area(2 * math.pi * 6.83 * (6.83 + 10.16))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.28)
    print (f'{name} {efficiency:.1f} ${cost_efficiency:.2f} ')
    
    name = '#1 Tall'
    v = compute_volume(math.pi * math.pow(7.78, 2) * 11.91)
    sa = compute_surface_area(2 * math.pi * 7.78 * (7.78 + 11.91))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.43)
    print (f'{name} {efficiency:.1f} ${cost_efficiency:.2f} ')
    
    name = '#2'
    v = compute_volume(math.pi * math.pow(8.73, 2) * 11.59)
    sa = compute_surface_area(2 * math.pi * 8.73 * (8.73 + 11.59))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.45)
    print (f'{name} {efficiency:.1f} ${cost_efficiency:.2f} ')
    
    name = '#2.5'
    v = compute_volume(math.pi * math.pow(10.32, 2) * 11.91)
    sa = compute_surface_area(2 * math.pi * 10.32 * (10.32 + 11.91))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.61)
    print (f'{name} {efficiency:.1f} ${cost_efficiency:.2f} ')
    
    name = '#3 Cylinder'
    v = compute_volume(math.pi * math.pow(10.79, 2) * 17.78)
    sa = compute_surface_area(2 * math.pi * 10.79 * (10.79 + 17.78))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.86)
    print (f'{name} {efficiency:.1f} ${cost_efficiency:.2f} ')
    
    name = '#5'
    v = compute_volume(math.pi * math.pow(13.02, 2) * 14.29)
    sa = compute_surface_area(2 * math.pi * 13.02 * (13.02 + 14.29))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.83)
    print (f'{name} {efficiency:.1f} ${cost_efficiency:.2f} ')
    
    name = '#6Z'
    v = compute_volume(math.pi * math.pow(5.4, 2) * 8.89)
    sa = compute_surface_area(2 * math.pi * 5.4 * (5.4 + 8.89))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.22)
    print (f'{name} {efficiency:.1f} ${cost_efficiency:.2f} ')
    
    name = '#8Z short'
    v = compute_volume(math.pi * math.pow(6.83, 2) * 7.62)
    sa = compute_surface_area(2 * math.pi * 6.83 * (6.83 + 7.62))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.26)
    print (f'{name} {efficiency:.1f} {cost_efficiency} ')
    
    name = '#10'
    v = compute_volume(math.pi * math.pow(15.72, 2) * 17.78)
    sa = compute_surface_area(2 * math.pi * 15.72 * (15.72 + 17.78))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 1.53)
    print (f'{name} {efficiency:.1f} {cost_efficiency} ')
    
    name = '#211'
    v = compute_volume(math.pi * math.pow(6.83, 2) * 12.38)
    sa = compute_surface_area(2 * math.pi * 6.83 * (6.83 + 12.38))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.34)
    print (f'{name} {efficiency:.1f} {cost_efficiency} ')
    
    name = '#300'
    v = compute_volume(math.pi * math.pow(7.62, 2) * 11.27)
    sa = compute_surface_area(2 * math.pi * 7.62 * (7.62 + 11.27))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.38)
    print (f'{name} {efficiency:.1f} ${cost_efficiency:.2f} ')
    
    name = '#303'
    v = compute_volume(math.pi * math.pow(8.1, 2) * 11.11)
    sa = compute_surface_area(2 * math.pi * 8.1 * (8.1 + 11.11))
    efficiency = compute_storage_efficiency(v / sa)
    cost_efficiency = compute_cost_efficiency(v / 0.42)
    print (f'{name} {efficiency:.1f} ${cost_efficiency:.2f} ')
    
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
def compute_storage_efficiency(efficiency):
    '''Compute and return the storage effiency
        of cans with differing dimensions
    parameter efficiency: stored and calculated 
        storage efficiency for x amount of can sizes from x amount
        of volumes calculated / x amount of surface areas
        calculated
    return: said calculated storage efficiency
        for each can'''
    storage_efficiency = efficiency
    return storage_efficiency

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