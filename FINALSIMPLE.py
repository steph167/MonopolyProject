import random #imports the random python library

class SetUp:
    def __init__(self):
        self.maxP = 6 #max no of players
        self.minP = 2 #min no of players
        self.startMoney = 1500
        self.candyCard = 'Cotton Candy Card'
        self.board = ['Go', 'Love Hearts', self.candyCard, 'Parma Violets', 'Sugar tax',
                      'Maoams', 'Gummy Bear', self.candyCard,'Gum Drops', 'Wine Gums',
                      'The Dentist','Strawberry Laces', 'Candy Shop', 'Strawberry Pencils',
                      'Rainbow Belts','Haribos', 'Chewits', self.candyCard, 'Starbursts',
                      'Fruittellas', 'Free Candy','Cola Bottles', self.candyCard,'Fizzy Cola Bottles',
                      'Fizzy Blue Bottles', 'Chupa Chups', 'Giant Strawberry', 'Giant Cherries',
                      'Sweet Factory','Gummy Snakes', 'Go to the dentist','Fox Glaciers', 'Humbugs',
                      self.candyCard, 'Imperial Mints', 'Drumsticks', self.candyCard, 'Nerds',
                      'Medical Bill', 'Popping Candy']
        self.noOfPlayers = self.players() #sets the number of players by the user
        self.playersBanks = [] #array of each players banks
        self.playersPlaces = [] #array of each players current position
        self.inDentist = []
        self.outOfDentistFree = [] #array of the number of get out of dentist free each player has
        for i in range(0, self.noOfPlayers):
            self.playersBanks.append(self.startMoney) #sets all users start banks
            self.playersPlaces.append(1) #sets all users start places (GO)
            self.inDentist.append(False) #no body is in jail in the beguinning
            self.outOfDentistFree.append(0) #all players have 0 number of dentist free cards
        self.owned = []
        for i in range(0, 40):
            self.owned.append('empty')
        self.freeCandy = 0 #initialised at the start to 0
        self.money() # prints out the money to
        self.bagPrices = [50, 100, 150, 200] #The prices of the buying a bag
        self.landedOnPrices = [[2, 10, 20, 90, 160, 250], [6, 30, 90, 270, 400, 550],
                               [10, 50, 150, 450, 625, 750], [14, 70, 200, 550, 750, 950],
                               [18, 90, 250, 700, 875, 1050], [22, 110, 330, 800, 975, 1150],
                               [26, 130, 390, 900, 1100, 1275], [35, 175, 500, 1100, 1300, 1500]]
                                # if a player lands on owned square
                                # layout = [0 bags, 1 bag, 2 bag, 3 bags, 4 bags, 1 tub]
        self.sweets = {2: [60, 0, 0, 0, 0], 4: [60, 0, 0, 0, 1],
                       7: [100, 0, 1, 0, 0], 9: [100, 0, 1, 0, 1], 10: [100, 0, 1, 0, 2],
                       12: [140, 1, 2, 0, 0], 14: [140, 1, 2, 0, 1], 15: [140, 1, 2, 0, 2],
                       17: [180, 1, 3, 0, 0], 19: [180, 1, 3, 0, 1], 20: [180, 1, 3, 0, 2],
                       22: [220, 2, 4, 0, 0], 24: [220, 2, 4, 0, 1], 25: [220, 2, 4, 0, 2],
                       27: [260, 2, 5, 0, 0], 28: [260, 2, 5, 0, 1], 30: [260, 2, 5, 0, 2],
                       32: [300, 3, 6, 0, 0], 33: [300, 3, 6, 0, 1], 35: [300, 3, 6, 0, 2],
                       38: [350, 3, 7, 0, 0], 40: [350, 3, 7, 0, 1]} #all the sweet information
                    #layout --> = {Location: [price, bagPrices ref, landedOnPrices ref, noOfBags, inner array number], ….
        self.sweetsOwned = [['',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','']]
        self.sweetsNos = [[2,4],[7,9,10],[12,14,15],[17,19,20],[22,24,25],[27,28,30],[32,33,35],[38,40]]
        

    #In this function, the program will ask how many players the user wants,
    #This is only accepted if the number of players is smaller or equal to 6
    #Or larger or equal to 2, if this is incorrect the program will not move on
    def players(self):
        noOfPlayers = self.isPlayerInt()
        while (noOfPlayers > self.maxP or noOfPlayers < self.minP):
            print("\nThere can only be 2 to 6 players")
            noOfPlayers = self.isPlayerInt()
        return noOfPlayers

    #This function, insures that the noOfPlayers is an integer
    def isPlayerInt(self):
         while True:
            noOfPlayers = input("How many players are there?")
            try: #trys to turn noOfPlayers into an integer
                return int(noOfPlayers)
            except ValueError: #excepts the error if it is not and asks the user again
                print('The number of players must be an integer!')

    #Sets the money for each user to 150
    def money(self):
        print("\nEach player starts with", self.startMoney, "candy coins!")
        return

class Game:
    def __init__(self):
        self.roleAgain = False #if the dice are matching, this is true

    #this function, calculates the 2 dice values and checks if they are a double
    def roleDice(self, player):
        dice1 = random.randint(1,6) #calculates randomly the numbers on the dice
        dice2 = random.randint(1,6)
        input("\nPlayer " + str(player+1) + ", please role the dice(<ENTER>)")
        #when the user presses enter, the calculated duce is returned to the main class
        if (dice1 == dice2):
            self.roleAgain = True #is a double
        return [self.roleAgain, dice1+dice2] 

class Main(SetUp): #inherits from 'SetUp'
    def __init__(self):
        SetUp.__init__(self) #Initialises alll variables in 'SetUp'
        self.again = True
        self.lost = 0

    def go(self):
        while True: #loops forever until broken out from (return/break etc.)
            for player in range(0, self.noOfPlayers):
                self.again = True
                if (self.playersBanks[player] < 0): #is this player bankrupt
                    print('/nPlayer', player+1, 'is out of the game, therefore misses a turn')
                    #therefore misses a go, and moves on to the next player
                elif (self.inDentist[player] == True): #if the player is in the dentist
                    self.dentist(player) #go to the function dentist
                else:
                    while(self.again == True):
                        if (self.lost == (self.noOfPlayers-1)): #if there is only one player left
                            print('/nPlayer', player+1, 'you have won the game!')
                            return #player has won, and the game has ended
                        self.addBagsTubs(player)
                        dice = Game().roleDice(player) #roles the dice
                        print('Dice =', dice[1])
                        self.playersPlaces[player] += dice[1] #sets the players new position
                        self.pastGoCheck(player) #checks if the player has gone around the whole board
                        print("You have landed on ", self.board[self.playersPlaces[player]-1])
                        i = self.playersPlaces[player] #i = the square the player is on
                        if (i == 3 or i == 18 or i == 34 or i == 8 or i == 23 or i == 37):
                            self.candyCards(player) #if the player has landed on a candy card, the desired action is completed
                        self.squares(player, dice[1])
                        self.again = dice[0]
                        if (self.playersBanks[player] < 0):# checks to see if player is bankrupt
                            print('\nPlayer', player+1, 'has gone bankrupt! Therefore are out of the game!')
                            self.lost += 1 #increments self.lost to show a player has gone bankrupt
                            self.again = False # ends their go completely 
                        if (self.inDentist[player] == True):
                            self.again = False #if they get sent to jail they have to wait until their next go
                        elif (dice[0] == True): #rolled a double, while loop runs again with the same player
                            print("You have rolled a double, therefore you get another role!")
                            self.again = True
                        else: #no double, therefore moves on to next player
                            self.again = False


    def pastGoCheck(self, player):
        if (self.playersPlaces[player] > 40): # when they have gone past the start of the board
            self.playersPlaces[player] -= 40 # sets the new positon
            self.playersBanks[player] += 200 # adds 200 cc to their bank
            print("\nGone past go, you have collected 200 candy coins!")
            print('Players bank:', self.playersBanks[player])
        return

    def addBagsTubs(self, player):
        canAddNames = [] #2 dimensional array of all the possible squares names
        canAddNos = [] #2 dimensional array of all the possible squares location numbers
        for outer in range(0, len(self.sweetsOwned)):
            no = 0 #number of items belonging to that player in that array
            for inner in range (0, len(self.sweetsOwned[outer])):
                if (self.sweetsOwned[outer][inner] == player):
                    no += 1 
                if (no == (len(self.sweetsOwned[outer]))):
                    #if player owns all squares belonging to that colour
                    canAddNos.append(self.sweetsNos[outer])
                    names = []
                    for k in range(0, len(self.sweetsNos[outer])):
                        names.append(self.board[self.sweetsNos[outer][k]-1])
                        #adds to the list all the names of the squares in that colour 
                    canAddNames.append(names)
                    
        if (canAddNos != []): #when there is at least 1 all colours owned
            qu = input('\nPlayer '+ str(player+1) + ', would you like to add any '
                       'candy bags to any of your squares?(y/n)')
            if (qu == 'y'): #if they would it outputs all the possible options
                for m in range(0, len(canAddNames)): #prints out number of options
                    print('\nOption', m+1, ':')
                    for n in range(0, len(canAddNames[m])): #with the squares names underneath 
                        print(canAddNames[m][n])
                print('\nOption 100: QUIT')
                while(True): #while not been broken out of
                    option = int(input('\nWhich option would you like to choose? (option number)'))
                    if (option == 100): #choose quit 
                        return #returns to go
                    elif ((option <= len(canAddNos)) and (option > 0)): #if option is valid
                        addTo = canAddNos[option-1][0] #addTo = square the bag/tub will be added to
                        for p in range (0, len(canAddNos[option-1])): #for every square in that option
                            square = canAddNos[option-1][p] #square = current square
                            if (self.sweets[addTo][3] > self.sweets[square][3]):
                                #chooses the square with least amount of bags/tubs on
                                addTo = canAddNos[option-1][p]
                        if (self.sweets[addTo][3] > 5): #max number of tubs
                            print('Sorry you have the max number of tubs on that colour squares!')
                        else:
                            print('It is ', self.bagPrices[self.sweets[addTo][1]], ' candy coins to buy a bag/tub')
                            an = input('Would you like to add a bag to ' + self.board[addTo-1]+ '?(y/n)')
                            if (an == 'y'): 
                                self.sweets[addTo][3] += 1 #adds a bag to the square in the dictionary
                                self.playersBanks[player] -= self.bagPrices[self.sweets[addTo][1]]
                                print('You have added a bag/tub to your square!')
                                return
                    else: #if option is not valid
                        print('This is not an option')
                   

    def squares(self, player, dice):
        square = self.playersPlaces[player] #the players square they are currently on
        if (square == 6 or square == 16 or square == 26 or square == 36):
            self.companies(player) 
        elif (square == 5 or square == 39):
            self.bills(player) #ensures the player pays their bills
        elif (square == 13 or square == 29):
            self.temptations(player, dice) 
        elif (square == 21):
            print('\nFree Candy, you have collected', self.freeCandy, 'candy coins!')
            self.playersBanks[player] += self.freeCandy #adds the money to the players bank
            self.freeCandy = 0 #resets the free candy square
        elif (square == 31):
            print('\nYou have been sent to the dentist')
            self.playersPlaces[player] = 11 #moves player into the dentist
            self.inDentist[player] = True 
        elif (square == 1 or square == 11 or square == 3 or square == 18 or
              square == 34 or square == 8 or square == 23 or square == 37):
            return #nothing happenes when a player lands on these squares
        else: #all remaining squares - candy squares
            self.candySquares(player, square)
        return

        
    def candyCards(self, player):
        print('Bank:', self.playersBanks[player])
        cards = ['Braces bill, pay 100cc',
                 'Tooth fairy\'s came, collect 200cc',
                 'Get out of dentist free card',
                 'Advance to Go and collect 200cc',
                 'Buy the pinata for the party, pay 100cc',
                 'Cavity! Go to the dentist!',
                 'Take a trip to the Sweet Factory',
                 'You\'ve had a filling, pay 100cc',
                 'Sugar rush, advance 3 places']
        choice = random.randint(0,8) #picks a random number between 0 and 8
        print('Your card = ', cards[choice]) #chooses the random card
        if (choice == 0 or choice == 4 or choice == 7):
            self.bills(player) #uses the bills function to pay the 100cc
        elif (choice == 1):
            self.playersBanks[player] += 200 #add 200 to the players bank
        elif (choice == 2):
            self.outOfDentistFree[player] += 1 #adds a card to be used to be released
        elif (choice == 3):
            self.playersPlaces[player] = 1 #moves player to go 
            self.playersBanks[player] += 200 #adds 200 to the players bank
            print("You are on", self.board[self.playersPlaces[player]-1])
        elif (choice == 5):
            self.playersPlaces[player] = 11 #moves player in the dentist
            self.inDentist[player] = True 
            print("You are on", self.board[self.playersPlaces[player]-1])
        elif (choice == 6):
            self.playersPlaces[player] = 29 #moves player to the sweet factory
            print("You are on", self.board[self.playersPlaces[player]-1])
        elif (choice == 8):
            self.playersPlaces[player] += 3 #moves player 3 places forwards
            print("You are on", self.board[self.playersPlaces[player]-1])
        print('Bank:', self.playersBanks[player])
        return

    def bills(self, player):
        print('You have to pay your bills, pay 100cc')
        self.playersBanks[player] -= 100 # The gets taken from the players bank
        self.freeCandy += 100 # and given to the free candy square
        return

    def temptations(self, player, dice):
        #if the players square they are currently on is empty:
        if(self.owned[self.playersPlaces[player]-1] == 'empty'): 
            self.buySquare(player, 150) #price = 150
        else:
            if (self.owned[self.playersPlaces[player]-1] != player):
                i = self.owned[self.playersPlaces[player]-1]
                #i = who owns the current temptation
                if ((self.owned[12] == i)and(self.owned[28] == i)):
                    multiplyBy = 10 #if both of the temptations are owned by the same player
                elif ((self.owned[12] == i)or(self.owned[28] == i)):
                    multiplyBy = 4 #if one of the temptations is owned
                toPay = dice * multiplyBy
                print('\nYou have to pay', multiplyBy, 'times the amount shown on the dice =', toPay)
                self.playersBanks[player] -= toPay # takes away the money from the current player
                print('Player', i+1, 'you have recieved', toPay, 'candy coins')
                self.playersBanks[i] += toPay #gives the money to the player who owns that temptation
                return

    def companies(self, player):
        places = [5, 15, 25, 35] #the positions of the companies on the board 
        prices = [25, 50, 100, 200] #prices for the number of companies owned
        howManyOwned = 0 #initilises to 0
        i = self.owned[self.playersPlaces[player]-1]
        # i = the player that owns the current square
        if(i == 'empty'):
            self.buySquare(player, 200) #price = 200
        else:
            if (i != player): #if it is not owned by the current player
                for j in range(0, 4): # for the number of companies
                    if (self.owned[places[j]] == i):
                        #if they are owned by the player that owns the current square
                        howManyOwned += 1 #increment howManyOwned
                print('Player', (i+1),'owns', howManyOwned, 'companies')
                toPay = prices[howManyOwned-1]
                #Pays in regards to how many companies that player owns
                print('Therefore, player', player+1, 'you have to pay', toPay, 'candy coins!')
                self.playersBanks[player] -= toPay # takes away the money from the current player
                print('Player', (i+1), 'you have recieved', toPay, 'candy coins!')
                self.playersBanks[i] += toPay #pays the player who owns the company
        return
        

    def candySquares(self, player, square):
        ownedBy = self.owned[self.playersPlaces[player]-1] #player the current square is owned by
        sweetInfo = self.sweets[square] # the list of the information about the sweet (current square)
        if(ownedBy == 'empty'):
            brought = self.buySquare(player, sweetInfo[0]) #sweetInfo[0] = price
            if (brought == True):
                outer = sweetInfo[2] #first reference for sweetsOwned
                inner = sweetInfo[4] #second reference for sweetsOwned
                self.sweetsOwned[outer][inner] = player
        else:
            if (ownedBy != player): #if the square is unowned
                print('\nThe number of bags on', self.board[self.playersPlaces[player]-1],
                      'is', sweetInfo[3]) 
                squaresPriceList = self.landedOnPrices[sweetInfo[2]] 
                toPay = squaresPriceList[sweetInfo[3]]
                #is the price for the number of bags currently on that square
                self.playersBanks[player] -= toPay
                print('Therefore you have to pay', toPay)
        return

    def buySquare(self, player, price):
        print('banks', self.playersBanks)
        print('\nThe price of', self.board[self.playersPlaces[player]-1], 'is', price, 'cc')
        decision = input('Would you like to buy it(y/n)?')
        if (decision == 'y'): #if they would like to buy it...
            self.owned[self.playersPlaces[player]-1] = player # saved player under that square
            self.playersBanks[player] -= price #ensures the players pay for the property
            print('You have brought', self.board[self.playersPlaces[player]-1])
            print('banks', self.playersBanks)
            return True #returns true if it has been brought
        return False #returns false if the player does not want to buy the square
            
    def dentist(self, player):
        #dentist menu
        print('\nPlayer', (player+1), ', you are in the dentist, to be released you have 3 options:')
        print('1. Pay 50cc')
        print('2. If you role a double')
        print('3. Use a get out of dentist free card')
        while (True):
            option = self.checkIfInt() #ensures that the uses input for option is an integer
            if (option == 1): #Pays 50cc to be released
                self.playersBanks[player] -= 50 
                self.freeCandy += 50
                print('You have payed 50 and are now released from the dentist!')
                self.inDentist[player] = False #released from the dentist
                return
            elif (option == 2):
                dice = Game().roleDice(player) #roles the dice
                if (dice[0] == True): #if it is a double
                    print('You have rolled a double and are released from the dentist!')
                    self.inDentist[player] = False #releaed front the dentist
                    return
                else: #if it is not a double
                    print('You haven\'t been released from the dentist, maybe next time!')
                    return #have to wait until their next go
            elif (option == 3):
                if (self.outOfDentistFree[player] >= 1): #if they have a card 
                    print('You have used one of your cards and have been released from the dentist!')
                    self.outOfDentistFree[player] -= 1
                    self.inDentist[player] = False
                    return
                else: #if they do not have a card, therefore they have to try again
                    print('You do not have a get out of dentist free card!')  
            else: #incorrect option is entered
                print('This is not an option, try again')

    def checkIfInt(self):
        while True:
            option = input('\nPlease enter your option:')
            try: #trys to turn option into an integer
                return int(option)
            except ValueError: #excepts the error if it is not and asks the user again
                print('The number of players must be an integer!')


Main().go() #calls the function from main
