import random

class Dice:
    def __init__(self):
        self.state = [1, 1, 1, 1, 1]
        self.sides = 6

    ######## Rolls Dice ##########
    def roll(self, positions):

        # start of round roll
        if positions == "all":
            for die in self.state:
                for new in range(5):
                    self.state[int(new) - 1] = random.randint(1, 6)
                return self.state

        # changes dice in list as needed
        for pos in positions:
            self.state[int(pos) - 1] = random.randint(1, 6)

    ######## gets dice state #####
    def getState(self):
        return self.state

    ####### determines hand ##########
    def score(self):

        # keeps track of roll
        Hand = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for keys in self.state:
            Hand[keys] += 1

        # assigns winning hands
        values = list(Hand.values())
        if 5 in values:
            handName = "five of a kind"
            handScore = 30

        elif 4 in values:
            handName = "four of a kind"
            handScore = 15

        elif 3 in values and 2 in values:
            handName = "full house"
            handScore = 12

        elif 3 in values:
            handName = "three of a kind"
            handScore = 8

        elif values.count(2) == 2:
            handName = "two pairs"
            handScore = 5

        elif values.count(1) == 5 and (Hand[1] == 0 or Hand[6] == 0):
            handName = "straight"
            handScore = 20

        else:
            handName = "Bad Hand"
            handScore = 0

        return handName, handScore
