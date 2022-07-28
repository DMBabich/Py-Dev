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
                tools.put()
            elif choice == '2':
                tools.buy()
            elif choice == '3':
                tools.history()
            elif choice == '4':
                print('Bye! See you later :)')
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
