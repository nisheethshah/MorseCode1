# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 22/03/2018
# Last Modified Date: 26/03/2018
# Assignment 1: Task 3: Decoding Morse Code Sequences
# -----------------------------------------------------------------------------

# Lets import the dictionary variable from Task 1
from Task1 import dictionary
from Task2 import input_morse


def decode_function(morse_code):
    """This function is used to decode the Morse code into English letters/numbers. Morse code is parameter"""

    decoded_output = []

    # Fetching each sequence from Morse code input.
    for each_line in morse_code:
        morse_code_split = each_line.split("*")
        decode_string = ""

        # Fetching each letter from the each sequence. Eg.: 1010
        for each_word in morse_code_split:

            # Below 'if condition' checks whether input input codes match with dictionary values. Eg.: 1010 == 1010?
            if each_word in dictionary.values():

                # This 'if section' means that user input code matches with the dictionary value.
                # So therefore, we'll save English character(key) for pairing value from the dictionary.
                decode_string += (list(dictionary.keys())[list(dictionary.values()).index(each_word)])
                decode_string += "*"    # Storing each English character separated by *. Eg.: H*A*P*P*Y

                # # Counting of each word had been done below here but as per assignment this should be in Task 4.
                # # I think having it here saves memory & time. Instead of re executing loops in task 4.
                # count_dict[(list(dictionary.keys())[list(dictionary.values()).index(each_word)])] += 1

            else:

                # if the user input code doesn't match with any dictionary value,
                # then we show "<Invalid Word>" for that character. Eg.: H*A*P*<Invalid letter>*Y
                decode_string += "<invalid letter>*"

        # Print the decoded sequence.
        print(each_line + " : " + (decode_string[:-1]).replace('*', ''))

        # Append the same decoded sequence in another list.
        decoded_output.append(decode_string)
    return decoded_output


# This is used to translate morse code into understandable English format.
print("\nMorse to English - ")
output_list = decode_function(input_morse)
