import csv

list = [['top gun','risky business','minority report'],
        ['titanic','the revenant','inception'],
        ['training day','man on fire','flight']]

with open('movies.csv','w') as f:
    w = csv.writer(f,delimiter=',')
    for low in list:
        w.writerow(low)
