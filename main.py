last = 0
turn = input('Choose when you wish to play (me/computer) ').strip().lower()

while last < 21:
    try:
        if turn == 'me':
            count = int(input('Tell how many numbers you wish to enter (1 - 3) '))
            if count not in [1, 2, 3]:
                print('Invalid input. You lost!')
                break
            nums = [last + i for i in range(1, count + 1)]
            print('You:', *nums, sep='\n')
            last = nums[-1]
            if last >= 21:
                print('You lost!')
                break
            turn = 'computer'
        else:
            comp = (4 - last % 4) or 3
            nums = [last + i for i in range(1, comp + 1)]
            print('Computer: ', *nums, sep='\n')
            last = nums[-1]
            if last >= 21:
                print('You win!')
                break
            turn = 'me'
    except KeyboardInterrupt:
        print('\nThe game has been ended manually')
        exit(0)




