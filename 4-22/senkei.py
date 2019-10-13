number_list = range(100)


def senkei(number_list, num):
    found = False
    for i in number_list:
        if i == num:
            found = True
            break
    return found


print(senkei(number_list, 9))
print(senkei(number_list, 1000))
