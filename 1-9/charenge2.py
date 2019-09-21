moji = ''
list = []
with open('favo_food.txt','w',encoding='utf-8') as f:
    while True:
        moji = input('好きな食べ物は何ですか？終了はqを入力。>')
        if moji == 'q':
            print('終了します。')
            break
        list.append(moji)
    f.write('\n'.join(list))
