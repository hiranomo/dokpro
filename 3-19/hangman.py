import random

def hangdman():
    w_list = ['harry','born','reon','ganp','nausika','joze']
    ward = random.choice(w_list)
    wrong = 0
    stages = ['__________',
              '|     |   ',
              '|     |   ',
              '|     O   ',
              '|    /|\  ',
              '|    / \  ',
              '|         ']
    rletters = list(ward)
    board = ['_'] * len(ward)
    win = False
    print('ハングマンへようこそ！{}文字のワードです。'.format(len(ward)))
    print(' '.join(board))
    while wrong < len(stages):
        print('\n')
        char = input('一文字予想してね！:')
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        if '_' not in board:
            win = True
            break
        if wrong > 0:
            print('\n','\n'.join(stages[0:wrong]))
    if win:
        print('あなたの勝ちです！')
    else:
        print('あなたの負け。\n答えは{}です。'.format(ward))

hangdman()
