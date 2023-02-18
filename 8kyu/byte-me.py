
#  Description

# If I were to ask you the size of "hello", what would you say?
# Wait, let me rephrase the question:
# If I were to ask you the total byte size of "hello", how many bytes do you think it takes up?
# I'll give you a hint: it's not 5.
# len("hello")  -->  5
# byte size -->  54
# 54? What?!
# Here's why: every string has to have an encoding (e.g ASCII),the info that makes it an object, 
# as well as all of it's other properites... it would have to take up a bit more than 5 bytes, wouldn't it?
# This might be useful for sending something over a network, where you need to represent the memory size 
# the item takes up. 

#My Solution
# return the total byte size of the object. 
import sys
def total_bytes(object):
    '''Return the memory size of an object in bytes.'''
    size=sys.getsizeof(object)
    if isinstance(object,str):
        size+=object.count('\0')
    return size
