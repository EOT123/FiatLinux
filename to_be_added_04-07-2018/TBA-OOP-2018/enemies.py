class Enemy():
    def __init__(self, name, hp, damage, defense):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2, defense=4)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=14, damage=4, defense=0)
