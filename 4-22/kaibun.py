def kaibun(word):
    word = word.lower()
    return word[::-1] == word


print(kaibun('mother'))
print(kaibun('Mom'))
