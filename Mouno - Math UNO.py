#Name: Anushka Yadav and Udisha Gunawardena
#Date: June 18th 2023
#File Name: Mouna - Math UNO.py
#Descrption: The following file contains a modified verion of the game Uno, called "Mouno". 
#Test Cases: In the Test Cases File

import random

#Process- Define burn pile function; no parameters passed
def get_burnpile():

    #Process- Intlzise list to store results from burn pile
    burnPiledeck = []

    #Process- Intilzie while loop goal is to generate 36 cards for brun pile without spescial characters

    while len(burnPiledeck) < 32:

        #Process- Create number generated cards
        while len(burnPiledeck) != 28:
            #Process- Create random method to generate colour (r,g,b,y)
            colour = random.choice("RGYB")

            #Process- Create random method to generate number for each card; card 0-9 inclusive
            #Note- To address duplicate we compare list of burn pile and respective other piles
            numberValue = random.randint(0, 9)

            #Process- Create finial card which will be stored in list through string concatination
            cardCreator = colour + str(numberValue)

            #Process- If satement will run if the card is in the burn pile deck
            if cardCreator in burnPiledeck:

                #Process- Count how many reptions of the respective card is in the burn pile
                #Process- Utlize method .count()
                repeats = burnPiledeck.count(cardCreator)

                #Process- If duplicates means 3 do not append card; or the number is 0
                if repeats != 3 or cardCreator[1] != 0:
                    #Process- Can add card to list as there is no duplicates
                    burnPiledeck.append(cardCreator)

            #Process- Add cards with no duplicates into list
            else:
                burnPiledeck.append(cardCreator)

        #Process- Create special cards
        for x in range(4):

            #Process- R(Red) G(Green) B(Blue) Y(Yellow) C(Mix)
            specialColourcard = random.choice("RYGBC")

            #Process - Create +2 or +4 cards
            #Process- specify range between 3-4 will get differenct plus values
            plusCard = random.randrange(2, 4)

            #Process- if stament will run if generates +2 or + 4  card
            if plusCard == 2 and specialColourcard == "C":
                #Process- Will create new card with  + 2
                cardCreator = "+" + str(plusCard)

            #Process- Else generate colour switch card
            elif specialColourcard == "C":

                #Process- will create block card
                cardCreator = specialColourcard + "C"

            #Process- Else stament will run allowing user to generate block colur card
            else:

                cardCreator = specialColourcard + "Block"

            #Process- add generated card to burn pile list
            burnPiledeck.append(cardCreator)


    #Process- Intilizse storgae for burn deck
    sortBurnlist = burnPiledeck[:]

    #Process- Intlize index holder, place will insert will take place
    indexHolder = 5

    #Process- Intilize index access which will hold what index value will be used to access card
    indexaccess = 1

    #Process- For loop will run three times to best shuffle cards
    for i in range(3):
        sortBurnlist.insert(indexHolder, burnPiledeck[indexaccess])

        #Process- Remove used card from orginal list
        sortBurnlist.remove(burnPiledeck[indexaccess])

        #Process- Add 5 to index holder
        indexHolder += 5

        #Process- Add 1 to index access
        indexaccess += 1

    #Process- Reutrn burn plie to fucntion
    return sortBurnlist


#Process- Pass burn deck as a parameter, as this function will genereate the users deck
def get_user_cards(BurnPile):

    #Process- Intlize list for user card list
    userCardList = []

    #Process- While loop will run until the length of the users card is equal to 5
    while len(userCardList) < 5:

        #Process- Call final card function, and use final card variable to store results
        finalCard = gene_card()

        #Process-  If stament will rungenerated card already in bunr pile dekc
        if finalCard in BurnPile:

            #Process- Count how many times such a card repeats
            repeats = BurnPile.count(finalCard)

            #Process- Card will be added to the list if the number of repeats is less than or equal to 2
            if repeats <= 2:

                #Crocess- Add card to the deck
                userCardList.append(finalCard)

        #Process- Else condtion will run if card is not in the deck
        else:

            #Process- Add card to the list
            userCardList.append(finalCard)

    #Process- Call special list function, use a holder to store returned value
    specialUser = two_special_cards()

    #Process- Add special user list to user card list
    userCardList = specialUser + userCardList

    #Process - Returning list to the main program
    return userCardList


#Process- Create function that will generate two special cards
def two_special_cards():

    #Process- Define special list
    specialList = []

    #Process- Dor loop will run twice to generate special card
    for x in range(2):

        #Process- Through random see what type of card has been accesd
        cardType = random.randint(1, 3)

        #Process- If stamnet will run if card type is 1
        if cardType == 1:

            #Process- Add +2 card to list
            specialList.append("+2")

        #Process- If stamnet will run if card type is 2
        elif cardType == 2:

            #Process- Randomly pick the colour of the card
            colour = random.choice("RGBY")

            #Process- Create block card
            finalBlockCard = colour + "Block"

            #Process- Add block card to list
            specialList.append(finalBlockCard)

        #Process- Else condtion will run if cardtype does not agree to the top two choices
        else:
            #Process- Add CC card to list
            specialList.append("CC")

    #Process- Return special list
    return specialList

#Process- Fucntion will generate playable card
def gene_card():
    
    #Process- Randomly select the colour of the card
    colour = random.choice("RGBY")

    #Process- Randomly select the number of the card
    number = random.randint(0, 9)

    #Process- Generate the final card
    finalCard = colour + str(number)

    #Process- Return final card to the function
    return finalCard

#Process- Define function that will genertae computer deck, pass burn pile as well as user pile
def get_computer_cards(BurnPile, UserCards):

    #Process- Intlize computer card deck
    computerCardList = []

    #Process- While loop will run until the length of the users card is equal to 5
    while len(computerCardList) < 5:

        #Process- Call final card function, and use final card variable to store results
        finalCard = gene_card()

        #Process- See if final card generate in burn pile or user pile
        if finalCard in BurnPile or finalCard in UserCards:

            #Process- See how many times generated card in burn deck
            BrunRepeats = BurnPile.count(finalCard)

            #Process- See how many times generated card in burn deck
            UserRepeats = UserCards.count(finalCard)

            #Process- Card will be added to the list if the number of repeats is less than or equal to 2
            if BrunRepeats <= 2 and UserRepeats <= 2:

                #Process- Add final card into comp deck
                computerCardList.append(finalCard)

        #Process- Alse stament will run
        else:
            #Process- add final card into comp deck
            computerCardList.append(finalCard)

    #Process- call special list function, use a holder to store returned value
    compSpeical = two_special_cards()

    #Process- Add special user list to user card list
    computerCardList = compSpeical + computerCardList

    # Output/Returning - Returning list to the main program
    return computerCardList

#Process - Define colour switch function which will be involked if the card puts down CC
def colourSwitch(updatedComputerDeck):

    #Process - Intialize counter for each possible color card in the computers deck 
    redCount = 0
    blueCount = 0
    yellowCount = 0
    greenCount = 0

    #Process - Intialize empty string to hold the final colour that the computer will choose based on which color cards it has more of
    colourResult = ""

    #Process - For loop to go through every card in the computer card deck 
    for x in range(len(updatedComputerDeck)):

        #Process - If "R" is in the computer card, add to Red counter 
        if "R" in updatedComputerDeck[x]:
            redCount += 1

        #Process - If "G" is in the computer card, add to Green counter 
        elif "G" in updatedComputerDeck[x]:
            greenCount += 1

        #Process - If "B" is in the computer card, add to Blue counter
        elif "B" in updatedComputerDeck[x]:
            blueCount += 1

        #Process - Else, If "Y" is in the computer card, add to Yellow counter
        else:
            if "Y" in updatedComputerDeck[x]:
                yellowCount += 1

    #Process - Add each of the counters to a list 
    colourCorrect = [redCount, blueCount, yellowCount, greenCount]

    #Process - Use the max function to find the maximum between the 4 counters
    maxcolOcuurance = max(colourCorrect)

    #Process - While loop - While colourResult is an empty string 
    while colourResult == "":

        #Process - For loop to go through every item in color correct list
        for i in range(len(colourCorrect)):

            #Process - If color counter from colour correct list == maximum
            if colourCorrect[i] == maxcolOcuurance:

                #Process - If index of colour correct list == 0: 
                if i == 0:
                    #Process - Assing "R" to colour result
                    colourResult = "R"
                    
                #Process - Elif index of colour correct list == 1: 
                elif i == 1:
                    #Process - Assing "B" to colour result
                    colourResult = "B"
                    
                #Process - Elif index of colour correct list == 2: 
                elif i == 2:
                    #Process - Assing "Y" to colo9r result
                    colourResult = "Y"
                #Process - Elif index of colour correct list == 2: 
                else:
                    #Process - Assing "G" to colour result
                    colourResult = "G"
                    
    #Process - Return colour result to main program 
    return colourResult

#Process - Define comparing computer deck function which will decide which card should be put down (AI)
def comparing_computer_deck(computerdeck, middleCard, userdeck,colourUsed):
    
    #Process - Color Counter and List for cards matching the colour of the middle card
    colorCounter = 0
    colourCards = []

    #Process - Number Counter and List for cards matching the number of the middle card
    numCounter = 0
    numberCards = []

    # Process - Special card counter and list for any special cards in the deck (+2 and CC)
    specialCounter = 0
    specialCardList = []

    # Process - Counter for number of extra cards that cannot be used
    draw = 0

    # Process- Variable to hold the card value that they computer will put down
    playCard = ""

    #Process - Intialize boolean value for wether or not the computer needs to pick up a card
    compDrawResult = False

    #Process - Create a duplicate holder list for the computer deck
    newComputerdeck = computerdeck[:]

    #Process - Intialize string that will hold the colour the computer decides to switch to after a colour change
    colName = ""

    # Process - For every card in the computer deck:
    for x in range(len(computerdeck)):

        #Process- To access colour of computer deck
        firstColour = computerdeck[x]

        # Process - If middle card and computer card are the same: 
        if middleCard == computerdeck[x]:

            #Process - Update value of play card to middle as computer will put down the same card
            playCard = middleCard

            #Process - If playCard == Colour change: 
            if playCard == "CC":
                
                #Process - Call the colour switch function to see what colour the computer would like to switch to
                colName = colourSwitch(newComputerdeck)

        #Process - If the colour of the middle card is the same as computer card or colourUsed is equal to first card and colour used is not an empty string:
        elif middleCard[0] in firstColour[0] or (colourUsed == firstColour[0] and colourUsed != ""):

            #Process - Add card to colour card list and update the colour counter!
            colourCards.append(computerdeck[x])
            colorCounter += 1

        #Process - If the number of the middle card is the same as computer card:  
        elif middleCard[1] in computerdeck[x]:
            #Process - Add card to number card list and update the number counter!
            numberCards.append(computerdeck[x])
            numCounter += 1
    
        else:

            #Pocess - If computer card is a +4 or CC: 
            if computerdeck[x] == "+2" or computerdeck[x] == "CC":
                
                #Process - Add card to special card list and update special counter!
                specialCardList.append(computerdeck[x])
                specialCounter += 1

            #Process - If there is no match with colour, number or special cards, add to draw counter
            else:
                draw += 1

    #Process - If the playcard does not already have a value attached to it from above, run the following: 
    if playCard == "":


        #Process- If the users card <= 4 or (num counter and colour counter are 0) and comeputer has special card: 
        if (len(userdeck) <= 4 or (numCounter == 0 and colorCounter == 0)) and len(specialCardList) != 0:

            #Process - Randomly assign a special card value to playcard
            position = random.randint(0, (len(specialCardList) - 1) )
            playCard = specialCardList[position]
            
            #Process - If playCard == CC: 
            if playCard == "CC":
                #Process - Call the colour switch function to see what colour the computer would like to switch to
                colName = colourSwitch(newComputerdeck)

        #Process- Address all of the special cases
        elif (middleCard == "+2" or middleCard == "CC") and (numCounter != 0 and colorCounter != 0):

            #Process - If middle card == +2: 
            if middleCard == "+2":
                #Process - Randomly assign a colour card value to playcard
                position = random.randint(0, len(colourCards) - 1)
                playCard = newComputerdeck[position]

    
            else:
                #Process - For every value in the computer deck
                for x in range (len(newComputerdeck)):

                    #Process - Assing card value to the card from the loop
                    cardValue = newComputerdeck[x]
                    #Process - If colourUsed as in colour of card value
                    if colourUsed in cardValue[0]:
                        #Process - Play card == card value
                        playCard = cardValue
                        
                #Process - If Play card is an empty string, chnage computer draw result to true
                if playCard == "":
                    compDrawResult = True

        # Process-  If there are more similar colour cards then similar number cards
        elif colorCounter > numCounter:

            # Process- If the users card <= 4 and and the computer deck has a block card
            if len(userdeck) <= 4 and (middleCard[0] + "Block" in newComputerdeck):


                #Process- Assing playCard the value of the block card
                playCard = middleCard[0] + "Block"

            #Process- If there is any exeption, regarding the block or number of user cards
            else:

                #Process - Randomly assign a colour card value to playcard
                position = random.randint(0, len(colourCards) - 1)
                playCard = colourCards[position]

        #Process- If there are more similar number cards then similar colour cards or colour counter == number counter and colour and number counter are not 0:
        elif colorCounter < numCounter or ( colorCounter == numCounter and colorCounter != 0 and numCounter !=0 ):

            # Process- Randomly assign a number card value to playcard
            position = random.randint(0, len(numberCards) - 1) #(0,0-1)
            playCard = numberCards[position]

        else:
            #Process - If the unuseable card counter(draw) is equal to the lenght of the computer deck
            if draw == len(newComputerdeck):
                #Process - Update computer draw result to true
                compDrawResult = True

    #Process - Returning variables to the main program
    return playCard, compDrawResult, colName,newComputerdeck



#Process- Define get first card function that will allow you to get first card of deck
def get_firstCard(deck):

    #Process- Intlize start card value
    startCard = ""

    #Process- Intlize index position
    indexPos = 0

    #Process- While loop will run until the start card IS NOT a special card and once start card is estbalished while loop will terminate
    while startCard == "+2" or startCard == "CC" or ("Block" in startCard) or startCard == "":
        
        #Process- Access card through the list
        startCard = deck[indexPos]

        #Process- Add one to index postion
        indexPos += 1

    #Process- Return staring card to the function
    return startCard


#Process - Define math function, which will create the math eqaution for the user
def math_operation():

    #Process- Through random modeule one of the four opeartions will be selected
    operation = random.choice ("+-/*")

    #Process- Hold intgers generated in a list
    numList = []

    #Process- Gnerate the intgers being ultizied; four intgers will be generated through a for loop
    for i in range (4):

        #Process- Randomly generate intgers between 1- 10 inclusive
        numberGenerated = random.randint(1,10)

        #Process- Add randomly generated number to a list
        numList.append(numberGenerated)


    #Process- To ensure proper answer is being returned we set both answers as strings
    #Process- Correct answer will change its data type to int

    #Process- Intilize first rounded answer
    roundedAnswer = ""

    #Process- Intilize second rounded answer
    roundedAnswertwo = ""

    #Process- If statement will run if chosen operatin statisfies the first group; either operation selcted is + or /
    if operation == "+" or operation == "/":

        #Output- Output structure of equation to user; list will be outputted to user, so user can sub in numbers accordnilgy
        generateEquation = print("The format of this equation is", "\n", "(numList[0] + numList[3]) / (numList[1] + numList [2])")

        #Process- Cariable will hold correct answer to equation
        userEquation =  (numList[0] + numList[3]) / (numList[1] + numList [2])

        #Process- Round answer to two decimal places
        roundedAnswer = round(userEquation,2)

    #Process- Else condtion will run if operation selcted statsifies the second group ( * and -)
    else:

        #Output- Output structure of equation to user; list will be outputted to user, so user can sub numbers in accordnilgy
        generateEquation = print ("The format of this equation is", "\n", "(numList[0] * numList[3]) - (numList[1] * numList [2])")

        #Process- Create base structure of operation; this operation will be displayed to user as a string
        #Process- Cariable will hold correct answer to equation
        userEquationtwo =  (numList[0] * numList[3]) - (numList[1] * numList [2])

        #Process- Round answer to two decimal places
        roundedAnswertwo = round(userEquationtwo,2)


    #process- Return the applicable answer and list to the main program
    return roundedAnswer,roundedAnswertwo,numList

#Process - Define valid input answer that will erify if user has entered a correct number when the math function is being called
#Process - Two paramteres will be passed to compare if user has enetred the right answer to math equation
def valid_input(answerOne,answerTwo):

    #Process- Initialize try counter 
    tries = 2

    #Process - Intialize result to false
    result = False

    #Process - While Loop - While ties is not 0
    while tries != 0:
        
       #Process - Try the follwing 
        try:
            #Input - Get answer input from the user 
            userAnswer = float(input("Enter your answer ROUNDED TO TWO DECIMAL PLACES: "))

            #Process - If user answer is equal to answer 1 or 2, break
            if answerOne == userAnswer or answerTwo == userAnswer:
                break
            
            #Process - Else, subtract 1 from tries counter
            else:
                tries -= 1
                #Process - Output error message,with number of tries
                print("Answer is incorrect! You have",tries, "tries left!")

        #Process - If an exception is raised:
        except:
            #Process - Output error message
            print("Answer is incorrect!")
            
            #Process - Subtract 1 from tries counter
            tries -= 1
            
            #Process - Print number of tries left
            print("You have ",tries, "tries left!")

            userAnswer = "Not Usable"

    #Process- Compare and see if comp answer and user answer is equal
    if answerOne == userAnswer or answerTwo == userAnswer:
        
        #Output - Print correct answer message to user
        print("You DO NOT need to draw a card!")

    else:
        #Output - Print wrong answer message to user
        print("You HAVE TO draw a card")

        #Process- Reassign result to True, which will make the user pick up a card
        result = True

    #Process- Return result boolean to main program
    return result

#Process- Define play game function - Allow user to play the math game
def play_game ():
    
    #Process- Call math fuction; Use three variables to store returned values
    roundedAnswer, roundedAnswertwo, numList = math_operation()

    #Output- Print number list to user
    print("Here are all of the number you must use: ", numList)

    #Output- Make user aware anwer should be rounded to two decimal places
    print("You must round your answer to two decimal places!")

    #Process- Allow user to enter there answer call function, and pass the two answers
    drawResult = valid_input(roundedAnswer, roundedAnswertwo)

    #Process- Return draw result value to function
    return drawResult

#Process - Define get card function- Allow user to input card; through get card function; process pass inital user deck as manuplation will be done
def get_card(userDeck, aganistCard,colPlay):

    #Process- Intialize play card variable
    playCard = ""

    #Process- Intialize put card variable
    putCard = 0

    #Process- While loop will run until user enters a right input
    while True:

        #Process- Try condition will run, allowing user to enter input
        try:
            #Input- Ask user if they want to place a card or not?
            putCard = int(input("Would you like to place a card? 1 = YES 2 = NO: "))

            #Process- If statment will run if wrong input is enetred
            if putCard > 2 or putCard < 1:

                #Output- Output to user an error message
                print("Invalid input! Please try again!")

            #Process- Else condtion will run if user enetrrs corretc option eother 1 or 2
            else:

                #Erocess- Ehile loop will break once proper inout has been added
                break

        #Erocess- Except condtion will run if wrong data type was entered
        except:

            #Output- oOtput to user an error message, wrong datatype
            print("Wrong datatype! Please try again!")

    #Process- Update user deck will store the updated user deck
    updateUserdeck = userDeck[:]

    #Process- Intlize draw variable to false, will see if user has to draw a card
    drawCard = False

    #Process- If statment will run if user wants to put card
    if putCard == 1:

        #Process- Intlaize the card; which will store the card the user has played
        card = ""

        #Input- Ask the user to enter a card they would like to play
        card = input("Please enter the card you want to play: ")

        #Process- Check if enetred card is a valid card, and apart of the users deck
        if card in userDeck:

            #Process - If statement will run if user entered a playable card
            if(card[0] == aganistCard[0] and len(card) == 6) or  ((card[0] == aganistCard[0]
                or card[1] == aganistCard[1]  or (aganistCard == "CC" and colPlay in card [0]) )
                and (len(card) == 2 ) ) or ("Block" in aganistCard and "Block" in card) \
                or (card == "CC"  or card == "+2") or aganistCard == "+2":

                #Process- Once card is valid it will remove from current user playing deck
                updateUserdeck.remove(card)

                playCard = card

            #Process- If user has enetered a not playable card else stamnet will run
            else:

                #Process- Draw card will be reassinged to true
                drawCard = True

                #Output- Output to user that thier card is not playable
                print("The card you entered is NOT playable! Draw a card!")

        #Process- Else condtion will run if user has entered a not in the users deck
        else:

            #Orocess- Draw card will be reassinged to true
            drawCard = True
            #Output- Output to user that thier card is not playable
            print("You entered a card that is not in your deck! Draw a card!")

    #process- else condtion will run if user has selected option 2; invoke math function
    else:

        #Process- Play game function is called and returned value will be held in draw card
        drawCard = play_game ()

    #Process- Return used card, updated list and draw card value
    return playCard, drawCard, updateUserdeck

#Process - Define function called introduction - Print introduction with welcome message and rules
def introduction():
    print("****" * 16)
    print("*", "                                                            " , "*")
    print("*", "          Welcome to Muno! Also know as Math Uno!           " , "*")
    print("*", "              Created by Udisha and Anushka!                " , "*")
    print("*", "                                                            " , "*")
    print("*", "                   Here are the rules!                      " , "*")
    print("*", "                                                            " , "*")
    print("*", "   You will play against the computer, with 7 cards each!   " , "*")
    print("*", "        Your deck will contain Number and Wild cards!       " , "*")
    print("*", "The wild cards include: +2, Colour Change (CC) and Block!  " , "*")
    print("*", "   If you are unable to put down a card. You are given the  " , "*")
    print("*", "option to answer a math question to bypass picking up a card" , "*")
    print("*", "        First person to 0 cards, wins! Good Luck :))        " , "*")
    print("*", "                                                            " , "*")
    print("****" * 16)


#Main Program

#Process - Calling introduction function!
introduction()

#Process - Getting the Burn/Middle cards and updated burn pile; use two variables to hold two return values
extraPile = get_burnpile()

#Process - Getting the users cards; pass full burn deck as a parameter
userCardDeck = get_user_cards(extraPile)
#Output - Printing the users pile
print("Users Cards:" , userCardDeck)

#Process - Getting the computers cards; pass full burn deck as a parameter
computerCardDeck = get_computer_cards(extraPile,userCardDeck)
#Output - Printing the computers pile
#print("Computers Cards:", computerCardDeck)

#Process - Getting the Starting card
startingCard = get_firstCard(extraPile)

#Process- Remove staring card from burn deck
extraPile.remove(startingCard)

#Process- Intialize tries counter which will keeps track of tries and allow the user and comp to take turns
tries = 1

#Process- Block counter; Checks if block counter was invoked
blockCounter = 1

#Process- Initializes updated user deck list
updateUserdeck = userCardDeck [:]

#Process- Initializes updated computer deck list
updatedComputerDeck = computerCardDeck[:]

#Process - Intializes starting card to variavle of agasint card
aganistCard = startingCard

#Process- Pass colour in play to function as you want to comp to see what colour is in play
colourInplay = ""


#Process - While comuter deck and user deck is no 0 or tries == 1 run the following:
#Process - While loop to keep the game going, once user or computer run out of cards or burn deck runs out, while loop will stop running
while (len(updateUserdeck) != 0 and len(updatedComputerDeck) != 0 and len(extraPile) != 0) or tries == 1:

    #Output- Otput the aganist card
    print("The card you are playing aganist is:", aganistCard)

    #Process- if statement will run if tries is an odd number - Users Turn
    if tries % 2 != 0:

        #Process- Call function to get respective card from user pile
        cardResult, drawResult, updateUserdeck = get_card(updateUserdeck, aganistCard,colourInplay)
        
        #Process - Print User's Cards
        #print("User cards",updateUserdeck)

        #Process - If Block in Card Result(card user will play):
        if "Block" in cardResult:
            
            #Process- Add 2 to the tries counter to revert turn back to user
            tries += 2 

            #Process- Remove 1 from the block counter
            blockCounter = 0

        #Process - Elif draw result == true and card result is empty:
        elif drawResult == True and cardResult == "":

            #Process- Add a card from burn pile to user list by randomly picking interger
            burnCardindex = random.randint(0,len(extraPile)-1)

            #Process- Add card to user deck
            updateUserdeck.append(extraPile[burnCardindex])
            
        #Process- If card result is colur chnage
        elif cardResult == "CC":

            #Process- Intialize empty string to hold the colour user would like to choose
            colourChange = ""
            #Process - Intialize string of accecptable input for colours
            coloursAccpte = "RGYB"

            #Output- Print out the basic conventions to the user
            print("Red - R, Green - G, Yellow- Y, Blue - B")

            #Process - While colour change is an empty string
            while colourChange == "":
                #Input - Allow user to input color
                colourWanted = input("Enter the colour you want to switch to:")
                
                #Process - If user input is not in colours accepte or user entered more than 1 chracter 
                if colourWanted not in coloursAccpte or len(colourWanted) != 1:
                    
                    #Output - Print Error Message
                    print("You have enetred an invalid colour try again")

                else:
                    #Process - Else reassing colour change to users inputed colour
                    colourChange = colourWanted
                    
                    #Output - Print colour change
                    print("Colour has been switched to",colourChange)
                    
                    #Process - Reassing colour in play to colour change from the user
                    colourInplay = colourChange

        else:
            #Process - If card result is +2:
            if cardResult == "+2":

                #Process- Get 2 cards from the burn pile
                for x in range (2):

                    #Process- Add card to the comp deck
                    updatedComputerDeck.append(extraPile[x])

                    #Process- Delete cards from burn
                    extraPile.remove(extraPile[x])

        #Process - If block counter is not 0
        if blockCounter != 0:

            #Process- Ass one to counter as block HAS NOT BEEN INVOKED
            tries += 1

        else:
            blockCounter = 1

        #Process- This if stament will run if user invokes math function as the first command, (no string card) addressed
        if cardResult != "":
            aganistCard = cardResult

        #Output - Output cards in current deck to user
        print("Your current deck", updateUserdeck)

    #Process - Else, tries is even, which means it is the computers turn
    else:

        #Process- Call function to get respective card, result and updated 
        chosenCard, pickUpCardResult, updatedColor, updatedComputerDeck = comparing_computer_deck(updatedComputerDeck, aganistCard, updateUserdeck, colourInplay)

        #Process - If block is in the computers chosen card:
        if "Block" in chosenCard:

            #Process- Ass 2 to the tries to revert back to computer
            tries += 2

            #Process- Add one to block counter
            blockCounter = 0
            
        #Process - Elif chosen card is colour change:
        elif chosenCard == "CC":

            #Process - Updated the colour in play with updated colour from computer function
            colourInplay = updatedColor
            #Output - Print new colour to the user
            print("The new colour is:", colourInplay)


        else:
            #Process - If chosen card is plus 2
            if chosenCard == "+2":
                
                for x in range(2):
                    #Process- Add card to the user deck
                    updateUserdeck.append(extraPile[x])

                    #Process- Delete card from burn pile
                    extraPile.remove(extraPile[x])

        #Process - If block counter is not 0
        if blockCounter != 0:
            #Process- Add 1 to counter as block HAS NOT BEEN INVOKED
            tries += 1

        else:
            blockCounter = 1

        #Process - Is the chosen card is not empty:
        if chosenCard != "":
            #Process - Reassing agasint card to chosen card
            aganistCard = chosenCard
        #Process - If the computer does not need to pick up a card:
        if pickUpCardResult == False:
            #Process - Remove chosen card from the deck
            updatedComputerDeck.remove(chosenCard)

        #Process- Else statement will run if computer has to pick up a card
        else:

            #Process- Randomly pick an index value from that will be used to access a card from the burn pile
            burnCardIndex = random.randint(0,len(extraPile)-1)

            #Process- Add selected card to the computer deck
            updatedComputerDeck.append(extraPile[burnCardIndex])

        #Output - Print our computer deck and number of cards the computer has in hand
        #print("Update comp deck", updatedComputerDeck)
        print("The computer has", len(updatedComputerDeck), "cards!")

#process- if statment will run if the extra pile has run out
if len(extraPile) == 0:

    #process- if length of user pile is less than length of computer pile
    if len(updateUserdeck) > len(updatedComputerDeck):

        #output- output message stating the computer has one
        print(" BURN RAN OUT COMPUTER WINSS! Better Luck next time!")

    #process- elif stament will run if user and computer deck is equa;
    elif len(updateUserdeck) == len(updatedComputerDeck):

        #output- output message stating no one wins
        print("NO ONE WINS")

    #process- else condtion will run if length of user pile is greater than length of computer pile
    else:

        # output- output message stating the user has one
        print("BURN RAN OUT YOU WIN!")


#process- else condtion will run if burn pile has not run out
else:

    #process- if condtion will run if user has won
    if len(updateUserdeck) == 0:

        # output- output message stating the user has one
        print("YOU WIN! CONGRATULATIONS!!")

    # process- if condtion will run if user has won
    else:

        # output- output message stating the computer has one
        print("COMPUTER WINSS! Better Luck next time!")

