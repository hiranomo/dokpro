moji = ''
seikai = [2,3,5,7]
while True:
    moji = input('一桁の素数を入力して下さい。終了はqを入力。>')
    if moji == 'q':
        print('終了します。')
        break
    try:
        moji = int(moji)
        if moji in seikai:
            print('正解！')
        else:
            print('不正解')
    except ValueError:
        print('数字を入力するか、”q”で終了します。')
