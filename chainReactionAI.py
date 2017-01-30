'''
https://www.hackerearth.com/problem/multiplayer/chainreaction/
Solution Link: https://www.hackerearth.com/submission/7019905/
'''
import os
import random

gameBoard = [[str(00) for i in range(0,5)] for i in range(0,5)]

isUnstable = 4 


def detectBombLoc(playerTurn):
    opponentsPlayer = findOppLocation(playerTurn);
    print("OPPONENT PLAYER ")
    print(opponentsPlayer)
    
    
    possiblePlantation = []
    
    for i in opponentsPlayer:
        print("EACH OPPONENT")
        
        
        if ( int(i[0]) <= 0  ):
            '''ROW IS ZERO '''
            
            tempRowCheck = int(i[0])
            tempColCheck = int(i[1]) + 1
            
           
            
            if ((tempColCheck >= 0 and tempColCheck <= 4) and (tempRowCheck >= 0 and tempRowCheck <= 4) ):
                ''' Sanitizing the range of values in game board '''
                print(" Value at row " + str(tempRowCheck) + " and col "+ str(tempColCheck)+ " =="+ str(gameBoard[ tempRowCheck ][ tempColCheck ][0]) )
                if( (int(gameBoard[ tempRowCheck ][ tempColCheck ][0]) == int(playerTurn)) or ( int(gameBoard[ tempRowCheck ][ tempColCheck ][0]) == 0 )):
                   ''' detect whether our player is at bombard loc '''
                   possiblePlantation.append(str(i[0]) +  str( int(i[1]) + 1 ))

            tempRowCheck = int(i[0])
            tempColCheck = int(i[1]) - 1
            
            if ((tempColCheck >= 0 and tempColCheck <= 4) and (tempRowCheck >= 0 and tempRowCheck <= 4) ):
                ''' Sanitizing the range of values in game board '''
                print(" Value at row " + str(tempRowCheck) + " and col "+ str(tempColCheck)+ " =="+ str(gameBoard[ tempRowCheck ][ tempColCheck ][0]) )
                if( (int(gameBoard[ tempRowCheck ][ tempColCheck ][0]) == int(playerTurn)) or ( int(gameBoard[ tempRowCheck ][ tempColCheck ][0]) == 0 )):
                   ''' detect whether our player is at bombard loc '''
                   possiblePlantation.append(str(i[0]) +  str( int(i[1]) + 1 ))            
            
        print("Possible Plantation")
        print(possiblePlantation)
    
    
def findOppLocation(playerTurn):
    if int(playerTurn) == 1 :
        opponent = 2
    else :
        opponent = 1
    
    oppositionLoc = []    
    for i in range(0,5):
        for j in range(0,5):
            
            if int(gameBoard[i][j][0]) == int(opponent):
                #print(str(i) +"  "+ str(j) + "\n")
                oppositionLoc.append(str(i)+str(j))
    
    return oppositionLoc

def possibleLocFinder(playerTurn):
    posLocTemp = []
    for i in range(0,5):
        for j in range(0,5):
            if( int(gameBoard[i][j][0]) == 0 ) or ( int(gameBoard[i][j][0]) == int(playerTurn)):
                posLocTemp.append(str(i) + str(j))
    return posLocTemp

#MATRIX INPUT

gameRow = str(input())
for values in range(0,4):
    #print(values)
    gameRow = gameRow + " " + str(input())
    #print("game" + gameRow)

firstRow = str(gameRow).split(" ")
temp = 0
for i in range(0,5):
    for j in range(0,5):
        gameBoard[i][j] = firstRow[temp]
        temp = temp + 1
        
playerTurn = input()
#GET ALL POSSIBLE LOCATION
possibleLocOfPlacing = possibleLocFinder(playerTurn)
#print(possibleLocOfPlacing)

#SELECTING RANDOM 
randomChoice = random.randint(0,len(possibleLocOfPlacing) - 1)

#Select the updating cell
whichCellToUpdateRow = int(possibleLocOfPlacing[randomChoice][0])
whichCellToUpdateCol = int(possibleLocOfPlacing[randomChoice][1])

#print("UPDATING " + str(possibleLocOfPlacing[randomChoice][0]) + str(possibleLocOfPlacing[randomChoice][1]))

#CHECk WHETHER EMPTY OR SOME THING EXIST THERE
if (int(gameBoard[ whichCellToUpdateRow ][ whichCellToUpdateCol ][0]) == 0) or ( int(gameBoard[ whichCellToUpdateRow ][ whichCellToUpdateCol ][0]) == playerTurn) :
    #it's empty
    convertItToEditable = list(gameBoard[ whichCellToUpdateRow ][ whichCellToUpdateCol ])
    convertItToEditable[0] = playerTurn
    convertItToEditable[1] = str(int(gameBoard[ whichCellToUpdateRow ][ whichCellToUpdateCol ][1]) + 1)
    #print("convertItToEditable " + str(convertItToEditable))
    #print(''.join(convertItToEditable))
    
    gameBoard[ whichCellToUpdateRow ][ whichCellToUpdateCol ] = ''.join(convertItToEditable)

print(str(whichCellToUpdateRow)+" "+str(whichCellToUpdateCol))



    #print(gameBoard)

'''
print(gameBoard)  
'''


