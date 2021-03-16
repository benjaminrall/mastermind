import random

running = True

def setupHSTable():
    table = []
    file = open('highscores.txt')
    with file as f:
        for item in f:
            table.append([i for i in item.split(',')])
    for i in range(5):
        b = table[i]
        b[0] = int(b[0])
        b.pop()
    file.close()
    table = sorted(table, key=lambda x: x[0])
    return table

def printHS(t):
    print("These are the current highscores: ")
    for i in range(5):
        row = t[i]
        print((i + 1),".   ",row[1],"",row[0])

def saveHS():
    file = open("highscores.txt","w")
    global table
    for i in range(5):
        row = table[i]
        p = (str(row[0]) + "," + str(row[1]) + ",\n")
        file.write(p)
    file.close()
        
def randomNum(c):
    num = [None]*c
    for i in range(c):
        num[i] = random.randint(1,9)
    return num

def userChoice(c):
    while True:
        num = int(input("Enter your guess: "))
        if len(str(num)) == c:
            break
        else:
            print("Please enter a",c,"digit number!\n")
    return num

def check(r, u, n, p):
    w = False
    c = 0
    for i in range(n):
        if r[i] == u[i]:
            c += 1
            if p:
                print("\nPosition",(i + 1),"was correct.")
    if c == len(r):
        w = True
    else:
        print("\nYou got",c,"numbers correct.")
    return w

def victory(t, m):
    print("\nCongratulations you won on",m,"mode!")
    print("It took you",t,"tries!")
    global table
    for i in range(5):
        row = table[i]
        if t < row[0]:
            name = input("\nWhat is your name?: ")
            table.insert(i, [t, name])
            table.pop()
            break
    printHS(table)
            

def easy():
    won = False
    tries = 0
    rNum = randomNum(4)
    while won != True:
        uNum = userChoice(4)
        uNum = [int(d) for d in str(uNum)]
        won = check(rNum, uNum, 4, True)
        tries += 1
    victory(tries, "easy")
        
def normal():
    won = False
    tries = 0
    rNum = randomNum(4)
    while won != True:
        uNum = userChoice(4)
        uNum = [int(d) for d in str(uNum)]
        won = check(rNum, uNum, 4, False)
        tries += 1
    victory(tries, "normal")

def hard():
    won = False
    tries = 0
    rNum = randomNum(5)
    while won != True:
        uNum = userChoice(5)
        uNum = [int(d) for d in str(uNum)]
        won = check(rNum, uNum, 5, False)
        tries += 1
    victory(tries, "hard")

def run():
    m = input("\nWhat mode would you like to play?: ('easy', 'normal', 'hard')\n")
    if m == "easy":
        easy()
    elif m == "normal":
        normal()
    elif m == "hard":
        hard()
    else:
        running = False

table = setupHSTable()

while running:
    printHS(table)
    run()
    if input("Would you like to play again? (y/n)\n") == "y":
        print("\nReloading...\n")
    else:
        print("\nOkay, saving highscores...")
        saveHS()
        running = False
