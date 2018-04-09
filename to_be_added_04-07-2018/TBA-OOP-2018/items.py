class Items():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue:  {}\n".format(self.name, self.description, self.value)


class Room(Items):
    def __init__(self, value):
        self.value = value
        super().__init__(name="Room", description="A room of some kind", value=self.value)


class Weapons(Items):
    def __init__(self, name, description, damage, defense):
        self.damage = damage
        self.defense = defense
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue:  {}\nDamage: {} Defense:{}".format(self.name, self.description, self.value)
