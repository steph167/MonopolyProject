import pygame
import sys
import random
import time
pygame.init()

class GUIfunctions:
    def __init__(self):
        self.text = pygame.font.Font('freesansbold.ttf',15) #font and size of text
        self.boardPic = pygame.image.load('board.png')# loads the board image
        self.noOption = pygame.image.load('no.png') # loads the no button image
        self.yesOption = pygame.image.load('yes.png') # loads the yes button image
        self.dice = pygame.image.load('dice.png')# loads the dice image
        self.sweetBagPics = pygame.image.load('bag.png') # loads the bag image
        self.sweetTubPics = pygame.image.load('tub.png') # loads the tub image
        self.sidePos = [600,0,300,600] #position of the side output column
        self.textPosX = 750 #what the side text is centered around
        self.bg =(198,226,255) #colours used (bg = background)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)
        self.bWidth = 600 #board width and height
        self.bHeight = 600
        #positions of the center for each square on the board
        self.boardPos = [[10, 10], [75, 10], [125, 10], [175,10], [225,10], [275,10], [325,10], [375,10], [425,10], [475, 10], [545, 10],
                         [545, 80], [545, 125], [545, 175], [545, 225], [545, 275], [545, 325], [545, 375], [545, 425], [545, 475], [545, 545],
                         [475, 545], [425,545], [375,545], [325,545], [275,545], [225,545], [175,545], [125, 545], [75, 545], [10, 545],
                         [10, 475], [10, 425], [10, 375], [10, 325], [10, 275], [10, 225], [10, 177], [10, 125], [10, 80]]
        self.pExtra = [[-4,4], [-2,-2], [0,0], [2,2], [4,4], [6,6]] #positions of each player


    def createScreen(self):
        pygame.display.set_caption('Candy Monopoly') #captions the top of the window
        pygame.draw.rect(gameDisplay, self.bg, [600,0,300,600]) #draws a rectangle for the side screen
        gameDisplay.blit(pygame.transform.scale(self.boardPic, (self.bWidth, self.bHeight)), (0,0))
            #displays the board 
        pygame.display.update() #updates the screen


    def textF(self, message, font): #sets text
        textSurface = font.render(message, True, self.black)#chooses the font
        return textSurface, textSurface.get_rect()

    def sideText(self, string, pX, pY): #gets the message, and the position of it
        noOfPText = self.textF(str(string), self.text) #gets the chosen font of the message
        noOfPText[1].center = (pX, pY) #centers the text around the x and y coordinate sent
        gameDisplay.blit(noOfPText[0], noOfPText[1])
        pygame.display.update()
        return

    def toQuit(self):
        for event in pygame.event.get(): #allows user to quit
            if event.type == pygame.QUIT:
                 pygame.quit(); sys.exit();

    def click(self, x, y, w, h): #takes the x and y position and the size
        mouse = pygame.mouse.get_pos() #the position of the mouse
        click = pygame.mouse.get_pressed() #if the mouse is clicked
        if ((x+w>mouse[0]>x) and (y+h>mouse[1]>y)):
            #if it is hovering over that particular button
            if click[0] == 1: #if that button was clicked
                pygame.draw.rect(gameDisplay, self.black,[x,y,w,h])
                #shows the user its been clicked
                pygame.display.update()
                return True #returns that its been clicked

    def updateBoard(self):#clears the board then updates it
        gameDisplay.blit(pygame.transform.scale(self.boardPic, (self.bWidth, self.bHeight)), (0,0))
        #displays the board
        for i in range(0, self.noOfPlayers): #for every player
            counter = self.playersCounters[i]
            #changes the postion of the counter, therefore all counters can be seen
            #if they are all on the same square
            x = self.boardPos[self.playersPlaces[i]-1][0] + self.pExtra[i][0]
            y = self.boardPos[self.playersPlaces[i]-1][1] + self.pExtra[i][1]
            gameDisplay.blit(pygame.transform.scale(counter, (45,45)), [x, y])
            #update the board with the counters new position
        pygame.display.update()

    def clearSideScreen(self): #clears the side screen
        pygame.draw.rect(gameDisplay, self.bg, self.sidePos)
        pygame.display.update() #updates the screen
            

class SetUp(GUIfunctions):
    def __init__(self):
        GUIfunctions.__init__(self)
        self.candyCard = 'Cotton Candy Card'
        self.board = ['Go', 'Love Hearts', self.candyCard, 'Parma Violets', 'Sugar tax', 'Maoams', 'Gummy Bear', self.candyCard, 'Gum Drops', 'Wine Gums', ' the Dentist',
                      'Strawberry Laces', 'Candy Shop', 'Strawberry Pencils', 'Rainbow Belts', 'Haribos', 'Chewits', self.candyCard, 'Starbursts', 'Fruittellas', 'Free Candy',
                      'Cola Bottles', self.candyCard, 'Fizzy Cola Bottles', 'Fizzy Blue Bottles', 'Chupa Chups', 'Giant Strawberry', 'Giant Cherries', 'Sweet Factory', 'Gummy Snakes', 'Go to the dentist',
                      'Fox Glaciers', 'Humbugs', self.candyCard, 'Imperial Mints', 'Drumsticks', self.candyCard, 'Nerds', 'Medical Bill', 'Popping Candy']
        self.noPlayers = [] #the message that goes on each button for noOfPlayers
        self.noPlayersPos = [660, 700, 740, 780, 820] #button positions for noOfPlayers
        self.pCButtons = (105,89,205) #colour of buttons for noOfPlayers
        self.playersCounters = [] #list of players counters pictures
        self.noOfPlayers = self.players() #sets the number of players by the user
        self.playersBanks = [] #array of each players banks
        self.playersPlaces = [] #array of each players current position
        self.startMoney = 1500 # players start with this amount in their banks
        self.inDentist = [] #if player is in the denist - True = they are
        self.outOfDentistFree = [] #array of the number of get out of dentist free each player has
        self.freeCandy = 0 #initialised at the start to 0
        for i in range(0, self.noOfPlayers):
            self.playersBanks.append(self.startMoney) #sets all users start banks
            self.playersPlaces.append(1) #sets all users start places (GO)
            self.inDentist.append(False) #no body is in jail in the beguinning
            self.outOfDentistFree.append(0) #all players have 0 number of dentist free cards
        self.owned = []
        for i in range(0, 40): #no player owns any squares at the beguinning
            self.owned.append('empty') 
        self.outDentistText = 'Pay 50cc', 'Try role a double', 'Use a get out of dentist free card'
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
        
    
    def players(self):
        self.sideText('How many players?',  self.textPosX, 100)
        #below creates 5 buttons with numbers 2-6 and positions them in the correct place
        for k in range(0,5): #creates the rectangle 
            pygame.draw.rect(gameDisplay, self.pCButtons,[self.noPlayersPos[k],150,20,20])
        for j in range(1,6): #adds the text on the rectangle
            p = self.textF(str(j+1), self.text) 
            self.noPlayers.append(p)
        for i in range(0,5): #centers the text
            self.noPlayers[i][1].center = ((self.noPlayersPos[i]+(20/2)),(150+(20/2)))
            gameDisplay.blit(self.noPlayers[i][0], self.noPlayers[i][1])
        pygame.display.update() #updates the screen
        while True:
            self.toQuit()
            for m in range(0,5): #for every button
                x = self.noPlayersPos[m]
                click = self.click(x,150,20,20) #if it is clicked - True
                if (click == True):
                    time.sleep(0.2)
                    # clears the side screen
                    pygame.draw.rect(gameDisplay, self.bg, self.sidePos)
                    self.noOfPlayers = m+2 #sets noOfPlayers to the button which was pressed
                    self.createCounters() #creates counter for every player
                    return self.noOfPlayers #returns noOfPlayers


    def createCounters(self): #creates the counters for the noOfPlayers
        for i in range(0, self.noOfPlayers):
            counter = pygame.image.load('counter'+str(i+1)+'.png')
            #loads the picture of each counter depending on which players
            self.playersCounters.append(counter)
            

class Game(GUIfunctions):
    def __init__(self):
        GUIfunctions.__init__(self)
        self.roleAgain = False #if the dice are matching, this is true
        self.dPosX = 250 #position of dice
        self.dPosY = 400
        self.dSize = 100
        
    def roleDice(self, player):
        self.sideText('Click below to role the dice:', 300, 350)
        #scales the picture of the dice and located it near the middle of the board
        gameDisplay.blit(pygame.transform.scale(self.dice, (self.dSize,self.dSize)),(self.dPosX,self.dPosY))
        pygame.display.update() 
        while True: #while this look has not been broken
            self.toQuit()
            click = self.click(self.dPosX,self.dPosY,self.dSize,self.dSize)
            if (click == True): #if dice has been clicked on
                dice = self.calculateDice(player) #calculate the dice
                return dice

    def calculateDice(self, player):
        dice1 = random.randint(1,6) #the dice is calculated
        dice2 = random.randint(1,6)
        if (dice1 == dice2): #if it is a double
            self.roleAgain = True
        return [self.roleAgain, dice1, dice2]

    def diceGUI(self, player):
        dice = self.roleDice(player) #when the dice has been rolled
        # dice format = [self.roleAgain, dice1, dice2]
        self.sideText('Dice 1 ='+str(dice[1]),  self.textPosX, 150)
        self.sideText('Dice 2 ='+str(dice[2]),  self.textPosX, 170)
        return dice #returned to the main program

    

class Main(SetUp):
    def __init__(self):
        SetUp.__init__(self)
        self.again = False
        self.double = False
        self.playersP = self.noOfPlayers #no of players playing
        self.lost = 0 #no of players bankrupt
        self.playersLost = [] #list of players who have lost
        self.oSize = 30 #button options size
        self.denOutPos = [200, 240, 280] 
        self.dCButtons = (255,193,193)
        self.bagsCButtons = (255,131,250)
        self.continueButton = (127,255,212)

    def go(self):
        while True:
            self.toQuit() #loops forever until broken out from (return/break etc.)
            self.updateBoard()
            for player in range(0, self.noOfPlayers):
                self.again = True
                self.updateBoard()
                if (self.playersBanks[player] <= 0): #is this player bankrupt
                    self.clearSideScreen()
                    self.sideText('Player '+str(player+1)+' is out of the game,',  self.textPosX, 220)
                    self.sideText('Therefore misses a go!',  self.textPosX, 240)
                    self.continueB()
                elif (self.inDentist[player] == True): #if the player is in the dentist
                    self.dentist(player) #go to the function dentist
                else:
                    while(self.again == True):
                        if(self.lost == (self.noOfPlayers-1)): #if there is only one player left
                            self.clearSideScreen()
                            self.sideText('Player '+str(player+1),  self.textPosX, 200)
                            self.sideText('Has won the game!',  self.textPosX, 220)
                            pygame.display.update()
                            return #player has won, and the game has ended
                        self.noPlayersGUI(player)
                        self.listProperties(player)
                        self.addBagsTubs(player)
                        self.noPlayersGUI(player)
                        self.banks()
                        if (self.double == True): #if the player has rolled a double
                            self.sideText('You have rolled a',  self.textPosX, 220)
                            self.sideText('double, therefore you get',  self.textPosX, 240)
                            self.sideText('another role!',  self.textPosX, 260)
                        dice = Game().diceGUI(player) #roles the dice
                        self.sideText('Move '+str(dice[1]+dice[2])+' places!',  self.textPosX, 190)
                        time.sleep(2)
                        totalDice = dice[1] + dice[2]
                        self.playersPlaces[player] += totalDice
                        self.pastGoCheck(player)
                        self.updateBoard()
                        self.clearSideScreen()
                        self.landedOn(player)
                        self.squares(player, dice[1])
                        self.again = dice[0]
                        self.double = dice[0] #if dice were a double
                        if (self.playersBanks[player] < 0): #if the player has gone bankrupt
                            self.clearSideScreen()
                            self.sideText('Player '+str(player+1)+' has gone bankrupt!,',  self.textPosX, 220)
                            self.sideText('Therefore are out of the game!',  self.textPosX, 240)
                            self.continueB() #continue button
                            self.playersP -= 1 #one less player playing
                            self.lost += 1
                            self.playersLost.append(player)
                            self.again = False
                        elif (self.inDentist[player] == True):
                            self.again = False


    def addBagsTubs(self, player):
        canAddNames = [] #2 dimensional array of all the possible squares names
        canAddNos = [] #2 dimensional array of all the possible squares location numbers
        for outer in range(0, len(self.sweetsOwned)):
            no = 0 #number of items belonging to that player in that array
            full = 0
            for inner in range (0, len(self.sweetsOwned[outer])):
                if (self.sweetsOwned[outer][inner] == player):
                    no += 1 
                    if (self.sweets[self.sweetsNos[outer][inner]][3] >= 5):
                        full += 1 #if a square is full (all squares own tubs)
                if (no == len(self.sweetsOwned[outer])):
                    #if player owns all squares belonging to that colour
                    if (full != (len(self.sweetsOwned[outer]))): #if you can add more bags
                        canAddNos.append(self.sweetsNos[outer])
                        names = []
                        for k in range(0, len(self.sweetsNos[i])):
                            names.append(self.board[self.sweetsNos[i][k]-1])
                            #adds to the list all the names of the squares in that colour
                        canAddNames.append(names)

        if (canAddNos != []): #when there is at least 1 all colours owned
            self.clearSideScreen()
            self.sideText('Player '+ str(player+1), self.textPosX, 100)
            self.sideText('Would you like to add any candy', self.textPosX, 120)
            self.sideText('bags to any of your squares?', self.textPosX, 140)
            gameDisplay.blit(pygame.transform.scale(self.yesOption, (self.oSize,self.oSize)),(680,300))
            gameDisplay.blit(pygame.transform.scale(self.noOption, (self.oSize,self.oSize)),(780,300))
            pygame.display.update()
            #displays the yes and no buttons
            while True:
                self.toQuit()
                click = self.click(680, 300, self.oSize, self.oSize)
                #if the player clicks on yes
                if (click == True):
                    self.clearSideScreen()
                    self.chooseOption(player, canAddNames, canAddNos)
                    return
                click = self.click(780, 300, self.oSize, self.oSize)
                #if the player clicks no
                if click == True:
                    time.sleep(0.5)
                    self.clearSideScreen()
                    return

    def chooseOption(self, player, canAddNames, canAddNos):
        y = 160
        opPos = [] #option positions
        optionButtons = [] #option texr
        self.sideText('Player '+ str(player+1), self.textPosX, 100)
        self.sideText('Choose an option:', self.textPosX, 120) 
        for m in range(0, len(canAddNames)): #displays option buttons    
            opPos.append([620, y]) #adds the postition of the option
            o = self.textF('Option '+str(m+1)+ ':', self.text)
            optionButtons.append(o)
            for n in range(0, len(canAddNames[m])):
                self.sideText(canAddNames[m][n], 800, y)
                y += 20 #outpiuts the names of the squares underneath the option
        o = self.textF('Quit', self.text)
        optionButtons.append(o)
        opPos.append([self.textPosX, 500])
        for s in range(0, len(opPos)):
            pygame.draw.rect(gameDisplay, self.bagsCButtons, [opPos[s][0], opPos[s][1], 100, 20])
            optionButtons[s][1].center = ((opPos[s][0]+(100/2)),(opPos[s][1]+(20/2)))
            gameDisplay.blit(optionButtons[s][0], optionButtons[s][1])
            #outputs every option and option text (optionButtons)
        pygame.display.update()
        while True:
            self.toQuit()
            click = self.click(self.textPosX, 500, 100, 20)
            #if the player presses quit
            if click == True:
                self.clearSideScreen() #clears output screen
                return
            for t in range(0, len(opPos)-1): #for every option button
                click = self.click(opPos[t][0], opPos[t][1], 100, 20)
                if (click == True):
                    #if it is clicked
                    time.sleep(0.2)
                    pygame.draw.rect(gameDisplay, self.bg, self.sidePos)
                    #shows that it has been clicked
                    addTo = canAddNos[t][0] #list of squares in that colour
                    for v in range (0, len(canAddNos[t])):
                        square = canAddNos[t][v] #the default square
                        if (self.sweets[addTo][3] > self.sweets[square][3]):
                            #chooses the square with least amount of bags/tubs on
                            addTo = canAddNos[t][v]
                    self.sweets[addTo][3] += 1 #adds a bag to the sweet squares dictionary
                    self.playersBanks[player] -= self.bagPrices[self.sweets[addTo][1]]
                        #pays the price
                    self.sideText('Player '+ str(player+1), self.textPosX, 100)
                    if (self.sweets[addTo][3] == 5): #if a tub has been added
                        self.sideText('You have added a tub to:', self.textPosX, 140)
                        self.sideText(self.board[addTo-1], self.textPosX, 160)
                        gameDisplay.blit(pygame.transform.scale(self.sweetTubPics , (50, 50)),(720, 200))
                        #displays a tub
                    else: #if a bag has been added
                        self.sideText('You have added a bag to:', self.textPosX, 140)
                        self.sideText(self.board[addTo-1], self.textPosX, 160)
                        self.sideText('The number of bags:', self.textPosX, 200)
                        x = 636
                        for i in range(0, self.sweets[addTo][3]):
                            gameDisplay.blit(pygame.transform.scale(self.sweetBagPics , (30, 30)),(x, 250))
                            x += 66
                        #displays the number of bags
                    self.continueB()
                    return 
             

    def pastGoCheck(self, player): #checks if player has passed go
        if (self.playersPlaces[player] > 40): # when they are the start of the board
            self.playersPlaces[player] -= 40 # updates the players new position on the board
            self.playersBanks[player] += 200 # adds 200cc
            self.clearSideScreen() #clears the side screen
            self.sideText('Player '+str(player+1),  self.textPosX, 180)
            self.sideText('You have passed go!',  self.textPosX, 220)
            self.sideText('You have collected 200cc!',  self.textPosX, 240)
            self.continueB()
        return

    def noPlayersGUI(self, player):
        pygame.draw.rect(gameDisplay, self.bg, self.sidePos)
        self.sideText('There are currently',  self.textPosX, 20)
        #outputs the number of players still in the game
        self.sideText(str(self.playersP)+ ' players',  self.textPosX, 40)
        self.sideText('Player '+str(player+1), self.textPosX, 80)
        self.sideText('It is your turn',  self.textPosX, 100)
        gameDisplay.blit(pygame.transform.scale(self.playersCounters[player] , (30, 30)),(800, 80))
        #displays the players counter to show which player has what colout counter
        pygame.display.update()

    def banks(self): 
        p = 470 #ouputs all the players bank values at the bottom of the side page
        self.sideText('Players Banks:', self.textPosX, p)
        for i in range(0, self.noOfPlayers):
            self.sideText('Player '+str(i+1)+' = '+str(self.playersBanks[i])+ 'cc',  self.textPosX, p+20)
            p += 20
        pygame.display.update()

    def landedOn(self, player): #ouputs the square the player has landed on
        self.sideText('Player '+str(player+1),  self.textPosX, 100)
        self.sideText('You have landed on:',  self.textPosX, 150)
        self.sideText(self.board[self.playersPlaces[player]-1],  self.textPosX, 170)

    def squares(self, player, dice):
        square = self.playersPlaces[player] #the players square they are currently on
        self.sideText('Player '+str(player+1),  self.textPosX, 100)
        if (square == 6 or square == 16 or square == 26 or square == 36):
            self.companies(player)
        elif (square == 5 or square == 39): 
            self.sideText('You have to pay your bills, pay 100cc', self.textPosX, 190) 
            self.bills(player) #ensures the player pays their bills
            self.continueB()
        elif (square == 13 or square == 29): 
            self.temptations(player, dice)
        elif (square == 31): #moves player to the dentist
            self.sideText('You have been sent to dentist!', self.textPosX, 190)
            self.playersPlaces[player] = 11
            self.inDentist[player] = True
            self.continueB()
        elif (square == 21): 
            self.sideText('Free Candy, you have collected', self.textPosX, 190)
            self.sideText(str(self.freeCandy)+'candy coins!', self.textPosX, 210)
            self.playersBanks[player] += self.freeCandy #adds the money to the players bank
            self.freeCandy = 0 #resets the free candy square
            self.continueB()
        elif (square == 3 or square == 18 or square == 34 or
              square == 8 or square == 23 or square == 37):
            self.candyCards(player)
        elif (square == 1 or square == 11): #nothing happenes when a player lands on these squares
            self.continueB()
            return 
        else: # The sweet squares (the remaining squares)
            self.candySquares(player, square)

    def candyCards(self, player):
        self.sideText('Player '+str(player+1),  self.textPosX, 100)
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
        self.sideText('Your card:',  self.textPosX, 200)
        self.sideText(cards[choice],  self.textPosX, 220) #chooses the random card
        if (choice == 0 or choice == 4 or choice == 7):
            self.bills(player) #uses the bills function to pay the 100cc
        elif (choice == 1):
            self.playersBanks[player] += 200
            #add 200 to the players bank
        elif (choice == 2):
            self.outOfDentistFree[player] += 1
            #adds a card to be used to be released
        else:
            if (choice == 3):
                self.playersPlaces[player] = 1 #moves player to go 
                self.playersBanks[player] += 200 #adds 200 to the players bank
            elif (choice == 5): #moves player in the dentist
                self.playersPlaces[player] = 11
                self.inDentist[player] = True
            elif (choice == 6): #moves player to the sweet factory
                self.playersPlaces[player] = 29
            elif (choice == 8): #moves player 3 places forwards
                self.playersPlaces[player] += 3
            self.sideText('You have landed on:',  self.textPosX, 260)
            self.sideText(self.board[self.playersPlaces[player]-1],  self.textPosX, 280)
        self.continueB()
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
                self.sideText('Player '+str(i+1)+' owns'+ str(howManyOwned) +' companies', self.textPosX, 220)
                toPay = prices[howManyOwned-1] #Pays in regards to how many companies that player owns
                self.sideText('Therefore, player'+ str(player+1), self.textPosX, 240)
                self.sideText('You have to pay'+str(toPay)+'candy coins!', self.textPosX, 260)
                self.playersBanks[player] -= toPay # takes away the money from the current player
                self.sideText('Player '+str(i+1), self.textPosX, 300)
                self.sideText('You have recieved'+str(toPay)+'candy coins!', self.textPosX, 320)
                self.playersBanks[i] += toPay #pays the player who owns the company
        self.continueB()
        return

    def bills(self, player):
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
                    message = 'Player '+str(i+1)+' owns 2 temptations'
                    multiplyBy = 10 #if both of the temptations are owned by the same player
                elif ((self.owned[12] == i)or(self.owned[28] == i)):
                    message = 'Player '+str(i+1)+' owns 1 temptation'
                    multiplyBy = 4 #if one of the temptations is owned
                self.sideText(message, self.textPosX, 190)
                toPay = dice * multiplyBy
                self.sideText('Therefore, you pay '+ str(multiplyBy)+ ' times', self.textPosX, 220) 
                self.sideText('the amount shown on the dice = '+str(toPay), self.textPosX, 240)
                self.playersBanks[player] -= toPay # takes away the money from the current player
                self.sideText('Player '+str(i+1)+' you have recieved:', self.textPosX, 280)
                self.sideText(str(toPay)+ ' candy coins', self.textPosX, 300)
                self.playersBanks[i] += toPay #gives the money to the player who owns that temptation
        self.continueB()
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
                if (sweetInfo[3] == 5): #if there a tub on the square
                    self.sideText('There is a tub on', self.textPosX, 200)
                    self.sideText(self.board[self.playersPlaces[player]-1], self.textPosX, 220)
                    gameDisplay.blit(pygame.transform.scale(self.sweetTubPics , (50, 50)),(720, 270))
                    # display the picture in the position = 720, 270
                else:
                    self.sideText('The number of bags on', self.textPosX, 200)
                    self.sideText(self.board[self.playersPlaces[player]-1], self.textPosX, 220)
                    self.sideText('is '+ str(sweetInfo[3]), self.textPosX, 240)
                    x = 636
                    for i in range(0, sweetInfo[3]):
                        gameDisplay.blit(pygame.transform.scale(self.sweetBagPics , (30, 30)),(x,280))
                        x += 66
                        #displayes the number of bags on the square
                pygame.display.update() #updates the screen
                squaresPriceList = self.landedOnPrices[sweetInfo[2]] 
                toPay = squaresPriceList[sweetInfo[3]] #the price the player has to pay
                self.sideText('Therefore you have to pay', self.textPosX, 350)
                self.sideText(str(toPay)+' cc', self.textPosX, 370)
                self.playersBanks[player] -= toPay
                #is the price for the number of bags currently on that square
                outer = sweetInfo[2] #first reference for sweetsOwned
                inner = sweetInfo[4] #second reference for sweetsOwned
                self.sideText('Player '+str(self.sweetsOwned[outer][inner]+1)+' you have recieved:', self.textPosX, 280)
                self.sideText(str(toPay)+ ' candy coins', self.textPosX, 300)
                self.playersBanks[self.sweetsOwned[outer][inner]] += toPay
                
        self.continueB()
        return
        

    def buySquare(self, player, price):
        self.sideText('The price of', self.textPosX, 200)
        self.sideText(self.board[self.playersPlaces[player]-1], self.textPosX, 220)
        self.sideText('is '+str(price)+'cc', self.textPosX, 240)
        self.sideText('Would you like to buy it?', self.textPosX, 270)
        gameDisplay.blit(pygame.transform.scale(self.yesOption, (self.oSize,self.oSize)),(680,300))
        #scales and positions the yes button
        gameDisplay.blit(pygame.transform.scale(self.noOption, (self.oSize,self.oSize)),(780,300))
        #scales and positions the no button
        pygame.display.update()
        while True:
            self.toQuit()
            #if the yes button is clicked
            click = self.click(680, 300, self.oSize, self.oSize)
            if click == True:
                #the player has briught the squaere
                self.owned[self.playersPlaces[player]-1] = player
                self.playersBanks[player] -= price
                self.sideText('You have brought the square!', self.textPosX, 400)
                return True
            #if the no button is clicked
            click = self.click(780, 300, self.oSize, self.oSize)
            if click == True:
                #the square has not been brought
                return False

    def dentist(self, player):
        denPos = []
        boxPos = 625
        no = 3 #no of options
        clicked = False
        self.clearSideScreen()
        self.sideText('Player'+ str(player+1)+', you are in the dentist,', self.textPosX, 150)
        self.sideText('To be released you have 3 options:', self.textPosX, 170)
        #creates the 3 buttons
        for i in range(0,3):
            pygame.draw.rect(gameDisplay, self.dCButtons,[boxPos, self.denOutPos[i], 250, 20])
        for j in range(0,3):
            d = self.textF(str(self.outDentistText[j]), self.text)
            denPos.append(d)
        for k in range(0,3):
            denPos[k][1].center = ((boxPos+(250/2)),(self.denOutPos[k]+(20/2)))
            gameDisplay.blit(denPos[k][0], denPos[k][1])
        pygame.display.update()
        if(self.outOfDentistFree[player] == 0): #if the player has no card
            pygame.draw.rect(gameDisplay, self.black,[boxPos,self.denOutPos[2],250,20])
            #draw a rectangle over option 3
            pygame.display.update()
            no = 2 #no of option now equal 2
        while (clicked == False):
            self.toQuit()
            for m in range(0,no): #for every option
                y = self.denOutPos[m]
                click = self.click(boxPos, y, 250, 20)
                #if m option is clicked
                if (click == True):
                    time.sleep(1)
                    option = m + 1 #chosen option
                    self.clearSideScreen()
                    clicked = True
        self.sideText('Player'+ str(player+1), self.textPosX, 100)
        if (option == 1): #Pays 50cc to be released
            self.sideText('You\'ve payed 50 cc and', self.textPosX, 230)
            self.playersBanks[player] -= 50
            self.freeCandy += 50 #adds  to free candy square
            self.inDentist[player] = False #no longer in the dentist
        elif (option == 2): #tries to role a double
            dice = Game().diceGUI(player) #roles the dice
            time.sleep(0.5)
            pygame.display.update()
            if (dice[0] == True):
                self.sideText('You\'ve rolled a double!', self.textPosX, 230)
                self.inDentist[player] = False #no longer in the dentist
            else:
                self.sideText('You\'ve not rolled a double!', self.textPosX, 230)
                self.sideText('Therefore, are not released from the dentist!', self.textPosX, 250)
                self.continueB() #continue button
                return
        elif (option == 3): #used a get out of dentist free card
            self.sideText('You\'ve used of your cards', self.textPosX, 230)
            self.outOfDentistFree[player] -= 1 #has one less card now
            self.inDentist[player] = False #no longer in the dentist
        self.sideText('are now released from the dentist!', self.textPosX, 250)
        self.continueB() #continue button
        return

    def continueB(self):
        c = self.textF('Continue', self.text)
        pygame.draw.rect(gameDisplay, self.continueButton,[self.textPosX, 560, 100, 20])
        c[1].center = ((self.textPosX+(100/2)),(560+(20/2)))
        gameDisplay.blit(c[0], c[1])
        #creates the continue button
        pygame.display.update()

        while True:
            self.toQuit()
            click = self.click(self.textPosX, 560, 100, 20)
            if click == True:
                # when clicked the screen is cleared and it returns back to the function
                time.sleep(0.2)
                self.clearSideScreen()
                pygame.display.update()
                return

    def listProperties(self, player):
        l = self.textF('List My Properties', self.text)
        pygame.draw.rect(gameDisplay, self.continueButton,[675, 200, 150, 20])
        l[1].center = ((675+(150/2)),(200+(20/2)))
        gameDisplay.blit(l[0], l[1])
        # button for listing propeties
        c = self.textF('Continue', self.text)
        pygame.draw.rect(gameDisplay, self.continueButton,[self.textPosX, 560, 100, 20])
        c[1].center = ((self.textPosX+(100/2)),(560+(20/2)))
        gameDisplay.blit(c[0], c[1])
        #button to continue to next step
        pygame.display.update()
        while True:
            self.toQuit()
            click = self.click(675, 200, 150, 20)
            #if click is true, the player wants to view their properties
            if click == True:
                time.sleep(0.2)
                self.clearSideScreen()
                self.sideText('Player'+ str(player+1), self.textPosX, 100)
                y = 130
                for i in range(0, len(self.owned)):
                    #looks through owned for the players numbers
                    if (self.owned[i] == player):
                        # if square i is equal to player, the name of the square is outputed
                        self.sideText(self.board[i], self.textPosX, y)
                        y += 20 #adjusts the y axis, so squares aren't written over eachother
                q = self.textF('Quit', self.text)
                pygame.draw.rect(gameDisplay, self.continueButton,[675, 550, 150, 20])
                q[1].center = ((675+(150/2)),(550+(20/2)))
                gameDisplay.blit(q[0], q[1])
                #quit button
                pygame.display.update()
                while True:
                    self.toQuit()
                    click = self.click(675, 550, 150, 20)
                    #if clicked returns to the function
                    if click == True:
                        self.clearSideScreen() #clears the input/output screen
                        return
            click = self.click(self.textPosX, 560, 100, 20)
            #if the click is true, the player is continuing 
            if click == True:
                time.sleep(0.2)
                self.clearSideScreen()
                pygame.display.update()
                return
     
            
sWidth = 900 #screen width and height
sHeight = 600
gameDisplay = pygame.display.set_mode((sWidth,sHeight))            
GUIfunctions().createScreen()
Main().go()




