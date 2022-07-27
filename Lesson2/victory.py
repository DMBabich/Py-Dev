leo = 1974  # Leonardo DiCaprio
dwain = 1972  # Dwayne Johnson
brad = 1963  # Bradley Pitt
rob = 1965  # Robert John Downey Jr
john = 1963  # John Depp II

while 1:
    positive = 0
    negative = 0
    all = 5

    answer = int(input('Введите год рождения Leonardo DiCaprio:\t'))
    if answer == 1974:
        positive += 1
    else:
        negative += 1

    answer = int(input('Введите год рождения Dwayne Johnson:\t'))
    if answer == 1972:
        positive += 1
    else:
        negative += 1

    answer = int(input('Введите год рождения Bradley Pitt:\t'))
    if answer == 1963:
        positive += 1
    else:
        negative += 1

    answer = int(input('Введите год рождения Robert John Downey Jr:\t'))
    if answer == 1965:
        positive += 1
    else:
        negative += 1

    answer = int(input('Введите год рождения John Depp II:\t'))
    if answer == 1963:
        positive += 1
    else:
        negative += 1

    print(f'\nВаша статистика ->')
    print(f'Верных ответов: {positive}\t Ошибок: {negative}')
    print(f'Процент верных ответов: {(positive*100)/all}')
    print(f'Процент ошибочных ответов: {(negative*100)/all}')
    answer = input('wanna play again? (да | нет)\t')
    if answer == 'нет':
        break
