"""
Tic-Tac_Toe
"""

import sys
import random


row1 = [7,8,9]
row2 = [4,5,6]
row = [1,2,3]
row2.extend(row1)
row.extend(row2)
print("Player X is you.\nPlayer Y is the computer.")


def gameBoard():
    
    print()
    print(f"| {row[6]} | {row[7]} | {row[8]} |")          #row1
    print("-------------")          
    print(f"| {row[3]} | {row[4]} | {row[5]} |")          #row2      
    print("-------------")
    print(f"| {row[0]} | {row[1]} | {row[2]} |")          #row1
    print()


def Player1():
    print("\nX's turn, ")
    
    try:
        position_given = int(input("[+] Enter Position for X => "))
    except Exception as e:
        print("[!] Wrong Input, Please try again.")
        return 1
    
    pos = position_given - 1

    try:
        if (row[pos]=='X' or row[pos]=='O'):
            print("[!] Space Occuplied by another player.")
            return 1
        
        row[pos] = 'X'
        gameBoard()
        
    except Exception as e:
        print("Err Occured")
        return 1
   
    
def Player2():
    print("\nY's turn, Generating Input... ")
    # index_given = int(input("[+] Enter Position for Y => "))
    index_given = random.randrange(1,10)
    pos = index_given - 1

    try:
        if (row[pos]=='X' or row[pos]=='O'):
            print("[!] Space Occuplied by another player, Try Again.")
            return 1
        
        row[pos] = 'Y'
        gameBoard()
        
    except Exception as e:
        print("Err Occured")
        return 1
    
def rowWin():
    for k in range(0,9,3):
        rowFlagX = (row[k] == row[k+1] == row[k+2] == 'X')
        rowFlagY = (row[k] == row[k+1] == row[k+2] == 'Y')
        if rowFlagX or rowFlagY:
            break
        
    if rowFlagX   : return "X"
    elif rowFlagY : return "Y"
    else          : pass
    

def colWin():
    for k in range(0,3):
        colFlagX = (row[k] == row[k+3] == row[k+6] == 'X')
        colFlagY = (row[k] == row[k+3] == row[k+6] == 'Y')
        if colFlagX or colFlagY:
            break
        
    if colFlagX:
        return "X"
    elif colFlagY:
        return "Y"
    else:
        pass
    

def diagWin():
    l_Flag = row[0] == row[4] == row[8]
    r_Flag = row[2] == row[4] == row[6]
    
    if l_Flag:
        winner = row[0]
    elif r_Flag:
        winner = row[2]
    else:
        winner = 0
        
    return winner
    
    
    
def Win():
    if rowWin():
        winner = rowWin()
    elif colWin():
        winner = colWin()
    elif diagWin():
        winner = diagWin()
    else:
        pass
        
    if rowWin() or colWin() or diagWin():
        print(f"[+] Game End : '{winner}' won the game.")
        sys.exit()
        
    

def Start():
    turn = 0
    for i in range(9):
        # print(turn)
        
        if turn % 2 == 0:
            exp = Player1()
            if exp:
                Player1()
        else:
            exp2 = Player2()
            if exp2:
                Player2()
        
        Win()
        turn = turn + 1


gameBoard()    
Start()
