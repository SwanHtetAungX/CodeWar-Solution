#Description

# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9.

#MySolution
def square_sum(numbers):
    sum=0
    for i in range(len(numbers)):
        sum+=numbers[i]**2
    return sum
        


