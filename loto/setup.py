import random
import time


class Ticket:
    def __init__(self, name):
        self.name = name
        self.status = 'PLAY'
        self.ticket = ''
        self.card = [[], [], []]
        self.numbers = [i for i in range(1, 91)]
        self.numbers_in_ticket = random.sample(population=self.numbers, k=15)

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
        answer = None
        for line in self.card:
            for i in range(9):
                if line[i] == str(number):
                    answer = 1
        if answer:
            return True
        else:
            return False

    def strike_out_number(self, number):
        for line in self.card:
            for i in range(9):
                if line[i] == str(number):
                    line[i] = '--'
        self.ticket = ''
        self.create_ticket()

    def how_numbers_was_strike_out(self):
        return -26 + self.ticket.count("--")
        # print(f'вычеркнуто бочонков {-26 + self.ticket.count("--")}')

    def check_to_win(self):
        condition = self.how_numbers_was_strike_out()
        if condition == 15:
            self.status = 'WINNER'

    def print_card(self):
        print(self.card)


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


