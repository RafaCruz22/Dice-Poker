import copy
import diceUI
import dice

class DicePoker():
    def __init__(self):
        self.money = 100
        self.initialMoney = 100
        self.dice = dice.Dice()
        self.UI = diceUI.UserInterface()
        self.costToPlay = 10

    ########## Increase Money #########
    def increaseMoney(self, val):
        self.money += val

    ######## Decrease Money ##########
    def decreaseMoney(self, val):
        self.money -= val

    ###### Gets Money ##########
    def getMoney(self):
        return self.money

    ######## Starts Round #########
    def playRound(self):

        # subtracts $10 from current amount
        self.money -= self.costToPlay

        # print current amount to screen
        self.UI.displayMoney(self.money, time="current amount")

        # prints intro - start of round
        self.UI.printIntro("startRound")

        # prints - possible winning hands
        self.UI.otherMSG("winning hand box")

        # start of round roll
        self.dice.roll("all")
        self.UI.displayDice(self.dice, hand="starting hand")

        # handles enhancement
        for reRolls in range(1, 3):

            # ask user if they want to enhance
            enhance = self.UI.userInput("ehance roll")

            # if player wants to roll, then ask for position
            if enhance == True:

                # prints - rules to enhancement
                self.UI.otherMSG("enhanceMSG")

                # ask user which dice to enhance with Error checking
                positionEnhance = self.UI.enhancePositionQuestion()

                # enhancement heading with round number
                self.UI.otherMSG("enhancement")
                print((str(reRolls)).center(60))

                # rolls position and displays pervious and new
                # values to the dice that is being rolled
                oldHand = copy.deepcopy(self.dice.getState())
                positionEnhance = positionEnhance.split(" ")
                self.dice.roll(positionEnhance)
                for pos in positionEnhance:
                    print()
                    diceRolledMSG = (
                        "Dice "
                        + str(pos)
                        + ": Previously "
                        + str(oldHand[int(pos) - 1])
                        + " is now "
                        + str(self.dice.getState()[int(pos) - 1])
                        + "."
                    )
                    print(diceRolledMSG.center(60))

                # displays hand
                self.UI.displayDice(self.dice, hand="new hand")

                # checks if it is the last round of rolls
                if reRolls == 2:

                    # takes care of winnings
                    score = self.dice.score()[1]
                    self.money += score

                    # process the hand and prints proper output
                    self.processHand()

                    # prints end of round amount to screen
                    self.UI.displayMoney(self.money, time="end round")

            # handles player not wanting to roll either reroll
            elif enhance == False or reRolls == 2:
                if reRolls == 2:
                    
                    # process the hand and prints proper output
                    self.processHand()

                    # take care of winnings here
                    score = self.dice.score()[1]
                    self.money += score

                    # prints end of round amount to screen
                    self.UI.displayMoney(self.money, time="end round")

                else:
                    continue

    def processHand(self): 
        # print the final hand rolled
        self.UI.otherMSG("final hand")
        hand = str(self.dice.getState())
        print(hand.center(60))
        print()

        # print the hand name
        print((self.dice.score()[0]).center(60).title())

        # displays winnings
        self.UI.displayMoney(self.dice.score()[1], time="won")
        

    ######## Starts Game ########
    def playGame(self):

        # start of game banner
        self.UI.printIntro("start of game")

        # print current amount to screen
        self.UI.displayMoney(self.money, time="start amount")

        while True:

            # Checks for invalid inputs and
            # starts game if player wants to play
            round = self.UI.userInput("play a round") 
            while True:

                if round == False:
                    self.UI.displayMoney(self.money, time="final amount")
                    return False

                elif round == True:
                    # only allows round if player has min $10
                    if self.money >= self.costToPlay:
                        self.playRound()
                    break

            # checks if player has enough money to play the round
            if self.money < self.costToPlay:
                print()
                self.UI.displayMoney(self.money, time="current amount")
                self.UI.otherMSG("broke")

                # asks player if they want to play
                # a new
                response = self.UI.userInput("start a new game")
                while True:

                    if response == True:
                        self.money = self.initialMoney
                        print()
                        print("Amount reset.".center(60))
                        print("$100".center(60))
                        break

                    elif response == False:
                        self.UI.displayMoney(self.money, time="final amount")
                        return False

def main():

    Game = DicePoker()
    Game.playGame()

if __name__ == "__main__":
    main()

