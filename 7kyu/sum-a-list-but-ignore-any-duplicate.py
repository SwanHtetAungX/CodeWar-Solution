#Description
# Please write a function that sums a list, but ignores any duplicate items in the list.

# For instance, for the list [3, 4, 3, 6] , the function should return 10.

#MySolution

def sum_no_duplicates(l):
    seen = set()
    duplicates = set()
    for i in l:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return sum(seen - duplicates)
