"""
Создает основу БД через запрос
"""
from sqlite3 import connect


db = connect('base.db').cursor()

db.executescript('''
    create table words (
    id integer primary key,
    word varchar(50) not null,
    count real,
    up real,
    down real);

    create table skills (
    id integer primary key,
    name varchar(255)
    );

    create table wordskills (
    id integer primary key,
    id_word integer,
    id_skill integer,
    count real,
    percent real,
    foreign key (id_word) references words (id)
    foreign key (id_skill) references skills (id)
    );

    create table area (
    id integer primary key,
    name varchar(50) unique,
    ind integer
    );
''')

db.close()
