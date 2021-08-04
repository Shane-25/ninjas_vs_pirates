from character import Character


class Pirate(Character):

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_health( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , target ):
        print(self.name, "pirate attack", target.name, "for", self.strength, "\n")
        target.health -= self.strength
        if target.if_dead():
            print(target.if_dead(), "\n")
        return self

    def cannon_attack( self, target):
        print(self.name, "pirate cannon attack", target.name, "for", self.strength , "\n")
        target.health -= self.strength
        if target.if_dead():
            print(target.if_dead(), "\n")
            target.respawn()
        return self

