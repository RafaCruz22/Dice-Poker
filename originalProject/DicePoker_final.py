import random
import copy


class DicePoker:
    def __init__(self):
        self.money = 100
        self.initialMoney = 100
        self.dice = Dice()
        self.UI = UserInterface()
        self.costToPlay = 10

    ########## increase money #########
    def increaseMoney(self, val):
        self.money += val

    ######## decrease money ##########
    def decreaseMoney(self, val):
        self.money -= val

    ###### gets money ##########
    def getMoney(self):
        return self.money

    ######## starts round #########
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
            enhance = self.UI.enhanceQuestion()

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

                    # print the final hand rolled
                    self.UI.otherMSG("final hand")
                    hand = str(self.dice.getState())
                    print(hand.center(60))

                    # print the hand name
                    print((self.dice.score()[0]).center(60).title())

                    # displays winnings
                    self.UI.displayMoney(self.dice.score()[1], time="won")

                    # prints end of round amount to screen
                    self.UI.displayMoney(self.money, time="end round")

            # handles player not wanting to roll either reroll
            elif enhance == False or reRolls == 2:
                if reRolls == 2:

                    # print final hand rolled
                    self.UI.otherMSG("final hand")
                    hand = str(self.dice.getState())
                    print(hand.center(60))
                    print((self.dice.score()[0]).center(60).title())

                    # displays winnings
                    self.UI.displayMoney(self.dice.score()[1], time="won")

                    # take care of winnings here
                    score = self.dice.score()[1]
                    self.money += score

                    # prints end of round amount to screen
                    self.UI.displayMoney(self.money, time="end round")

                else:
                    continue

    ######## Starts Game ########
    def playGame(self):

        # start of game banner
        self.UI.printIntro("start of game")

        # print current amount to screen
        self.UI.displayMoney(self.money, time="start amount")

        while True:

            # Checks for invalid inputs and
            # starts game if player wants to play
            round = self.UI.newRoundQuestion()
            while True:

                if round == False:
                    self.UI.displayMoney(self.money, time="final amount")
                    return False

                elif round == True:
                    # only allows round if play has min $10
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
                response = self.UI.newGameQuestion()
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


class UserInterface:

    #########  Prints Intros  ###########
    def printIntro(self, intro):

        # start of round heading
        if intro == "startRound":
            print()
            roundMSG = "Start of Round"
            roundStyle = "-" * len(roundMSG)
            print(roundMSG.center(60) + "\n" + roundStyle.center(60))

        # intro to game (message to player)
        elif intro == "start of game":
            print()
            introMessage = "Welcome to Dice Poker"
            print(("_" * len(introMessage)).center(60))
            print()
            print(introMessage.center(60))
            print(("_" * len(introMessage)).center(60))
            print()
            welcomeMSG = (
                " ***************************************************************"
                + "\n *                                                             *"
                + "\n *    Game starts with $100. Each round costing $10 to play.   *"
                + "\n *     Every round allows the player two chances to enhance    *"
                + "\n *       their hand by rerolling any or all of the dices.      *"
                + "\n *      After the second enhancement your Final Hand will      *"
                + "\n *               possibly be a winning hand.                   *"
                + "\n *                                                             *"
                + "\n *                        Good luck!                           *"
                + "\n *              May the odds be in your favor.                 *"
                + "\n *                                                             *"
                + "\n ***************************************************************"
            )
            print(welcomeMSG.center(60))
            print()
            start = "Start of Game"
            print(("_" * len(start)).center(60))
            print()
            print(start.center(60))
            print(("_" * len(start)).center(60))

    def otherMSG(self, whichMSG):

        if whichMSG == "winning hand box":
            possibleWinHand = (
                "    **********************************************************"
                + "\n    *  Hand                                       Pay        *"
                + "\n    **********************************************************"
                + "\n    *                                                        *"
                + "\n    *  Two Pairs                                   $5        *"
                + "\n    *  Three of a Kind                             $8        *"
                + "\n    *  Full House                                 $12        *"
                + "\n    *  Four of a Kind                             $15        *"
                + "\n    *  Straight [1,2,3,4,5] or [2,3,4,5,6]        $20        *"
                + "\n    *  Five of a Kind                             $30        *"
                + "\n    *                                                        *"
                + "\n    **********************************************************"
            )
            print((possibleWinHand).center(60))
            print()

        # enhancement - rules
        elif whichMSG == "enhanceMSG":

            enhanceMSG = (
                "    **********************************************************"
                + "\n    *                                                        *"
                + "\n    *   You can enhance any of the 5 dice by inputing which  *"
                + "\n    *    dice you want enhanced with spaces in-between       *"
                + "\n    *               each number (1 - 5).                     *"
                + "\n    *                                                        *"
                + "\n    *               Example: 1 2 3 4 5                       *"
                + "\n    *                                                        *"
                + "\n    **********************************************************"
            )

            print((enhanceMSG).center(60))
            print()

        # enhancement - heading
        elif whichMSG == "enhancement":

            print()
            enhanceHeading = "- Enhancement -"
            print(enhanceHeading.center(60))

        # final hand - banner
        elif whichMSG == "final hand":
            print()
            rolledMSG = " * Final Hand * "
            line = "-" * len(rolledMSG)
            print(line.center(60))
            print(rolledMSG.center(60))
            print(line.center(60))

        # your broke message
        elif whichMSG == "broke":
            print()
            broke = "You do not have enough to play!"
            Funds = "$10 needed to play a round!"
            print(broke.center(60))
            print(Funds.center(60))

    #########  Prints Money  ############
    def displayMoney(self, money, time):

        # prints - start of game amount
        if time == "start amount":
            startAmount = "Start Amount : ${}".format(money)
            print()
            print(("-" * len(startAmount)).center(60))
            print(startAmount.center(60))
            print(("-" * len(startAmount)).center(60))

        # prints - current funds banner
        elif time == "current amount":
            currentAmount = "Current Amount: ${}".format(money)
            print()
            print(("-" * len(currentAmount)).center(60))
            print(currentAmount.center(60))
            print(("-" * len(currentAmount)).center(60))

        # prints - winning
        elif time == "won":
            print(("You won: ${}".format(money).center(60)))

        # prints - end of round winnings
        elif time == "end round":
            print()
            print(("End of round!").center(60))
            print((" End of round amount: ${}".format(money).center(60)))

        # prints - final amount
        elif time == "final amount":
            print()
            finalAmount = "Final Amount: ${}".format(money)
            thanks = "Thanks for playing"
            print(("_" * len(thanks)).center(60))
            print()
            print(finalAmount.center(60))
            print()
            print(thanks.center(60))
            print(("_" * len(thanks)).center(60))

    #########  Prints Dice ############
    def displayDice(self, dice, hand):

        # prints - starting hand
        if hand == "starting hand":
            newHand = "Starting hand: " + str(dice.getState())
            print(newHand.center(60))

        # prints - enhanced hand for both rolls
        elif hand == "new hand":
            print()
            newHand = "Enhanced Hand: " + str(dice.getState())
            print(newHand.center(60))

    #########  new round?  ############
    def newRoundQuestion(self):

        # Returns True to keep playing, False to stop
        response = (
            input("\n" + " " * 8 + "Do you want to play a round (Yes or No): ")
            .lower()
            .strip()
        )

        while True:
            if response == "yes":
                return True

            elif response == "no":
                return False

            else:
                print("Invalid Entry!".center(60))
                response = (
                    input("\n" + " " * 8 +
                          "Do you want to play a round (Yes or No): ")
                    .lower()
                    .strip()
                )

    #########  reroll?  ############
    def enhanceQuestion(self):

        # Returns True to keep playing, False to stop
        response = (
            input("\n" + " " * 8 + "Do you want to enhance your roll? (Yes or No): ")
            .lower()
            .strip()
        )
        # error checking - enhance question
        while True:

            if response == "yes":
                return True

            elif response == "no":
                return False

            else:
                print("Invalid Entry!".center(60))
                response = (
                    input(
                        "\n"
                        + " " * 8
                        + "Do you want to enhance your roll? (Yes or No): "
                    )
                    .lower()
                    .strip()
                )

    #######  reroll position?  ##########
    def enhancePositionQuestion(self):

        # message to player
        position = input(
            " " * 10 + "Which dice do you want to enhance? : ").strip()

        while True:
            userInput = "valid"
            try:
                for pos in position.strip().split(" "):

                    if len(position.strip()) > 9:
                        raise Exception

                    elif int(pos) > 5 or int(pos) == 0:
                        raise Exception
            except:
                userInput = "invalid"
                msg = "Invalid Entry!"
                print(msg.center(62))

            if userInput != "invalid":
                break

            print()
            position = input(
                " " * 10 + "Which dice do you want to enhance? : ").strip()

        return position

    ######## new game? #############
    def newGameQuestion(self):

        # Returns turn to play again, false to stop
        response = (
            input("\n" + " " * 8 + "Do you want to play a new game? (Yes or No): ")
            .lower()
            .strip()
        )
        while True:
            if response == "yes":
                return True

            elif response == "no":
                return False

            else:
                print("Invalid Entry!".center(60))
                response = (
                    input(
                        "\n" + " " * 8 +
                        "Do you want to play a new game? (Yes or No): "
                    )
                    .lower()
                    .strip()
                )


def main():

    Game = DicePoker()
    Game.playGame()


if __name__ == "__main__":
    main()
