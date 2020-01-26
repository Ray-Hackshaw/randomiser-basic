#Song randomiser - shuffler

from random import randint
import math


#Reads input from file, stores it into lines and splits by new line into new list.
list_input = open("artists.txt", "r")
lines = list_input.read()
list_input.close()
lines_list = str(lines).split("\n")
#Filters through results until a valid list is reconstructed.
valid_list = []
for i in lines_list:
    if len(i) <= 0:
        break
    else:
        valid_list.append(i)
#Generate random number within range of elements in the list.
range_val = len(valid_list)
ran_numb = randint(0, range_val - 1)

print("Your random artist of the day is: " + str(valid_list[ran_numb]))
