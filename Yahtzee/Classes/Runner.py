from Classes.Menu import *  # might not need this because of the extension of the checker class on menu
from Classes.Roll import *
from Classes.Checker import *
from Classes.HighScore import *


def runner():
    menu = Menu()
    error = 'Invalid Input! Try Again!'
    nums = '123456'
    other = '3k4kfslcy'
    roll = Roll()
    print('What\'s Your First and Last Name? ')
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
            print('do you want to roll again<r> or score<s>?', end = '')
            option = input()
            if option == 'r':
                moveOn = False
                moveOnTwo = False
                while not moveOn:
                    print('What dice do you wanna re-roll (enter 0 thru 4 separated by spaces) ', end = '')
                    answer = input()
                    indexes = answer.split()
                    if len(indexes) < 5:
                        i = 0
                        while i < len(indexes):
                            if not moveOnTwo and indexes[i] in nums:
                                moveOn = True
                            elif moveOn and not indexes[i] in nums:
                                moveOn = False
                                moveOnTwo = True
                            i += 1
                    if moveOn:
                        print('\n')
                        changes = roll.getChanges()
                        for index in indexes:
                            changes[index] = True
                        roll.generateRoll()
                        print('Reroll: ', roll)
                        menu.getScore().updateSum(roll)
                        tries += 1
                    else:
                        print(error)
            elif option is 's':
                print('\n')
                score = True
            else:
                print(error)
        selection = False
        while not selection:
            checker = Checker(menu.getScore().getSumsOfSingleDigitNums())
            checker.change(roll)
            print(checker)
            print('ones<1>, twos<2>, threes<3>, fours<4>, fives<5>, sixes<6>, 3kind<3k>, 4kind<4k>, fhouse<f>, sm str<s>, lg str<l>, chance<c>, yahtzee<y>: ')
            option = input()
            if option in nums or option in other:
                menu.setOption(option)
                list = checker.getList()
                menu.setList(list)
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
    # file writing


if __name__ == '__main__':
    runner()