# write your code here

space = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
motion = 'X'
print("---------")
print("| {} {} {} |".format(space[0][0], space[0][1], space[0][2]))
print("| {} {} {} |".format(space[1][0], space[1][1], space[1][2]))
print("| {} {} {} |".format(space[2][0], space[2][1], space[2][2]))
print("---------")

while True:
    check = [1, 2, 3]
    coordinate = input('Enter the coordinates ').split()
    if coordinate[0].isdigit() is False or coordinate[0].isdigit() is False:
        print('You should enter numbers!')
    elif int(coordinate[0]) > 3 or int(coordinate[1]) > 3:
        print('Coordinates should be from 1 to 3!')
    elif space[int(coordinate[0]) - 1][int(coordinate[1]) - 1] != ' ':
        print('This cell is occupied! Choose another one!')
    elif int(coordinate[0]) in check and int(coordinate[1]) in check:
        space[int(coordinate[0]) - 1][int(coordinate[1]) - 1] = motion
        print("---------")
        print("| {} {} {} |".format(space[0][0], space[0][1], space[0][2]))
        print("| {} {} {} |".format(space[1][0], space[1][1], space[1][2]))
        print("| {} {} {} |".format(space[2][0], space[2][1], space[2][2]))
        print("---------")
        if motion == 'X':
            motion = 'O'
        else:
            motion = 'X'
        if ((space[0][0] == space[0][1] == space[0][2] == 'X' or
             space[1][0] == space[1][1] == space[1][2] == 'X' or
             space[2][0] == space[2][1] == space[2][2] == 'X' or
             space[0][0] == space[1][0] == space[2][0] == 'X' or
             space[0][1] == space[1][1] == space[2][1] == 'X' or
             space[0][2] == space[1][2] == space[2][2] == 'X' or
             space[0][0] == space[1][1] == space[2][2] == 'X' or
             space[2][0] == space[1][1] == space[0][2] == 'X') and
                (space[0][0] == space[0][1] == space[0][2] == 'O' or
                 space[1][0] == space[1][1] == space[1][2] == 'O' or
                 space[2][0] == space[2][1] == space[2][2] == 'O' or
                 space[0][0] == space[1][0] == space[2][0] == 'O' or
                 space[0][1] == space[1][1] == space[2][1] == 'O' or
                 space[0][2] == space[1][2] == space[2][2] == 'O' or
                 space[0][0] == space[1][1] == space[2][2] == 'O' or
                 space[2][0] == space[1][1] == space[0][2] == 'O')):
            print('Impossible')
            break
        elif (space[0][0] == space[0][1] == space[0][2] == 'X' or
              space[1][0] == space[1][1] == space[1][2] == 'X' or
              space[2][0] == space[2][1] == space[2][2] == 'X' or
              space[0][0] == space[1][0] == space[2][0] == 'X' or
              space[0][1] == space[1][1] == space[2][1] == 'X' or
              space[0][2] == space[1][2] == space[2][2] == 'X' or
              space[0][0] == space[1][1] == space[2][2] == 'X' or
              space[2][0] == space[1][1] == space[0][2] == 'X'):
            print('X wins')
            break
        elif (space[0][0] == space[0][1] == space[0][2] == 'O' or
              space[1][0] == space[1][1] == space[1][2] == 'O' or
              space[2][0] == space[2][1] == space[2][2] == 'O' or
              space[0][0] == space[1][0] == space[2][0] == 'O' or
              space[0][1] == space[1][1] == space[2][1] == 'O' or
              space[0][2] == space[1][2] == space[2][2] == 'O' or
              space[0][0] == space[1][1] == space[2][2] == 'O' or
              space[2][0] == space[1][1] == space[0][2] == 'O'):
            print('O wins')
            break
        elif ' ' not in space[0] and ' ' not in space[1] and ' ' not in space[2]:
            print('Draw')
            break
