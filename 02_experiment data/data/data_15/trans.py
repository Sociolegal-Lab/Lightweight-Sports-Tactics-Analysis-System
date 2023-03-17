import os
import csv
os.mkdir('./ner')
os.mkdir('./ori')
with open('./test.csv', newline='') as csvfile:

    rows = csv.reader(csvfile)
    a = 0
    path = './ner/test_thuner.txt'
    f = open(path, 'w')
    
    
    for row in rows:
        
        if a == 0:
            a = a + 1
            continue
        else:
            # print(row[1] + row[2])
            print(row)
            f.write('<title>news\n')
            nertag = row[2].split(" ")
            for i in range(0, len(nertag)):
                print(i)
                try:
                    if row[1][i] != " ":
                        f.write(row[1][i] + " " + nertag[i]+ "\n")
                except:
                    a = a
            f.write("\n")
        
f.close()

with open('./dev.csv', newline='') as csvfile:

    rows = csv.reader(csvfile)
    a = 0
    path = './ner/dev_thuner.txt'
    f = open(path, 'w')
    
    
    for row in rows:
        
        if a == 0:
            a = a + 1
            continue
        else:
            # print(row[1] + row[2])
            f.write('<title>news\n')
            nertag = row[2].split(" ")
            for i in range(0, len(nertag)):
                if row[1][i] != " ":
                    f.write(row[1][i] + " " + nertag[i]+ "\n")
            f.write("\n")
        
f.close()

with open('./train.csv', newline='') as csvfile:

    rows = csv.reader(csvfile)
    a = 0
    path = './ner/train_thuner.txt'
    f = open(path, 'w')
    
    
    for row in rows:
        
        if a == 0:
            a = a + 1
            continue
        else:
            # print(row[1] + row[2])
            f.write('<title>news\n')
            nertag = row[2].split(" ")
            for i in range(0, len(nertag)):
                if row[1][i] != " ":
                    f.write(row[1][i] + " " + nertag[i]+ "\n")
            f.write("\n")
        
f.close()

