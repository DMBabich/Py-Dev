import tools
import os


def test_mkdir():
    assert tools.make_folder('papka') == 'Folder was created!'


def test_remove():
    assert tools.remove('papka') == 'Remove complete'


def test_info():
    assert tools.info() == 'info'


def test_save_checker():
    name = os.getcwd()
    answer = 'yes'
    assert tools.save_checker(name, answer) == 'checker was saved'


def test_save_balance():
    assert 'balance.txt' in os.listdir(os.getcwd())


def test_save_history():
    assert 'history.txt' in os.listdir(os.getcwd())


def test_put_balance():
    summ = 1000000
    tools.put(summ)
    assert tools.balance > 0
