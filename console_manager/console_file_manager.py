import tools
import os


while 1:
    tools.console_info()
    answer = input('Я выбираю:\t')

    if answer == '1':
        folder = input('Введите название папки:\n')
        tools.make_folder(folder)
    elif answer == '2':
        item = input('Введите название папки в текущей директории которую надо удалить:\n')
        tools.remove(item)
    elif answer == '3':
        item = input('Введите название (папки|файла) или путь с названием который будем копировать:\n')
        path = input('Введите название (папки|файла) или путь с названием куда будем копировать:\n')
        tools.make_copy(item, path)
    elif answer == '4':
        name = os.getcwd()
        tools.check_dir(name)
        answer = input('Хотите записать инфу о директории? (yes|no):\t')
        tools.save_checker(answer, name)
    elif answer == '5':
        name = os.getcwd()
        tools.check_dir_only(name)
    elif answer == '6':
        name = os.getcwd()
        tools.check_files_only(name)
    elif answer == '7':
        tools.info()
    elif answer == '8':
        tools.creator()
    elif answer == '9':
        tools.victory()
    elif answer == '10':
        while True:
            print('1. пополнение счета')
            print('2. покупка')
            print('3. история покупок')
            print('4. выход')
            choice = input('\nВыберите пункт меню:\t')
            if choice == '1':
                summ = float(input('Введите сумму пополнения:\t'))
                tools.put(summ)
            elif choice == '2':
                summ = float(input('Введите сумму покупки:\t'))
                tools.buy(summ)
            elif choice == '3':
                answer = input('Посмотреть прошлые покупки? (yes|no):\t')
                tools.show_history(answer)
                tools.history()
            elif choice == '4':
                print('Bye! See you later :)')
                tools.save_balance(tools.balance)
                tools.save_history(tools.his)
                tools.his = []
                break
            else:
                print('Неверный пункт меню')
            print()
    elif answer == '11':
        folder = input('Введите путь, в который надо перейти:\n')
        tools.set_dir(folder)
    elif answer == '12':
        print('Bye!')
        break
    else:
        print('Неверный пункт меню')
    print()
