mass_len = int(input('Enter lenght of massive:\t'))
digits = []
for i in range(mass_len):
    digits.append(int(input('Enter a number:\t')))
digits.sort()
print(digits)
