#Description
# Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

# --> "alpha beta gamma delta alpha beta gamma delta"

#MySolution
def remove_consecutive_duplicates(s):
    original_list = s.split()
    if not original_list:
        return ""
    new_list = [original_list[0]]
    for i in range(1, len(original_list)):
        if original_list[i] != original_list[i-1]:
            new_list.append(original_list[i])
    return ' '.join(new_list)