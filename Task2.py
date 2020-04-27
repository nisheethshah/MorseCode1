# -----------------------------------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 22/03/2018
# Last Modified Date: 24/03/2018
# Assignment 1: Task 2: Reading Morse Code Sequences & check for valid/invalid input
# -----------------------------------------------------------------------------------------------------

# Re library provides regular expression matching operations. Its usage is seen further in the program.
import re


def input_function(message_for_input):
    """"'input_function' function is used to take input from the user."""
    """"'message_for_input' is kept just in case want to show message to the user. Can be ignored if not required."""
    user_string = input(
        message_for_input + "Please type your your Morse code here:")
    return user_string


def input_validation_function(morse_code):
    """This function is created to validate whether the input is 0 &/or 1 & separated by '*' """
    invalid_word = []
    for each_line in morse_code:

        # print("Each Input: ", each_line)
        morse_code_split = each_line.split("*")

        # "re.compile(r'[^0-1]')" is a regular expression syntax applied via "re" library to check whether 0 and/or 1.
        # We have stored the regular expression syntax in "zero_one_re"
        zero_one_re = re.compile(r'[^0-1]')
        for each_word in morse_code_split:

            # Below we are checking whether all characters(eg. '110') from input morse code match with only 0 and/or 1.
            # Or check whether blank character (eg. '')
            if (bool(zero_one_re.search(each_word)) is True) or not each_word:

                # if not 0 and/or 1 then we store that character in "invalid_word" list.
                invalid_word.append(each_line)

                # get out of loop if invalid character. No need to check other characters too.
                break

    # Remove all the invalid character (other than 0 and/or 1) from the user input list
    for each_word in invalid_word:

        # List that do not contain '0 and/or 1' is removed from the original input.
        morse_code.remove(each_word)
    return morse_code, invalid_word


input_morse = []
my_str = "garbage"  # this is created to store some random data in "my_str" so that it doesn't start as blank.

print("\n" +
      "Enter the word in Morse code(0/1) separated by * (e.g.: ""0110*1011*1*0000*111*10"" for ""PYTHON""). " +
      "Leave blank & press Enter to terminate.")

# While loop below helps to keep asking user from inputs until user leaves blank to terminate.
while my_str != "":
    my_str = input_function("")
    if my_str != "":
        input_morse.append(my_str)

# Print the whole list of user input
print("\nUser input:", str(input_morse)[1:-1])


if input_morse:

    # "input_validation_function" function helps to check whether user input is correct or not i.e. only 0 and/or 1;
    # And also, it should be separated by "*" only. Invalid input will be store in invalid_input list
    input_morse, invalid_input = input_validation_function(input_morse)

    # Re print valid & invalid input separately.
    if invalid_input:
        print("Invalid input:", str(invalid_input)[1:-1])
        print("Valid input:", str(input_morse)[1:-1])
else:
    print("The input is either incorrect or blank!")
