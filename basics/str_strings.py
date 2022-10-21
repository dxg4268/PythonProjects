"""
String ==> sequence of characters enclosed 
        in single or double quotes.

STRINGS ARE ARRAYS

'hello' is equivalent to "hello"

"""

s1,s2 = 'h', "h"
s1 == s2 # returns true

"""
* ASSIGNMENT OF STRING TO VARIABLE

        variable_name = " a string "

* MULTILINE STRINGS ==> enclosed in '''<sting>'''

* There is no Character datatype

* Indexing can be used to access elements of string

* Slicing is used to return a substring of a string


"""



a = "Hello World"               #creating a test string

# === Indexing and Slicing ===

char = a[4]             # character at 4 index
substring1 = a[2:5]     # sample output : llo
str2 = a[2:]            # from starting index till the end
str3 = a[:6]            # from beginning upto stopping index (stop not included)
str4 = a[2:5:2]         # adding a step value (jumping)
str5 = a[-1:-5:-1]      # negative indexing works
str6 = a[::-1]          # trick to reverse a string


# === Modifing Strings ===

""" 
Note : string method return new values, 
it does not change the actual string
"""

upper_case_func = "hello".upper() #converts all alpha to upper case
lower_case_func = "HELLO".lower() # converts to lowercase

strip_func = a.strip() #removing trailing and leading whitespace
replace_func = a.replace('to be replaced', 'replace value') #replace string with given string
split_func = a.split('separator') #splits string into substrings and returns a list
title_func = a.title() # converts first letter of each word to upper case

startswith_func = a.startswith() # returns a boolean value
endswith_func = a.endswith() # returns a boolean value

partition_func = a.partition('args') #returns a tuple where string is divided into 3 parts.
count_func = a.count('args') #returns frequency of occurence of a given substring in the string.



# === String formating ===

'''
We can combine strings and numbers using
format() method

We can use indexes to place the argumant
'''

age = 16
name = "Tony"

formatted_string = "My name is {} of age {}.".format(name, age)



