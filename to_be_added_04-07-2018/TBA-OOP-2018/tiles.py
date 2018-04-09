class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


class StartingRoom(MapTile):
    def intro_text(self):
        return 'you find yourself etced to death'

    def modify_player(self, player):
        # room has no actions
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, items):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining".format(self.enemy.damage, the_player.hp))


'''
    if myxandy == (-4, -4):
        print("there is a giant waterfall here cascading into darkness")
    if myxandy == (-3, -4):
        print("you are in a room with a wet floor, you hear thundering water to the west, a door is on the south wall")
    if myxandy == (-2, -4):
        print("you are standing at -2,-4")
    if myxandy == (-1, -4):
        print("you are standing at -1, -4")
    if myxandy == (0, -4):
        print("you are standing at 0, -4")
    if myxandy == (1, -4):
        print("you are standing at 1,-4")
    if myxandy == (2, -4):
        print("you are standing at 2,-4")
    if myxandy == (3, -4):
        print("you are standing at 3,-4")

    if myxandy == (-4, -3):
        print("you are standing at -4,-3")
    if myxandy == (-1, -3):
        print("you are standing at -1, -3")
    if myxandy == (1, -3):
        print("you are standing at 1, -3")

    if myxandy == (-4, -2):
        print("you are standing at -4, -2")
    if myxandy == (-3, -2):
        print("you are standing at -3, -2")
    if myxandy == (-2, -2):
        print("you are standing at -2, -2")
    if myxandy == (-1, -2):
        print("you are standing at -1, -2")
    if myxandy == (1, -2):
        print("you are standing at 1, -2")
    if myxandy == (3, -2):
        print("you are standing at 3, -2")
    if myxandy == (4, -2):
        print("you are standing at 4, -2")

    if myxandy == (-4, -1):
        print("you are standing at -4, -1")
    if myxandy == (-2, -1):
        print("you are standing at -2, -1")
    if myxandy == (1, -1):
        print("you are standing at 1, -1")
    if myxandy == (2, -1):
        print("you are standing at 2, -1")
    if myxandy == (3, -1):
        print("you are standing at 3, -1")

    if myxandy == (-3, 0):
        print("you are standing at -3, 0")
    if myxandy == (-2, 0):
        print("you are standing at -2, 0")
    if myxandy == (-1, 0):
        print("you are standing at -1, 0")
    if myxandy == (0, 0):
        print("You are standing in a room with a door on the north wall and a door on the west.")
        print("There is a pocket knife here.")

    if myxandy == (1, 0):
        print("you are standing at 1, 0")
    if myxandy == (3, 0):
        print("you are standing at 3, 0")

    if myxandy == (-2, 1):
        print("you are standing at -2, 1")
    if myxandy == (0, 1):
        print("you are standing in a hallway that stretches out to the north and south")
    if myxandy == (2, 1):
        print("you are standing at 2, 1")
    if myxandy == (3, 1):
        print("you are standing at 3, 1")
    if myxandy == (4, 1):
        print("you are standing at 4, 1")

    if myxandy == (-2, 2):
        print("you are standing at -2, 2")
    if myxandy == (0, 2):
        print("you are standing in front of a door marked 'long hallway'")
    if myxandy == (3, 2):
        print("you are standing at 3, 2")

    if myxandy == (-3, 3):
        print("you are standing at -3,3")
    if myxandy == (-2, 3):
        print("you are standing at -2,3")
    if myxandy == (-1, 3):
        print("you are in a room, there is a locked door on the north wall")
    if myxandy == (0, 3):
        print("you are standing at the intersection of hallways heading off to the west, east, and south")
    if myxandy == (1, 3):
        print("you are standing at 1,3")
    if myxandy == (2, 3):
        print("you are standing at 2,3")
    if myxandy == (3, 3):
        print("you are standing at 3,3")
    if myxandy == (4, 3):
        print("you are standing at 4,3")

    if myxandy == (-4, 4):
        print("you are standing at -4,4")
    if myxandy == (-3, 4):
        print("you are standing at -3,4")
    if myxandy == (-1, 4):
        print("you are standing at -1, 4")
    if myxandy == (1, 4):
        print("you are standing at 1,4")
    if myxandy == (3, 4):
        print("you are standing at 3,4")


'''
