for i in range(1, 100):
    if i % 15 == 0:
        print('fizzbazz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('bazz')
    else:
        print(i)
