import os
import shutil
import random


balance = 0
his = []


def put():
    global balance
    summ = float(input('Введите сумму пополнения:\t'))
    balance += summ
    print(f'Ваш текущий баланс составляет {balance}')
    # return balance + summ


def buy():
    global balance
    global his
    summ = float(input('Введите сумму покупки:\t'))
    if summ > balance:
        print('Недостаточно средств, оформите кредит или овердрафт')
    else:
        prod = input('Что будете приобретать?:\t')
        balance -= summ
        his.append((prod, summ))


def history():
    global his
    for item in his:
        print(f'{item[0]} на сумму {item[1]}')


def make_folder(name):
    os.mkdir(name)


def remove(name):
    item = os.getcwd() + '/' + name
    os.rmdir(item)


def make_copy(name, path):
    full_name = name
    full_path = path
    if name[0] != '/':
        full_name = os.getcwd() + '/' + name
    if path[0] != '/':
        full_path = os.getcwd() + '/' + path
    shutil.copy(full_name, full_path)


def check_dir(name):
    print(f'Директория содержит: {os.listdir(name)}')


def check_dir_only(name):
    only_dir = None
    for dirs, folder, files in os.walk(name):
        only_dir = folder
        break
    print(only_dir)


def check_files_only(name):
    only_files = None
    for dirs, folder, files in os.walk(name):
        only_files = files
        break
    print(only_files)


def info():
    inf = os.uname()
    print(inf)
    print(inf.sysname)


def creator():
    print('*'*15)
    print('Badi')
    print('https://github.com/DMBabich')
    print('*'*15)


def victory():
    actors = [
        ('Леона́рдо Вильге́льм Ди Ка́прио', '11.11.1974'),
        ('Уи́льям Брэ́дли Питт', '18.12.1963'),
        ('Джон Кри́стофер Депп II', '09.06.1963'),
        ('Ро́берт Джон Да́уни — мла́дший', '04.04.1965'),
        ('Уи́ллард Кэ́рролл Смит Второй', '25.09.1968'),
        ('Том Круз', '03.07.1962'),
        ('Дуэ́йн Ду́глас Джо́нсон', '02.05.1972'),
        ('Ра́йан Ро́дни Ре́йнольдс', '23.10.1976'),
        ('Майкл Сильве́стр Гарденцио Сталло́не', '06.07.1946'),
        ('Ра́йан То́мас Го́слинг', '12.11.1980')
    ]

    days = {
        '01': 'первого',
        '02': 'второго',
        '03': 'третьего',
        '04': 'четвертого',
        '05': 'пятого',
        '06': 'шестого',
        '07': 'седьмого',
        '08': 'восьмого',
        '09': 'девятого',
        '10': 'десятого',
        '11': 'одиннадцатого',
        '12': 'двеннадцатого',
        '13': 'тринадцатого',
        '14': 'четырнадцатого',
        '15': 'пятнадцатого',
        '16': 'шестнадцатого',
        '17': 'семнадцатого',
        '18': 'восемнадцатого',
        '19': 'девятнадцатого',
        '20': 'двадцатого',
        '21': 'двадцать первого',
        '22': 'двадцать второго',
        '23': 'двадцать третьего',
        '24': 'двадцать четвертого',
        '25': 'двадцать пятого',
        '26': 'двадцать шестого',
        '27': 'двадцать седьмого',
        '28': 'двадцать восьмого',
        '29': 'двадцать девятого',
        '30': 'тридцатого',
        '31': 'тридцать первого'
    }

    mouth = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря'
    }

    while 1:
        positive = 0
        negative = 0
        quest = 5
        numbers = [i for i in range(10)]
        random_index = random.sample(numbers, 5)
        for i in random_index:
            choose = actors[i]
            answer = input(f'Введите дату рождения в формате dd.mm.yyyy для актера {choose[0]}\n')
            if answer == choose[1]:
                positive += 1
                print()
            else:
                negative += 1
                year = choose[1][-4:]
                print('Wrong!\nTrue answer is')
                print(f'{days[choose[1][:2]]} {mouth[choose[1][3:5]]} {year} года\n')
        print('Y statistic')
        print('*' * 15)
        print(f'Правильных ответов: {positive}\nОшибок: {negative}')
        print(f'Процент верных ответов: {(positive * 100) / quest}')
        print(f'Процент ошибочных ответов: {(negative * 100) / quest}')
        answer = input('play again?\n(yes | no)\n')
        if answer != 'yes':
            break


def set_dir(name):
    os.chdir(name)


def console_info():
    print('Выберите действие:')
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого текущей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об ОС')
    print('8. создатель')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. сменить рабочую директорию')
    print('12. выход')
