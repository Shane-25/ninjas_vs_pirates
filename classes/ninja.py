from character import Character


class Ninja(Character):

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_health( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , target ):
        print(self.name, "ninja attack", target.name, "for", self.strength, "\n")
        target.health -= self.strength
        if target.if_dead():
            print(target.if_dead(), "\n")
        return self

    def special_attack( self , target ):
        print(self.name, "ninja special attack", target.name, "for", self.strength, "\n")
        target.health -= self.strength * 10
        if target.if_dead():
            print(target.if_dead(), "\n")
        return self