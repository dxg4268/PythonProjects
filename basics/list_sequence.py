"""
List ==> ordered sequence of data of various data types
        It is a ARRAY
* USE :- to store multiple values (collection of data) in a 
        single variable

* created dusing square brackets

* elements are ordered (also indexed), mutable, allow duplicate values

* mutable : elements can be changed, removed, added etc.

* Length of list : 
                len('list1')

* check if item is present:
                'apple' in list_1

"""
# x = 4
# print("hello") if x%2==0 else print("false")

# many data of diff. types stored in one variable :)
example_list = ["apple" , 45.49 , { "key1" : 99 }, ('t1', 't2')]
list_2 = ["apple","red","green","pineapple"]

#creating a sample test list
list_1 = ["apple", "mango", "orange", "grapes", 12, 144, 6, 36]


# === Indexing and slicing ===

'''Indexing in list is used to access items'''

index_1 = list_1[4]         # accessing element at 4
neg_index = list_1[-1]        # start from the end

l1 = list_1[2:6]            # grab elements from index 2 upto index 6 (not including 6)

l2 = list_1[:5]             # grab from the beginning up to given ending index

l3 = list_1[2:]             # grab from given starting value till the very end



# === Modifing a list ===
'''
List are mutable :) 

* Note : .pop() method also returns the removed value
'''
alpha_list = ['a', 'x', 'z', 'A', 'b' , 'w']
num_list = [6,4,89,65,43,23,91,34,56,-4,-99]


list_1[2] = "pineapple"     # changing value of element at index 2
list_1[1:2] = ["blackcurrent", "vanilla"]   #inserting more items in place of one item, remaining items will move accordingly.

list_1.insert(4,'coconut')      # insert item at given index
list_1.append('strawberry')     # adding items at end of list
list_1.extend(example_list)     # appending elements from any sequence to current list

list_1.remove("grapes")         # removing specified element from list
list_1.pop(4)                   # removing element at given index or element present at last index
del list_1[5]                   # del keyword removes specified index
del example_list                # danger ! it deletes the entire list
list_2.clear()                  # empties the list, but the list remains wiht no content

alpha_list.sort()               # sort the list alphanumerically, in increasing order
num_list.sort( reverse = True )   # sort the list alphanumerically, in decreasing order

list_1.reverse()                # reversing the list not in increasing or decreasing order

copied_list = list_1.copy()     # copy a list to a new list

''' list1 = list2  (something unexpected)
    does not create a copy but a reference
    any change to original list will be reflected in another list
'''

# === List Comprehension ===

''' List Comprehension docs

* Shorter syntax to create a new list 
  based on values of another list

* List comprehensions are unique way of quickly creating a 
  list with python

* Great alternative to using for loop with .append() 
  method to create list

Syntax: 
        newList = [expression for item in iterable if condition == true]


* old list remain unchanges

* condition is filter to accept items that evalute to True

* condition is optional

* iterable can be any array (iterable object)

* range() to create iterable

* we can manipulate the expression part
'''

list_1 = [1,2,3,4,5,6,7,8,9,10]

new_list = [x for x in list_1 if x % 2 == 0 ]       # creating a new list of element 'x' if 'x' is even

#otherwise, for loop method
new_list = []
for x in list_1:
    if x % 2 == 0:
        new_list.append(x)











