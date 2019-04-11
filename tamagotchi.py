import random
class Tamagotchi:
    boredom_level = 5
    hunger_level = 10
    boredom_lower = 4
    hunger_lower = 6

    def __init__(self, name):
        self.name = name
        self.words = ["Mmmrp", "Hrrp"]
        self.ifBored = 0
        self.ifHungry = 0

    def clock(self):
        self.ifBored += 1
        self.ifHungry += 1

    def humor(self):
        if self.ifBored < self.boredom_level:
            return "Im Bored"
        if self.ifHungry < self.hunger_level:
            return "Im Hungry"

    def __str__(self):
        self.clock()
        return "Hey, Im {} and I feel {}".format(self.name, self.humor())

    def lower_hunger(self):
        self.ifHungry -= self.hunger_lower
        if (self.ifHungry < 0):
            self.hunger_level = 0

    def lower_boredom(self):
        self.ifBored -= self.boredom_lower
        if(self.boredom_level < 0):
            self.boredom_level = 0

    def SayHi(self):
        self.clock()
        self.lower_boredom()
        return "{} says {}".format(self.name, random.choice(self.slowa))

    def teachMe(self, word):
        self.words.append(word)
        self.lower_boredom()
        self.clock()

    def feed(self):
        self.lower_hunger()
        self.clock()


