import random
import turtle

scr = turtle.Screen()
trt = turtle.Turtle()

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class Organism:
    name = ''
    type = ''
    speed = ''
    level = ''
    size = ''
    cooperation = ''
    fitness = ''
    lifespan = ''
    herding = ''

    def description(self):
        desc_str = "Name:{}\n Typ:{} Spd:{} Lvl:{}\n Sz:{} Coop:{} Fit:{}\n Lspn:{} Hrd:{}\n".format(self.name,
                                                                                                     self.type,
                                                                                                     self.speed,
                                                                                                     self.level,
                                                                                                     self.size,
                                                                                                     self.cooperation,
                                                                                                     self.fitness,
                                                                                                     self.lifespan,
                                                                                                     self.herding)
        return desc_str


for repetitions in range(0, 10):
    bugcatcher = []
    empty_name_list = []
    namelist = []
    for alphalooper in range(0, 3):
        item_picker = random.randrange(0, len(alphabet_list))
        empty_name_list.append(alphabet_list[item_picker])
    empty_name_list.append('-')
    for i in range(0, 3):
        item_picker = random.randrange(0, len(number_list))
        empty_name_list.append(number_list[item_picker])
    namelist.append(''.join(empty_name_list))
    # print("".join(empty_name_list))
    orgname = namelist
    orgtype = random.randrange(-2, 2)
    orgspeed = random.randrange(0, 2)
    orglevel = random.randrange(0, 2)
    orgsize = random.randrange(0, 3)
    orgcoop = random.randrange(-2, 2)
    orgfitness = random.randrange(1, 5)
    orglifespan = 1000
    orgherding = random.randrange(-2, 2)
    bug01 = Organism()
    bug01.name = orgname
    bug01.type = orgtype
    bug01.speed = orgspeed
    bug01.level = orglevel
    bug01.size = orgsize
    bug01.cooperation = orgcoop
    bug01.fitness = orgfitness
    bug01.lifespan = orglifespan
    bug01.herding = orgherding
    print(bug01.description())
    bugcatcher.append(bug01.name)
print(type(bug01))
print(bugcatcher)

scr.mainloop()
