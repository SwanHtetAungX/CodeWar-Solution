#Description
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
#MySolution
def reverse_words(text):
    words = text.split(" ")
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return " ".join(words)

