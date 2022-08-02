import random
import time
import os
from setup import Player
from setup import Comp
from setup import BagOfBalls
from setup import initializer

peoples = int(input('Введите кол-во играющих:\t'))
play_with_computer = input('В игре будет участвовать компьютер? (yes|no):\t')
if play_with_computer == 'yes':
    count_comp = int(input('Сколько игроков из общего числа будут компьютерами?:\t'))
    if peoples<count_comp:
        print('Дичь какая-то')
        os.system(exit())
    count_people = peoples - count_comp
else:
    count_people = peoples

versus = {}
p = 0
k = 0
while p!=count_people:
    player_name = input('Введите имя игрока:\t')
    if player_name in versus.keys():
        print('Такой игрок уже существует')
    else:
        versus[player_name] = Player(player_name)
        p += 1
try:
    while k!=count_comp:
        comp_name = input('Введите имя компьютера:\t')
        if comp_name in versus.keys():
            print('Такой игрок уже существует')
        else:
            versus[comp_name] = Comp(comp_name)
            k += 1
except Exception:
    print('Играем без компов')


print('Ожидайте инициализации партии')
loto = BagOfBalls()
time.sleep(2)
for k, v in versus.items():
    current_person = v
    print(f'Инициализируется {current_person.name}')
    current_person.create_empty_card()
    current_person.fill_card()
    current_person.create_ticket()
    print('Инициализация завершена успешно')
    print(f'Ваш билетик:\n{current_person.ticket}\n\n')
    time.sleep(1)
initializer()

# print(isinstance(computer, Player))  # False
perfomance = []
while loto.depth_of_bag() != 0:
    game_status = 0
    ball = loto.output_ball()[0]
    print(f'Выпало число {ball}')
    for k, v in versus.items():
        person = v
        if (len(versus) - len(perfomance) == 1) and person.status == 'PLAY':
            print(f'Победа за {person.name}')
            game_status = 1
            break
        if person.status != 'PLAY':
            continue
        print(f'Ход {person.name}')
        if isinstance(person, Player) and person.status == 'PLAY':
            person.print_ticket()
            answer = input(f'Хотите зачеркнуть число {ball} в своем билете? (yes|no):\t')
            if answer == 'yes' and person.check_number_in_ticket(number=ball):
                person.strike_out_number(number=ball)
            elif answer != 'yes' and person.check_number_in_ticket(number=ball):
                print('Вы проиграли')
                person.status = 'LOOSE'
                perfomance.append(0)
            elif answer == 'yes' and not person.check_number_in_ticket(number=ball):
                print('Вы проиграли')
                person.status = 'LOOSE'
                perfomance.append(0)
        elif isinstance(person, Comp) and person.status == 'PLAY':
            person.print_ticket()
            if person.check_number_in_ticket(number=ball):
                person.strike_out_number(number=ball)
        person.check_to_win()
        if person.status == 'WINNER':
            print(f'Победа за {person.name}')
            game_status = 1
            break
        print('\n'*1)
    time.sleep(1)
    if game_status:
        break
