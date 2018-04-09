import random

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
namelist = []

for repetitions in range(0, 100):
    empty_name_list = []
    for alphalooper in range(0, 3):
        item_picker = random.randrange(0, len(alphabet_list[0:5]))
        empty_name_list.append(alphabet_list[item_picker])
    empty_name_list.append('-')
    for i in range(0, 3):
        item_picker = random.randrange(0, len(number_list))
        empty_name_list.append(number_list[item_picker])
    print("".join(empty_name_list))
    namelist.append(''.join(empty_name_list))
print(namelist)
