def runner():
    # create a menu class
    error = 'Invalid Input! Try Again!'
    # create a roll class
    print('What\'s Your First and Last Name? ')
    name = input()
    finish = False
    while not finish:
        # check the bonus
        # print(menu) print the menu
        # set the roll's empty variable to true
        # generate a roll from the roll class
        # print('\nRoll: ', roll)
        # use the menu variable to get the score and update the sum of the roll
        nums = '123456'
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
                        print()
                        # create a boolean array the gets the changes boolean array from the roll class
                        # for index in indexes:
                        #     changes[index] = True
                        # generate a roll
                        # print('Reroll: ', roll)


if __name__ == '__main__':
    runner()