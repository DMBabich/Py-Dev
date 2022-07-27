seq1 = input('Enter a number for first massive with separate as ", or / or ;"\n')
set1 = set(seq1.replace('/',',').replace(';',',').split(','))

seq2 = input('Enter a number for second massive with separate as ", or / or ;"\n')
set2 = set(seq2.replace('/',',').replace(';',',').split(','))

print(set1-set2)
