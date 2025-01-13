import random


st = [[' ', ' ', ' '],
      [' ', ' ', ' '],
      [' ', ' ', ' ']]
move = 0
game = True
while game:
    try:
        if move % 2 == 0:
            print('User place X')
            row = int(input('Enter Row '))
            column = int(input('Enter Column '))
            if st[row - 1][column - 1] == ' ':
                st[row - 1][column - 1] = 'X'
                move += 1
            else:
                print('Space is occupied')
        else:
            print('Computer place O')
            r = random.randint(1,4)
            c = random.randint(1,4)
            if st[r - 1][c - 1] == ' ':
                st[r - 1][c - 1] = 'O'
                move += 1
        for i in st:
            print(i)
    except IndexError:
        print('Enter Valid Row and Column')

    for i in range(3):
        if st[i][0] == st[i][1] == st[i][2] and st[i][0] != ' ' and game == True:
            print(str(st[i][0]), 'wins')
            game = False
        if st[0][i] == st[1][i] == st[2][i] and st[0][i] != ' ' and game == True:
            print(str(st[i][0]), 'wins')
            game = False
        if st[0][0] == st[1][1] == st[2][2] and st[0][0] != ' ' and game == True:
            print(str(st[i][0]), 'wins')
            game = False
    if move == 9 and game == True:
        print('Game Drawn')
        game = False