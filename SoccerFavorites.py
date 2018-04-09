import random  # for list randomization

game_state = 1  # sets up my app loop
choices = 0  # will count the number of sorts that the user makes
print("")
team_list = ["Atlanta United", "Chicago Fire", "Colorado Rapids", "Columbus Crew",
             "D.C. United", "F.C. Dallas", "Sporting Kansas City", "L.A. Galaxy",
             "Minnesota United F.C.", "Montreal Impact", "New England Revolution",
             "N.Y.C.F.C.", "New York Red Bulls", "Orlando F.C.", "Philadelphia Union",
             "Portland Timbers", "Real Salt Lake", "San Jose Earthquakes", "Seattle Sounders",
             "Toronto F.C.", "Vancouver Whitecaps"]
random.shuffle(team_list)  # self explanatory
print ("Here is a randomized list of MLS teams")
for number_of_teams in range(0, len(team_list)):  # prints out team list in random
    print (number_of_teams + 1, team_list[number_of_teams])
print ("")
while game_state == 1:  # starts loop
    choices = choices + 1  # counts the number of user sorts
    spot01 = random.randrange(0, len(team_list))  # creates the first list index number
    spot02 = random.randrange(0, len(team_list))  # creates the second list index number
    holder01 = team_list[spot01]  # assigns index number to corresponding team on list
    holder02 = team_list[spot02]  # assigns index number to corresponding team on list

    print ("Out of these two teams - Which team do you like better?")
    my_ans = input("Enter (1) for " + (holder01) + "\nEnter (2) for " + (holder02) + "? \n(press escape to quit)")
    if my_ans == "1":  # user chooses first team
        team_list.remove(holder01)  # team is erased from the list
        spot01 = spot01 - 1  # variable is decremented by one
        if spot01 <= 0:
            spot01 = 0
        if spot01 >= 20:
            spot01 = 20
        if spot02 <= 0:
            spot02 = 0
        if spot02 >= 20:
            spot02 = 20
        team_list.insert(spot01, holder01)  # team is inserted back to list one spot higher
        print ("")
    elif my_ans == "2":  # does the opposite of the if statement
        team_list.remove(holder02)
        spot02 = spot02 - 1
        if spot01 <= 0:
            spot01 = 0
        if spot01 >= 20:
            spot01 = 20
        if spot02 <= 0:
            spot02 = 0
        if spot02 >= 20:
            spot02 = 20
        team_list.insert(spot02, holder02)
        print ("")
    else:  # loop escape
        my_ans == "E" or "e"
        break

print ("")
print ("you made a total of " + str(choices) + " choices")  # counts total moves
print ("Here are your results in order.")
for number_of_teams in range(0, len(team_list)):  # prints out team list in order from most upvoted to least
    print (number_of_teams + 1, team_list[number_of_teams])
