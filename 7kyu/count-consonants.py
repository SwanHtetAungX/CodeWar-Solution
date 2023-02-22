#Description
# Description:

# Complete the function that takes a string of English-language text and returns the number of consonants in the string.

# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.
#MySolution
def consonant_count(s):
    count=0
    lower=s.lower()
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    for i in lower:
        if i in consonants:
            count+=1
    return count