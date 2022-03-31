# might not need this because of the extension of the checker class on menu
from Classes.Roll import *
from Classes.Checker import *
from Classes.HighScore import *


def runner():
    menu = Menu()
    error = 'Invalid Input! Try Again!'
    nums = '123456'
    other = '3k4kfslcy'
    roll = Roll()
    print('What is Your First and Last Name (With Spaces)? ', end='')
    name = input()
    finish = False
    while not finish:
        menu.checkBonus()
        print(menu)
        roll.setEmpty(True)
        roll.generateRoll()
        print('\nRoll: ', roll)
        menu.getScore().updateSum(roll)
        score = False
        tries = 1
        while not score and tries != 3:
            print('do you want to roll again<r> or score<s>?', end='')
            option = input()
            if option == 'r':
                moveOn = False
                moveOnTwo = False
                while not moveOn:
                    print('What dice do you wanna re-roll (enter 0 thru 4 separated by spaces) ', end='')
                    answer = input()
                    indexes = answer.split()
                    if len(indexes) < 5:
                        index = 0
                        while index < len(indexes):
                            if not moveOnTwo and indexes[index] in nums:
                                moveOn = True
                            elif moveOn and not indexes[index] in nums:
                                moveOn = False
                                moveOnTwo = True
                            index += 1
                    if moveOn:
                        changes = roll.getChanges()
                        for index in indexes:
                            changes[int(index)] = True
                        roll.generateRoll()
                        print('Reroll: ', roll)
                        menu.getScore().updateSum(roll)
                        tries += 1
                    else:
                        print(error)
            elif option == 's':
                print('\n')
                score = True
            else:
                print(error)
        selection = False
        while not selection:
            checker = Checker(menu.getScore().getSumsOfSingleDigitNums())
            checker.change(roll)
            print(checker)
            print('enter a score category -> ones<1>, twos<2>, threes<3>, fours<4>, fives<5>, sixes<6>, 3kind<3k>, '
                  '4kind<4k>, fhouse<f>, sm str<s>, lg str<l>, chance<c>, yahtzee<y>: ')
            option = input()
            if option in nums or option in other:
                menu.setOption(option)
                checkerList = checker.getList()
                menu.setList(checkerList)
                menu.change(roll)
                if menu.getError():
                    print('You Already Scored This Category! Try Again!')
                else:
                    selection = True
            else:
                print('\n')
                if menu.finish():
                    print(menu)
                    finish = True
    total = menu.getScore().getTotal()
    #  name = 'Dhruv Halderia' # For Debugging purposes
    #  total = 369
    recent = HighScore(name, total)
    length = 0
    output = ''
    with open('TopFiveHighScores.txt', 'r') as file:
        lineChange = -1
        valid = False
        length = int(file.readline())
        dialogue = []
        index = 0
        while index < len(dialogue):
            line = file.readline().split()
            dialogue[index] = HighScore(line[0] + ' ' + line[1], int(line[2]))
            index += 1
        dialogue = dialogue[::-1]  # reverses the list
        index = 0
        while index < len(dialogue) and not valid:
            if total > dialogue[index].getScore():
                lineChange = index
                valid = True
            index += 1
        newScores = []
        if not valid and length < 5:
            lineChange = index
            valid = True
        if valid:
            if length < 5:
                length += 1
                newScores = []
            else:
                length = 5
            index = 0
            finish = False
            while index < len(newScores):
                if index == lineChange:
                    newScores[index] = recent
                    finish = True
                elif finish:
                    newScores[index] = dialogue[index - 1]
                else:
                    newScores[index] = dialogue[index]
                index += 1
            for hS in newScores:
                output += hS
                output += '\n'
        elif length == 0:
            length += 1
        else:
            for hS in dialogue:
                output += hS
                output += '\n'
    with open('TopFiveHighScores.txt', 'w') as file:
        file.write(length)
        if output == '':
            file.write(recent.__str__())
        else:
            file.write(output)
    print('Leaderboard: ')
    print(output)


if __name__ == '__main__':
    runner()
