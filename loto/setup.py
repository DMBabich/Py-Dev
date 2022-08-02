import random
import time


# maket of logic
"""
Последовательная программа (прототип) для отработки главных функций и логики
класс БИЛЕТ - в нем основная игра
класс ИГРОВОЕ_ПОЛЕ - в нем будет вытаскиваться бочонок
класс ИГРОК\ПК - дети класса БИЛЕТ
"""
## create numbers for ticket
numbers = [i for i in range(1,91)]
numbers_in_ticket = random.sample(population=numbers, k=15)
## create fields 4 tickets
ticket = [[],[],[]]
for i in range(3):
    for j in range(9):
        ticket[i].append(' ')
## fill tickets
for i in range(3):
    start = 0
    end = 9
    popup = [i for i in range(start, end)]
    indexes = random.sample(population=popup, k=5)
    for j in range(9):
        if j in indexes:
            ticket[i][j] = str(numbers_in_ticket.pop())
        # else:
        #     ticket[i][j].append(' ')

##decorathor
# TODO: можно бахнуть в декоратор, но так как все перевел в текст - спорно
print('-'*26)
text = ('-'*26) + '\n'
for line in ticket:
    space = [' '*(3-len(i)) for i in line]
    # print(f'{line[0]}  {line[1]}  {line[2]}  {line[3]}  {line[4]}  {line[5]}  {line[6]}  {line[7]}  {line[8]}')
    text += f'{line[0]}{space[0]}{line[1]}{space[1]}{line[2]}{space[2]}{line[3]}{space[3]}' \
            f'{line[4]}{space[4]}{line[5]}{space[5]}{line[6]}{space[6]}{line[7]}{space[7]}' \
            f'{line[8]}{space[8]}\n'
print('-'*26)
text += ('-'*26) + '\n'



print('\n','*'*20,'\n')
print(text)

for i in [25, 66, 59, 81, 55, 60]:
    if str(i) in text:
        print(f'{i} yyyeeesss')
        text = text.replace(str(i), '--')
print(text)
print(f'вычеркнуто бочонков {-26 + text.count("--")}')


class Ticket:
    def __init__(self, name):
        self.name = name
        self.status = None
        self.ticket = ''
        self.card = [[], [], []]
        self.numbers = [i for i in range(1, 91)]
        self.numbers_in_ticket = random.sample(population=numbers, k=15)

    def create_empty_card(self):
        for i in range(3):
            for j in range(9):
                self.card[i].append(' ')

    def fill_card(self):
        for i in range(3):
            popup = [i for i in range(0, 9)]
            indexes = random.sample(population=popup, k=5)
            for j in range(9):
                if j in indexes:
                    self.card[i][j] = str(self.numbers_in_ticket.pop())

    def create_ticket(self):
        self.ticket += ('-' * 26) + '\n'
        for line in self.card:
            space = [' ' * (3 - len(i)) for i in line]
            self.ticket += f'{line[0]}{space[0]}{line[1]}{space[1]}{line[2]}{space[2]}{line[3]}{space[3]}' \
                           f'{line[4]}{space[4]}{line[5]}{space[5]}{line[6]}{space[6]}{line[7]}{space[7]}' \
                           f'{line[8]}{space[8]}\n'
        self.ticket += ('-' * 26) + '\n'

    def print_ticket(self):
        print(self.ticket)

    def check_number_in_ticket(self, number):
        return str(number) in self.ticket

    def strike_out_number(self, number):
        self.ticket = self.ticket.replace(str(number), '--')

    def how_numbers_was_strike_out(self):
        return -26 + self.ticket.count("--")
        # print(f'вычеркнуто бочонков {-26 + self.ticket.count("--")}')

    def check_to_win(self):
        condition = self.how_numbers_was_strike_out()
        if condition == 15:
            self.status = 'WINNER'


class BagOfBalls:
    def __init__(self):
        self.balls = [i for i in range(1, 91)]
        self.current_ball = None

    def output_ball(self):
        self.current_ball = random.sample(population=self.balls,
                                          k=1)
        self.balls.remove(self.current_ball[0])
        return self.current_ball

    def depth_of_bag(self):
        return len(self.balls)


class Player(Ticket):
    pass


class Comp(Ticket):
    pass


def initializer():
    print('Ваша игра готова!')
    for i in [3,2,1]:
        print(f'Запуск через {i}')
        time.sleep(1)
    print('\n' * 30)


