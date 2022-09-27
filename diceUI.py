# User Interface for dicepoker.
class UserInterface:

    #########  Banner for all messages ###########
    def banner(self, whichBanner, msg):

        if whichBanner == "complete": 
            print()
            print(("_" * 66 ).center(60))
            print()
            print(msg.center(60))
            print(("_" * 66 ).center(60))
            print()
        
        if whichBanner == "top":
            print()
            print(("_" * 66 ).center(60))
            print()
            print(msg.center(60))

        if whichBanner == "bottom":
            print(msg.center(60))
            print(("_" * 66 ).center(60))
            print()

        if whichBanner == "thin":
            print(("_" * 66 ).center(60))
            print()
            print(msg.center(60))
            print(("_" * 66 ).center(60))
            print()


    #########  Prints Intros  ###########
    def printIntro(self, intro):

        # intro to game (message to player)
        if intro == "start of game":
            introMessage = "Welcome to Dice Poker"
            self.banner("complete", introMessage)

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
            self.banner("top", start)

        # start of round heading
        if intro == "startRound":
            roundMSG = "Start of Round"
            self.banner("bottom", roundMSG)


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
                + "\n    *               Example: 5 4                             *"
                + "\n    *    The above example will enhance dice 4 & 5           *"
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
            rolledMSG = " ** Final Hand ** "
            self.banner("top", rolledMSG)
            print()

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
            startAmount = "Start Amount: ${}".format(money)
            self.banner("bottom", startAmount)

        # prints - current funds banner
        elif time == "current amount":
            currentAmount = "Current Amount: ${}".format(money)
            print()
            self.banner("top", currentAmount)

        # prints - winning
        elif time == "won":
            print(("You won: ${}".format(money).center(60)))

        # prints - end of round winnings
        elif time == "end round":
            endRound = "End of round!"
            endAmount = " End of round amount: ${}".format(money).center(60)
            self.banner("top", endRound)
            self.banner("bottom", endAmount)

        # prints - final amount
        elif time == "final amount":
            print()
            finalAmount = "Final Amount: ${}".format(money)
            thanks = "Thanks for playing"
            self.banner("top", finalAmount)
            self.banner("bottom", thanks)

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
    def userInput(self, whichUserMSG):
        # Returns True to keep playing, False to stop
        response = (
            input("\n" + " " * 8 + f"--> Do you want to {whichUserMSG}? (Yes or No): ")
            .lower()
            .strip()
        )

        while True:
            if response.lower() == "yes" or response.lower() == "y":
                return True

            elif response.lower() == "no" or response.lower() == "n":
                return False

            else:
                print("Invalid Entry!".center(60))
                response = (
                    input("\n" + " " * 8 +
                          "--> Do you want to {whichUserMSG} (Yes or No): ")
                    .lower()
                    .strip()
                )

    #######  reroll position?  ##########
    def enhancePositionQuestion(self):

        # message to player
        position = input(
            " " * 10 + "--> Which dice do you want to enhance? : ").strip()

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
                " " * 10 + "--> Which dice do you want to enhance? : ").strip()

        return position