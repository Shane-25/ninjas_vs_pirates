class Character:

    def __init__(self, name, strength, speed, health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_health(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def enter_arena(self):
        print(self.name, " is entering Arena...", "\n")
        return self

    def if_dead(target):
        if target.health <= 0:
            return target.name, "is already dead"

    def respawn(self):
        if self.health <= 0:
            self.health = 100
            print(self.name, "was respawned")
        else:
            print(self.name, "this character is still alive")
            return self
    
    def regain_health(self):
        if self.health == 100:
            print(self.name, "this character is already alive")
        elif self.health + 20 >= 100:
            self.health = 100
            print(self.name, " has been healed to", 100)
        else:
            self.health += 20
            print(self.name, "has been healed")
        return self 
