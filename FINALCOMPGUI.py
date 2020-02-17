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
        self.boardPos = [[10, 10], [75, 10], [125, 10], [175,10], [225,10],
                         [275,10], [325,10], [375,10], [425,10], [475, 10],
                         [545, 10],[545, 80], [545, 125], [545, 175], [545, 225],
                         [545, 275], [545, 325], [545, 375], [545, 425],
                         [545, 475], [545, 545],[475, 545], [425,545], [375,545],
                         [325,545], [275,545], [225,545], [175,545], [125, 545],
                         [75, 545], [10, 545], [10, 475], [10, 425], [10, 375],
                         [10, 325], [10, 275], [10, 225], [10, 177], [10, 125], [10, 80]]
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
        self.board = ['Go', 'Love Hearts', self.candyCard, 'Parma Violets', 'Sugar tax',
                      'Maoams', 'Gummy Bear', self.candyCard, 'Gum Drops', 'Wine Gums', ' the Dentist',
                      'Strawberry Laces', 'Candy Shop', 'Strawberry Pencils', 'Rainbow Belts',
                      'Haribos', 'Chewits', self.candyCard, 'Starbursts', 'Fruittellas', 'Free Candy',
                      'Cola Bottles', self.candyCard, 'Fizzy Cola Bottles', 'Fizzy Blue Bottles',
                      'Chupa Chups', 'Giant Strawberry', 'Giant Cherries', 'Sweet Factory', 'Gummy Snakes',
                      'Go to the dentist','Fox Glaciers', 'Humbugs', self.candyCard, 'Imperial Mints',
                      'Drumsticks', self.candyCard, 'Nerds', 'Medical Bill', 'Popping Candy']
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
        self.sweetsNos = [[2,4],[7,9,10],[12,14,15],[17,19,20],[22,24,25],[27,28,30],[32,33,35],[38,40]]
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
                    #layout --> = {Location: [price, bagPrices ref, landedOnPrices ref,
                                    #noOfBags, inner array number], ….
        self.sweetsOwned = [['',''],['','',''],['','',''],['','',''],['','',''],['','',''],
                            ['','',''],['','']]
        self.computerPlayer = 0 #computer player = player 1
        
    
    def players(self):
        self.sideText('How many players?',  self.textPosX, 100)
        #below creates 5 buttons with numbers 2-6 and positions them in the correct place
        for k in range(0,5): #creates the rectangle 
            pygame.draw.rect(gameDisplay, self.pCButtons,[self.noPlayersPos[k],150,20,20])
        for j in range(0,5): #adds the text on the rectangle
            p = self.textF(str(j+1), self.text) 
            self.noPlayers.append(p)
        for i in range(0,5): #centers the text
            self.noPlayers[i][1].center = ((self.noPlayersPos[i]+(20/2)),(150+(20/2)))
            gameDisplay.blit(self.noPlayers[i][0], self.noPlayers[i][1])
        self.sideText('Computer Player = Player 1',  self.textPosX, 200)
        pygame.display.update()
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
        self.computerPlayer = 0 ################
        
    def roleDice(self, player):
        self.sideText('Click below to role the dice:', 300, 350)
        gameDisplay.blit(pygame.transform.scale(self.dice, (self.dSize,self.dSize)),(self.dPosX,self.dPosY))
        #scales the picture of the dice and located it near the middle of the board
        pygame.display.update()
        if (player == self.computerPlayer): #if player = computer player, simulate a dice role
            time.sleep(1) #simulates a dice role
            pygame.draw.rect(gameDisplay, self.black,[self.dPosX,self.dPosY,self.dSize,self.dSize])
            pygame.display.update()
            time.sleep(0.5)
            dice = self.calculateDice(player)
            return dice
        else:
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
            
            if(player == self.computerPlayer): # buys a bag if there is more than 500cc in the bank
                if (self.playersBanks[self.computerPlayer] > 500):
                    time.sleep(1)
                    pygame.draw.rect(gameDisplay, self.black,[680, 300, self.oSize, self.oSize])
                    pygame.display.update()
                    time.sleep(0.5)
                    self.clearSideScreen()
                    self.chooseOption(self.computerPlayer, canAddNames, canAddNos)
                    return
                else: #computer player clicks quit
                    time.sleep(1)
                    pygame.draw.rect(gameDisplay, self.black,[780, 300, self.oSize, self.oSize])
                    pygame.display.update()
                    time.sleep(0.5)
                    self.clearSideScreen()
                    return
            else:
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
            if (player == self.computerPlayer): 
                time.sleep(1)
                option = random.randint(0, len(opPos)-1)
                pygame.draw.rect(gameDisplay, self.black,[opPos[option][0], opPos[option][1], 100, 20])
                pygame.display.update()
                time.sleep(0.5)
                self.printsAdd(option, self.computerPlayer, canAddNos)
                return
            else:
                click = self.click(self.textPosX, 500, 100, 20)
                if click == True: #quit
                    self.clearSideScreen()
                    return
                for t in range(0, len(opPos)-1):
                    click = self.click(opPos[t][0], opPos[t][1], 100, 20)
                    if (click == True):
                        time.sleep(0.2)
                        pygame.draw.rect(gameDisplay, self.bg, self.sidePos)
                        self.printsAdd(t, player, canAddNos)
                        return
                        


    def printsAdd(self, number, player, canAddNos):
        self.clearSideScreen()
        print(canAddNos)
        addTo = canAddNos[number][0]
        for v in range (0, len(canAddNos[number])):
            square = canAddNos[number][v]
            if (self.sweets[addTo][3] > self.sweets[square][3]):
                addTo = canAddNos[number][v]
        self.sweets[addTo][3] += 1
        self.playersBanks[player] -= self.bagPrices[self.sweets[addTo][1]]
        
        self.sideText('Player '+ str(player+1), self.textPosX, 100)
        if (self.sweets[addTo][3] == 5):
            self.sideText('You have added a tub to:', self.textPosX, 140)
            self.sideText(self.board[addTo-1], self.textPosX, 160)
            gameDisplay.blit(pygame.transform.scale(self.sweetTubPics , (50, 50)),(720, 200))              
        else:
            self.sideText('You have added a bag to:', self.textPosX, 140)
            self.sideText(self.board[addTo-1], self.textPosX, 160)
            self.sideText('The number of bags:', self.textPosX, 200)
            x = 636
            for i in range(0, self.sweets[addTo][3]):
                gameDisplay.blit(pygame.transform.scale(self.sweetBagPics , (30, 30)),(x, 250))
                x += 66
            self.continueB(player)
            return 
             

    def pastGoCheck(self, player):
        if (self.playersPlaces[player] > 40): # when they are the start of the board
            self.playersPlaces[player] -= 40
            self.playersBanks[player] += 200
            self.clearSideScreen()
            self.sideText('Player '+str(player+1),  self.textPosX, 180)
            self.sideText('You have passed go!',  self.textPosX, 220)
            self.sideText('You have collected 200cc!',  self.textPosX, 240)
            self.continueB(player)
        return

    def noPlayersGUI(self, player):
        pygame.draw.rect(gameDisplay, self.bg, self.sidePos)
        self.sideText('There are currently',  self.textPosX, 20)
        self.sideText(str(self.playersP)+ ' players',  self.textPosX, 40)
        self.sideText('Player '+str(player+1), self.textPosX, 80)
        if (player == self.computerPlayer):
            self.sideText('It\'s the computers turn',  self.textPosX, 100)
        else:
            self.sideText('It is your turn',  self.textPosX, 100)
        gameDisplay.blit(pygame.transform.scale(self.playersCounters[player] , (30, 30)),(850, 80))
        pygame.display.update()

    def banks(self):
        p = 470
        self.sideText('Players Banks:', self.textPosX, p)
        for i in range(0, self.noOfPlayers):
            self.sideText('Player '+str(i+1)+' = '+str(self.playersBanks[i])+ 'cc',  self.textPosX, p+20)
            p += 20
        pygame.display.update()

    def landedOn(self, player):
        self.sideText('Player '+str(player+1),  self.textPosX, 100)
        self.sideText('You have landed on:',  self.textPosX, 150)
        self.sideText(self.board[self.playersPlaces[player]-1],  self.textPosX, 170)

    def squares(self, player, dice):
        square = self.playersPlaces[player]
        self.sideText('Player '+str(player+1),  self.textPosX, 100)
        if (square == 6 or square == 16 or square == 26 or square == 36): 
            self.companies(player)
        elif (square == 5 or square == 39): 
            self.sideText('You have to pay your bills, pay 100cc', self.textPosX, 190)
            self.bills(player)
            self.continueB(player)
        elif (square == 13 or square == 29): 
            self.temptations(player, dice)
        elif (square == 31): 
            self.sideText('You have been sent to dentist!', self.textPosX, 190)
            self.playersPlaces[player] = 11
            self.inDentist[player] = True
            self.continueB(player)
        elif (square == 21): 
            self.sideText('Free Candy, you have collected', self.textPosX, 190)
            self.sideText(str(self.freeCandy)+'candy coins!', self.textPosX, 210)
            self.playersBanks[player] += self.freeCandy
            self.freeCandy = 0
            self.continueB(player)
        elif (square == 3 or square == 18 or square == 34 or
              square == 8 or square == 23 or square == 37):
            self.candyCards(player)
        elif (square == 1 or square == 11): #nothing happenes when a player lands on these squares
            self.continueB(player)
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
        choice = random.randint(0,8)
        self.sideText('Your card:',  self.textPosX, 200)
        self.sideText(cards[choice],  self.textPosX, 220)
        if (choice == 0 or choice == 4 or choice == 7):
            self.bills(player)
        elif (choice == 1):
            self.playersBanks[player] += 200
        elif (choice == 2):
            self.outOfDentistFree[player] += 1
        else:
            if (choice == 3):
                self.playersPlaces[player] = 1
                self.playersBanks[player] += 200
            elif (choice == 5):
                self.playersPlaces[player] = 11
                self.inDentist[player] = True
            elif (choice == 6):
                self.playersPlaces[player] = 29
            elif (choice == 8):
                self.playersPlaces[player] += 3
            self.sideText('You have landed on:',  self.textPosX, 260)
            self.sideText(self.board[self.playersPlaces[player]-1],  self.textPosX, 280)
        time.sleep(1)
        self.continueB(player)
        return
    
    def companies(self, player):
        places = [5, 15, 25, 35]
        prices = [25, 50, 100, 200]
        howManyOwned = 0
        i = self.owned[self.playersPlaces[player]-1]
        # i = the player that owns the square the other player is on
        if(i == 'empty'):
            if (player == self.computerPlayer): ################
                self.compBuySquare(200, places)
            else:
                self.buySquare(player, 200)
        else:
            if (i != player):
                for j in range(0, 4):
                    if (self.owned[places[j]] == i):
                        howManyOwned += 1
                self.sideText('Player '+str(i+1)+' owns'+ str(howManyOwned) +' companies', self.textPosX, 220)
                toPay = prices[howManyOwned-1]
                self.sideText('Therefore, player'+ str(player+1), self.textPosX, 240)
                self.sideText('You have to pay'+str(toPay)+'candy coins!', self.textPosX, 260)
                self.playersBanks[player] -= toPay
                self.sideText('Player '+str(i+1), self.textPosX, 300)
                self.sideText('You have recieved'+str(toPay)+'candy coins!', self.textPosX, 320)
                self.playersBanks[i] += toPay
        self.continueB(player)
        return

    def bills(self, player):
        self.playersBanks[player] -= 100
        self.freeCandy += 100
        return

    def temptations(self, player, dice):
        places = [12, 28]
        if(self.owned[self.playersPlaces[player]-1] == 'empty'):
            if (player == self.computerPlayer):
                self.compBuySquare(200, places) ################
            else:
                self.buySquare(player, 200)
        else:
            if (self.owned[self.playersPlaces[player]-1] != player):
                i = self.owned[self.playersPlaces[player]-1]
                if ((self.owned[12] == i)and(self.owned[28] == i)):
                    message = 'Player '+str(i+1)+' owns 2 temptations'
                    multiplyBy = 10
                elif ((self.owned[12] == i)or(self.owned[28] == i)):
                    message = 'Player '+str(i+1)+' owns 1 temptation'
                    multiplyBy = 4
                self.sideText(message, self.textPosX, 190)
                toPay = dice * multiplyBy
                self.sideText('Therefore, you pay '+ str(multiplyBy)+ ' times', self.textPosX, 220) 
                self.sideText('the amount shown on the dice = '+str(toPay), self.textPosX, 240)
                self.playersBanks[player] -= toPay
                self.sideText('Player '+str(i+1)+' you have recieved:', self.textPosX, 280)
                self.sideText(str(toPay)+ ' candy coins', self.textPosX, 300)
                self.playersBanks[i] += toPay
        self.continueB(player)
        return

    def candySquares(self, player, square):
        ownedBy = self.owned[self.playersPlaces[player]-1]
        sweetInfo = self.sweets[square]
        if(ownedBy == 'empty'):
            if (player == self.computerPlayer): ##############################
                brought = self.compBuySquare(sweetInfo[0], square)
            else:
                brought = self.buySquare(player, sweetInfo[0])
            if (brought == True):
                inner = sweetInfo[4]
                outer = sweetInfo[2]
                self.sweetsOwned[outer][inner] = player
        else:
            if (ownedBy != player):
                if (sweetInfo[3] == 5):
                    self.sideText('There is a tub on', self.textPosX, 200)
                    self.sideText(self.board[self.playersPlaces[player]-1], self.textPosX, 220)
                    gameDisplay.blit(pygame.transform.scale(self.sweetTubPics , (50, 50)),(720, 270))              
                else:
                    self.sideText('The number of bags on', self.textPosX, 200)
                    self.sideText(self.board[self.playersPlaces[player]-1], self.textPosX, 220)
                    self.sideText('is '+ str(sweetInfo[3]), self.textPosX, 240)
                    x = 636
                    for i in range(0, sweetInfo[3]):
                        gameDisplay.blit(pygame.transform.scale(self.sweetBagPics , (30, 30)),(x,280))
                        x += 66
                pygame.display.update()                
                squaresPriceList = self.landedOnPrices[sweetInfo[2]]
                toPay = squaresPriceList[sweetInfo[3]]
                self.sideText('Therefore you have to pay', self.textPosX, 350)
                self.sideText(str(toPay)+' cc', self.textPosX, 370)
                self.playersBanks[player] -= toPay
                inner = sweetInfo[4]
                outer = sweetInfo[2]
                self.sideText('Player '+str(self.sweetsOwned[outer][inner]+1)+
                              ' you have recieved:', self.textPosX, 280)
                self.sideText(str(toPay)+ ' candy coins', self.textPosX, 300)
                self.playersBanks[self.sweetsOwned[outer][inner]] += toPay
                
        self.continueB(player)
        return

    def buyingDisplay(self, player, price):
        self.sideText('The price of', self.textPosX, 200)
        self.sideText(self.board[self.playersPlaces[player]-1], self.textPosX, 220)
        self.sideText('is '+str(price)+'cc', self.textPosX, 240)
        self.sideText('Would you like to buy it?', self.textPosX, 270)
        gameDisplay.blit(pygame.transform.scale(self.yesOption, (self.oSize,self.oSize)),(680,300))
        gameDisplay.blit(pygame.transform.scale(self.noOption, (self.oSize,self.oSize)),(780,300))
        pygame.display.update()
        

    def buySquare(self, player, price):
        self.buyingDisplay(player, price)
        while True:
            self.toQuit()
            click = self.click(680, 300, self.oSize, self.oSize)
            if click == True:
                self.owned[self.playersPlaces[player]-1] = player
                self.playersBanks[player] -= price
                self.sideText('You have brought the square!', self.textPosX, 400)
                return True
            click = self.click(780, 300, self.oSize, self.oSize)
            if click == True:
                return False

    def compBuySquare(self, price, places): 
        self.buyingDisplay(self.computerPlayer, price)
        howManyOwned = 0
        decision = False
        try: #checks to see if ist as temptation or company
            length = len(places)
        except TypeError: #or a candy square
            length = 1
            
        if (length == 1): #for candy squares
            inList = self.sweets[places][2]-1
            for i in range(0, len(self.sweetsNos[inList])-1):
                if (self.owned[self.sweetsNos[inList][i]-1] == self.computerPlayer):
                    howManyOwned += 1 #checks to see how many squares in that colour are owned
            if (howManyOwned > 1): #if the computer player already owns 1 square in that colour
                decision = True #buy the square
            elif (self.playersBanks[self.computerPlayer] > 600): #if the back is bigger than 600cc
                decision = True #buy the square
            #if not decision remains false
                
        else:
            for i in range(0, length): #for companies and temptations
                if (self.owned[places[i]] == 0): #if already owns comp/temp squares
                        howManyOwned += 1 #implements howManyOwned
            if ((howManyOwned == (length - 1)) or(howManyOwned == (length/2))):
                decision = True #if the player owns more that half, buy the square
            elif (self.playersBanks[self.computerPlayer] > 500):
                decision = True #if the players bank is over 500cc, buy the square
            #if not decision remains false
                
        if (decision == True): #square is brought
            time.sleep(1)
            pygame.draw.rect(gameDisplay, self.black,[680,300,self.oSize,self.oSize])
            pygame.display.update()
            time.sleep(0.5)
            self.owned[self.playersPlaces[self.computerPlayer]-1] = self.computerPlayer
            self.playersBanks[self.computerPlayer] -= price
            self.sideText('You have brought the square!', self.textPosX, 400)
            return True
        if (decision == False): #the square has not been brought
            time.sleep(1)
            pygame.draw.rect(gameDisplay, self.black,[780,300,self.oSize,self.oSize])
            pygame.display.update()
            time.sleep(0.5)
            return False
            
    def dentist(self, player):
        denPos = []
        boxPos = 625
        no = 3
        clicked = False
        self.clearSideScreen()
        self.sideText('Player'+ str(player+1)+', you are in the dentist,', self.textPosX, 150)
        self.sideText('To be released you have 3 options:', self.textPosX, 170)
        for i in range(0,3):
            pygame.draw.rect(gameDisplay, self.dCButtons,[boxPos, self.denOutPos[i], 250, 20])
        for j in range(0,3):
            d = self.textF(str(self.outDentistText[j]), self.text)
            denPos.append(d)
        for k in range(0,3):
            denPos[k][1].center = ((boxPos+(250/2)),(self.denOutPos[k]+(20/2)))
            gameDisplay.blit(denPos[k][0], denPos[k][1])
        pygame.display.update()
        
        if(self.outOfDentistFree[player] == 0):
            pygame.draw.rect(gameDisplay, self.black,[boxPos,self.denOutPos[2],250,20])
            pygame.display.update()
            no = 2
            
        if (player == self.computerPlayer):# if the player is the computer player
            if(self.outOfDentistFree[0] > 0): #checks to see if it has a card
                option = 3 # if it does, option 3 is choosen
                pos = [625, 280, 250, 20] #the positions of the option buttons (option 3)
            elif(self.playersBanks[0] < 100): #if players bank is less that 100cc
                option = 2 #option 2 is chosen
                pos = [625, 240, 250, 20] #option 2 position
            else: 
                option = 1 #option 1 is chose
                pos = [625, 200, 250, 20] #option 1 position
            time.sleep(1) # simulating clicking the button
            pygame.draw.rect(gameDisplay, self.black, pos)
            pygame.display.update()
            time.sleep(0.5)
            
        else: #for thr human players:
            while (clicked == False):
                self.toQuit()
                for m in range(0,no):
                    y = self.denOutPos[m]
                    click = self.click(boxPos, y, 250, 20)
                    if (click == True):
                        time.sleep(1)
                        option = m + 1
                        clicked = True
        self.clearSideScreen()
        self.sideText('Player'+ str(player+1), self.textPosX, 100)
        if (option == 1):
            self.sideText('You\'ve payed 50 cc and', self.textPosX, 230)
            self.playersBanks[player] -= 50
            self.freeCandy += 50
            self.inDentist[player] = False
        elif (option == 2):
            dice = Game().diceGUI(player)
            time.sleep(0.5)
            pygame.display.update()
            if (dice[0] == True):
                self.sideText('You\'ve rolled a double!', self.textPosX, 230)
                self.inDentist[player] = False
            else:
                self.sideText('You\'ve not rolled a double!', self.textPosX, 230)
                self.sideText('Therefore, are not release from the dentist!', self.textPosX, 250)
                self.continueB()
                return
        elif (option == 3):
            self.sideText('You\'ve used of your cards', self.textPosX, 230)
            self.outOfDentistFree[player] -= 1
            self.inDentist[player] = False
        self.sideText('are now released from the dentist!', self.textPosX, 250)
        self.continueB(player)
        return

    def continueB(self, player):
        c = self.textF('Continue', self.text)
        pygame.draw.rect(gameDisplay, self.continueButton,[self.textPosX, 560, 100, 20])
        c[1].center = ((self.textPosX+(100/2)),(560+(20/2)))
        gameDisplay.blit(c[0], c[1])
        pygame.display.update()
        if (player == self.computerPlayer): #if it is the computer player
            time.sleep(1.5) #simulate button press
            pygame.draw.rect(gameDisplay, self.black,[self.textPosX, 560, 100, 20])
            pygame.display.update()
            time.sleep(1)
        else:
            while True:
                self.toQuit()
                click = self.click(self.textPosX, 560, 100, 20)
                if click == True:
                    time.sleep(0.2)
                    self.clearSideScreen()
                    pygame.display.update()
                    return

    def listProperties(self, player):
        if (player != self.computerPlayer):
            l = self.textF('List My Properties', self.text)
            pygame.draw.rect(gameDisplay, self.continueButton,[675, 200, 150, 20])
            l[1].center = ((675+(150/2)),(200+(20/2)))
            gameDisplay.blit(l[0], l[1])
            
            p = self.textF('List Computer Players Properties', self.text) 
            pygame.draw.rect(gameDisplay, self.continueButton,[625, 240, 250, 20])
            p[1].center = ((625+(250/2)),(240+(20/2)))
            gameDisplay.blit(p[0], p[1])
            
            c = self.textF('Continue', self.text)
            pygame.draw.rect(gameDisplay, self.continueButton,[self.textPosX, 560, 100, 20])
            c[1].center = ((self.textPosX+(100/2)),(560+(20/2)))
            gameDisplay.blit(c[0], c[1])
            pygame.display.update()
            while True:
                self.toQuit()
                click = self.click(self.textPosX, 560, 100, 20)
                if click == True: #if continue is clicked
                    time.sleep(0.2)
                    self.clearSideScreen()
                    pygame.display.update()
                    return
                #click to view the human player properties
                click = self.click(675, 200, 150, 20)
                if click == True:
                    time.sleep(0.2)
                    self.clearSideScreen()
                    self.sideText('Player'+ str(player+1), self.textPosX, 100)
                    self.viewingProperties(player)
                    return
                #clicked on view the human player properties
                click = self.click(625, 240, 250, 20)
                if click == True:
                    time.sleep(0.2)
                    self.clearSideScreen()
                    self.sideText('Computer Player', self.textPosX, 100)
                    self.viewingProperties(0)
                    return

    def viewingProperties(self, player):
        y = 130 #y axis starts at 130
        for i in range(0, len(self.owned)): #for the length of all squares
            if (self.owned[i] == player): #if the property is owned by the player
                self.sideText(self.board[i], self.textPosX, y)
                #insert the name
                y += 20 #increment the yaxis 
        q = self.textF('Quit', self.text)
        pygame.draw.rect(gameDisplay, self.continueButton,[675, 550, 150, 20])
        q[1].center = ((675+(150/2)),(550+(20/2)))
        gameDisplay.blit(q[0], q[1])
        #quit button
        pygame.display.update()
        while True:
            self.toQuit()
            click = self.click(675, 550, 150, 20)
            #if clicked is returned
            if click == True: #quit
                self.clearSideScreen()
                return
        
           

sWidth = 900 #screen width and height
sHeight = 600
gameDisplay = pygame.display.set_mode((sWidth,sHeight))            
GUIfunctions().createScreen()
Main().go()




