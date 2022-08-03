from setup import Ticket
from setup import Player
from setup import Comp
from setup import BagOfBalls


class TestTicket:

    def test_init(self):
        test_ticket = Ticket('test')
        assert test_ticket.name == 'test'
        assert test_ticket.status == 'PLAY'
        assert test_ticket.card == [[],[],[]]
        assert len(test_ticket.numbers) == 90

    def test_create_empty_card(self):
        test_ticket = Ticket('test')
        test_ticket.create_empty_card()
        assert test_ticket.card != [[], [], []]

    def test_isinstance(self):
        test_ticket = Ticket('test')
        assert isinstance(test_ticket, Ticket)


class TestPlayer:

    def test_init(self):
        test_ticket = Player('test_player')
        assert test_ticket.name == 'test_player'
        assert test_ticket.status == 'PLAY'
        assert test_ticket.card == [[],[],[]]
        assert len(test_ticket.numbers) == 90

    def test_isinstance(self):
        test_player = Player('player')
        assert isinstance(test_player, Player)


class TestComp:

    def test_init(self):
        test_ticket = Comp('test_comp')
        assert test_ticket.name == 'test_comp'
        assert test_ticket.status == 'PLAY'
        assert test_ticket.card == [[],[],[]]
        assert len(test_ticket.numbers) == 90

    def test_isinstance(self):
        test_comp = Comp('comp')
        assert isinstance(test_comp, Comp)


class TestBagOfBalls:

    def test_init(self):
        balls = BagOfBalls()
        assert len(balls.balls) == 90
        assert balls.current_ball == None

    def test_output_ball(self):
        bag = BagOfBalls()
        bag.output_ball()
        assert bag.current_ball != None

    def test_depth_of_bag(self):
        bag = BagOfBalls()
        bag.output_ball()
        bag.output_ball()
        assert len(bag.balls) == 88
