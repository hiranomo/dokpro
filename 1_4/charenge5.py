def reigai(suuti):
    '''prints the suuti convert to float.
    :param suuti: int.
    '''
    try:
        print(float(suuti))
    except (ValueError):
        print('数値を入力してください')

suuti = input('suuti :')

reigai(suuti)
