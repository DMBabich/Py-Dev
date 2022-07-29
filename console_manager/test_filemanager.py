import tools


def test_mkdir():
    assert tools.make_folder('papka') == 'Folder was created!'


def test_remove():
    assert tools.remove('papka') == 'Remove complete'


def test_info():
    assert tools.info() == 'info'


