import random

possible_elements = [0, 1, 2]  # this will substitute for two, other, and, empty

total_list = []  # Will capture 1000 random mini lists (probably should grab all possible combos)
for i in range(1, 1000):
    new_list = []  # made specifically to grab randoms four at a time
    for j in range(0, 4):
        x = random.randrange(0, 3)
        new_list.append(possible_elements[x])  # mini list grabbing 4 things
    total_list.append(new_list)  # big lists grabbing little lists

print ("this is total list before eliminating duplicates and sorting" + str(
    total_list))  # what it looks like before sorting and eliminating duplicates
print("")
new_list = list()  # This I don't get because it looks like I am setting a variable to a function???
for sublist in total_list:  # makes a new list and only adds stuff once - I read that this is verbose and inefficient but it works so I don't care.
    if sublist not in new_list:
        new_list.append(sublist)
new_list.sort()  # now that they are back to lists and eliminated of all duplicates - here they are sorted.

print(new_list)
print(len(new_list))
