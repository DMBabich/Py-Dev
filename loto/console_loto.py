import random

# from setup import Ticket
import time

from setup import Player
from setup import Comp
from setup import BagOfBalls
from setup import initializer


player_name = input('Введите имя игрока:\t')
player = Player(player_name)
comp_name = random.choice(['Badi','Thor','Odin','Квазимодо','Шарлатан','Воландеморт'])
print(f'Против вас играет {comp_name}')
computer = Comp(comp_name)
loto = BagOfBalls()
versus = [player, computer]

print('Ожидайте инициализации партии')
time.sleep(2)
for current_person in versus:
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
    for person in versus:
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
