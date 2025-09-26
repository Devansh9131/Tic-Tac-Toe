import random
import sys

def board():
    print(f'''
        {l[0]}|{l[1]}|{l[2]}
        - - -
        {l[3]}|{l[4]}|{l[5]}
        - - - 
        {l[6]}|{l[7]}|{l[8]}
        ''')
    
def Pl_move(ch):
    if ch not in l:
        print("Please enter valid move.")
        loop()
        
    l.insert(ch,"X")
    l.remove(ch)
    ail.remove(ch)
    board()

    if(l[0] == l[1] == l[2] == "X" or l[3] == l[4] == l[5] == "X" or l[6]== l[7] == l[8] == "X" or l[0] == l[3] == l[6] == "X" or l[1] == l[4] == l[7] == "X" or l[2] == l[5] == l[8] == "X" or l[0] == l[4] == l[8] == "X" or l[2] == l[4] == l[6] == "X" ):
        print("congrats, you Win.")
        sys.exit()

def AI_move():

    print("After AI's move: ")
    ra = random.choice(ail)
    l.insert(ra,"O")
    l.remove(ra)
    ail.remove(ra)
    board()
    if(l[0] == l[1] == l[2] == "O" or l[3] == l[4] == l[5] == "O" or l[6]== l[7] == l[8] == "O" or l[0] == l[3] == l[6] == "O" or l[1] == l[4] == l[7] == "O" or l[2] == l[5] == l[8] == "O" or l[0] == l[4] == l[8] == "O" or l[2] == l[4] == l[6] == "O" ):
        print("You lose, Try again.")
        sys.exit()


def loop():
    if(len(ail) != 0):

        ch = int(input("Enter your choice: "))
        if(ch<1 or ch>9):
            print("Please enter valid move.")

        else:
            Pl_move(ch)
            AI_move()

        loop()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ail = [1, 2, 3, 4, 5, 6, 7, 8, 9]

board()

print("choice no. form 1-9\n")

loop()

print("The game ends with draw, Try again.")

