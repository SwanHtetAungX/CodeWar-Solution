#Description
# In this kata you will be given a sequence of the dimensions of rectangles ( sequence with width and length ) and circles ( radius - just a number ).
# Your task is to return a new sequence of dimensions, sorted ascending by area.

# For example,

# seq = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ] # [ rectangle, circle, circle, rectangle ]
# sort_by_area(seq) => [ ( 1.342, 3.212 ), 1.23, ( 4.23, 6.43 ), 3.444 ]

#MySolution
from math import pi
def sort_by_area(seq):
    areas = [] # create empty list of areas
    for s in seq:
        if isinstance(s, tuple):
            areas.append((s, s[0] * s[1])) # calculate and append rectangle area
        elif isinstance(s, (int, float)):
            areas.append((s, pi * s ** 2)) # calculate and append circle area
    areas.sort(key=lambda x: x[1]) # sort by area
    print([s[0] for s in areas]) # return sorted list of shapes
sort_by_area([ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ])