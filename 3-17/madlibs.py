import re
text = '''__いつ__、__どこで__で__誰が__が__何をした__した。
何故なら、__なぜ__。'''

def mad_libs(text):
    hints = re.findall('__.*?__',text)
    if hints is not None:
        for hint in hints:
            word = input('{}を入力：'.format(hint))
            text = text.replace(hint,word,1)
        text = text.replace('\n','')
        print('\n')
        print(text)
    else:
        print('引数textが無効です。')

mad_libs(text)
