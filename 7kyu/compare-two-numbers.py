#Description
# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.

# Example:

#     compare(13,14)=50%;
#     compare(23,22)=50%;
#     compare(15,51)=100%;
#     compare(12,34)=0%.

#MySoultion

def compare(a, b):
    num1_digits = set(str(a))
    num2_digits = set(str(b))
    intersection = num1_digits.intersection(num2_digits)
    if a == b:
        similarity = "100"
    else:
        similarity = str(int(len(intersection) / 2 * 100))
    return similarity+"%"


