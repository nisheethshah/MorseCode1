# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 22/03/2018
# Last Modified Date: 25/03/2018
# Assignment 1: Task 1: Building a Dictionary of Morse Code
# -----------------------------------------------------------------------------

# I've created an Excel file with Morse Code key & values.
# We'll pull dictionary data from that Excel file.
# So I'll import that file into here as below -
import xlrd
# import pprint     # "pprint" library helps to print dictionary in vertical format

# Creating a variable that can hold the Excel data. "xlrd.open_workbook" is used to fetch the Excel data.
workbook = xlrd.open_workbook("Data.xlsx")

# We'll save the keys & values in a list from Excel file first sheet(means '0').
# For keys, we'll fetch data from first row  onwards in first column i.e programmatically it means row 0, column 0.
# & for values, we'll fetch data from row 0 onwards in column 1 (i.e. first row onwards in second column).
key_list = workbook.sheet_by_index(0).col_values(0, 0)
val_list = workbook.sheet_by_index(0).col_values(1, 0)

# Passing the pair of keys & values in the dictionary
dictionary = {str(a).replace(".0", ""): b for a, b in zip(key_list, val_list)}

# Showing the dictionary as per Task 1
for key, value in dictionary.items():
    print(key, ":", value)

# Showing the dictionary as per Task 1
# "pprint" from "pprint" library helps to print dictionary in vertical format. Hence, it is more readable.
# pprint.pprint(dictionary)


