#Tic Tac Toe 
def check_horizontal(b):
    for i in range(3):
        j = 0
        if (b[i][j] == b[i][1] == b[i][2] == 'O') or (b[i][j] == b[i][1] == b[i][2] == 'X'):
            return 1
    return 0

def check_vertical(b):
    for i in range(3):
        j = 0
        if (b[j][i] == b[j+1][i] == b[j+2][i] == 'O') or (b[j][i] == b[j+1][i] == b[j+2][i] == 'X'):
            return 1
    return 0

def check_diag(b):
    if ((b[0][0] == b[1][1]==b[2][2] == 'O') or (b[0][2] == b[1][1]==b[2][0] == 'O') or (b[0][0] == b[1][1]==b[2][2] == 'X') or (b[0][2] == b[1][1]==b[2][0] == 'X')):
        return 1
    else:
        return 0

def board_state(b):
    for i in range(3):
        for j in range(3):
            print(b[i][j],end="  ")
        print()


if __name__ == "__main__":
    print("Start...")
    global b
    b = [[0,0,0],[0,0,0],[0,0,0]]
    global flag,ct
    board_state(b)
    flag = 0
    ct = 0
    while True:
        print("Player 1...")
        X = int(input("Enter X: "))
        Y = int(input("Enter Y: "))
        ini = 0 
        while not ini:
            if b[X][Y] == 0:
                b[X][Y] = 'O'
                ct +=1
                board_state(b)
                ini = 1
                if (check_horizontal(b) or check_vertical(b) or check_diag(b)):
                    print("Player 1 wins")
                    flag = 1
                    break
                    
            else:
                print("Already Entered..")
                print("Enter Again..")
                X = int(input("Enter X"))
                Y = int(input("Enter Y"))
        if(flag or ct == 9):
                break
        
        
        print("Player 2...")
        X = int(input("Enter X: "))
        Y = int(input("Enter Y: "))
        ini = 0
        while not ini:
            if b[X][Y] == 0:
                b[X][Y] = 'X'
                ct +=1
                board_state(b)
                ini = 1
                if (check_horizontal(b) or check_vertical(b) or check_diag(b)):
                    print("Player 2 wins")
                    flag = 1
                    break
            else:
                print("Already Entered..")
                print("Enter Again..")
                X = int(input("Enter X"))
                Y = int(input("Enter Y"))
        if(flag or ct == 9):
                break
        
     
    print("Game over...")
    board_state(b)  
    if(not flag):
        print("Game Draw...")
        

    