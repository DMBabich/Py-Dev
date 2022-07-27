seq = input('Enter a number with separate as ", or / or ;"\n')
mass = seq.replace('/',',').replace(';',',').split(',')
print(set(mass))
