# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 26/03/2018
# Last Modified Date: 28/03/2018
# Assignment 1: Task 4: Print the occurrence of each English letter
# -----------------------------------------------------------------------------

# Lets import the dictionary variable from Task 1 & decoded output from Task 3
from Task1 import dictionary
from Task3 import output_list


def count_function(decoded_list):
    """This function is used to print the occurrence of English letters/numbers from the decoded list(Task3)"""

    # We create another dictionary variable similar to dictionary created in Task 1. But insert value 0 to all keys.
    count_dict = dict.fromkeys(dictionary, 0)

    # Fetching each sequence from decoded list.
    for each_line in decoded_list:
        each_word = each_line[:-1].split("*")
        # Fetching each letter from the each sequence.
        for each_char in each_word:

            # Below 'if condition' will check whether each letter present in the list of keys in count dictionary.
            if each_char in count_dict.keys():

                # If the letter is present in the keys list from count dictionary, increment the occurrence(value) by 1.
                count_dict[each_char] += 1

    return count_dict


# store the count data in a variable which will be later used to print output.
count_characters = count_function(output_list)

print("\nEnglish character count - ")

# We'll display the count of each English character. Eg: H=1 A=1 P=2 Y=1.
for key in (key for key, value in count_characters.items() if value > 0):
    print(key, ":", count_characters[key])
