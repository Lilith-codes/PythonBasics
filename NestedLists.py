Lilith = 24
print(Lilith)

_Sneha = 25
print(_Sneha)

__Sneha = 25
print(__Sneha)

___Virat = 28
print(___Virat)
# From the above code lines we can understand that placeholder value begins with an alphabet or an underscore but not with any special characters or numbers.



# print a statement

print("This is my first program on Pycharm console which is belong to a community edition with 2024 version.")

#Let's make a something different! Try to parse the entire statement into a variable and call it with a print function.

Note = "This is my first program on Pycharm console which is belong to a community edition with 2024 version."
print(Note)



## Slicing operations on data

a = 10
print(a)

#List
L = [12, 13, 14, 17, 19, 24, 46]
type(L)
print(type(L))

# Make a list of items with alpha numeric data and data types and a list inside

L1 = [67, "Naveen", 65.7, "Lilith11", "Sneha25", True, "Random shit", ["Chandan", 45.67, "KA PAUL", "Trump", 99999, "LLLL" ]]
# Perform Indexification operations
# call the items in the list through their indices with left to right order
print(L1[0])
print(L1[1])
print(L1[5])
print(L1[6])


# call the last items in a list with negative indices through right to left order
print(L1[-1])
print(L1[-2])

# call the list in a list and extract the items in it through their indices from right to left order
print(L1[-1][0])
print(L1[-1][3])
print(L1[-1][-1])
print(L1[-1][-3])


# Type 2 method # Calling the elements in start, end, step method.

L2 = [10, "SriKrishna Ji", 30.56, False, (4+7j), 6767, ["Aleena", 234, "Mishtu1013", 679.34, "USD", "KAMALA HARRIS" ]]
# set a range and list the items
print(L2[0:5])
# set a range and list the items with max range
print(L2[0:50])

# Calling the elements in start, end, step method.
# list the items in sequence by leaving 2 items and followed the next
print(L2[0:5:2])

# Calling the elements in start, end, step method.
# list the items in sequence by leaving 3 items and followed the next
print(L2[0:5:3])

print(L2[0:9:6])
# printing the sequence items in reverse order
print(L2[10:0:-1]) #This syntax will not print the last item in reverse order
print(L2[::-1]) # This syntax will print all the items in reverse order

# Question: How to print all the items in reverse sequence by excluding the nested list inside through range operation?
# Answer:  Make a syntax with range function and then iterate the items in nested list, so that selective sequence will be printed in reverse order by excluding the nested list

# printing the sequence items in reverse order by exceeding 2 numbers followed
L2 = [10, "SriKrishna Ji", 30.56, False, (4+7j), 6767, ["Aleena", 234, "Mishtu1013", 679.34, "USD", "KAMALA HARRIS" ]]
print(L2[100:0:-2])
#The items in the list are reversed,
# every 2nd item after pointed index is printed and the last remaining index is not printed
# which shows that if the last index list items equals to the threshold range i.e exceeding number then it is not printed.

print(L2[-2:100])
# Indexifying and calling the last 2 items in the list

# Hahah! Trying to call the last items of the list and indexifying to the last of the last
print(L2[-2:100:-1])
#The slice L2[-2:100:-1] is attempting to start from the second-to-last element and go to the 100th element in reverse order.
# However, since the ending index (100) is out of range and also greater than the starting index (-2), it won't produce any elements.


print(L2[-2::-1])
# Reverse the list excluding the last element and printing the items after the last second element to the beginning.

print(L2[0])
#printing the zero index.

print(L2[0:10:1])
#Start at index slice 0, Stop at index 10, step 1 index and print the data.

print(L2[::-1])
#Reverse the sequence, Start at nowhere, end at nowhere, step at -1(move towards reverse and print after 1 element)

print(L2[3:10:-1])
# Data not printable

print(L2[10:3:-1])
#Starting the index at 10, ends at 3 index, steps back reverse in direction by 1 element.
#Interestingly we found that if the index line direction is reverse then we should make sure to place the step value in negative.

print(L2[20:3:-2])
#Starting the index at 10, ends at 3 index, steps back reverse in direction by 2 element.



