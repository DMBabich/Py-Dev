from orm import Session
from orm import Word
from orm import Skill
from orm import WordSkill


def add_words(current, new):
    result = current.query(Word).filter_by(word=new['keywords']).first()
    if result:
        if result.count < new['count']:
            result.count = new['count']
            result.up = new['up']
            result.down = new['down']
            print('Key word edit')
        else:
            print('Key word not edit')
    else:
        current.add(Word(word=new['keywords'], count=new['count'], up=new['up'], down=new['down']))
        print('UwU')
    return current


def add_skills(current, new):
    for item in new['requirements']:
        res = current.query(Skill).filter_by(name=item['name']).one_or_none()
        if not res:
            print(item['name'])
            current.add(Skill(name=item['name']))
        else:
            print('skills not added')
    return current


def add_ws(current, new):
    result = current.query(Word).filter_by(word=new['keywords']).first()
    word_id, word_count = result.id, result.count
    for item in new['requirements']:
        skill_id = current.query(Skill).filter_by(name=item['name']).first().id
        print(word_id, skill_id)
        result = current.query(WordSkill).filter_by(id_word=word_id, id_skill=skill_id).one_or_none()
        if not result:
            current.add(WordSkill(id_word=word_id, id_skill=skill_id, count=item['count'], percent=item['percent']))
            print('WordSkill done')
        elif word_count < new['count']:
            result.count = item['count']
            result.percent = item['percent']
            print('WordSkill edit')
        else:
            print('WordSkill not edit')
    return current


def add_row(new):
    current = Session()
    current = add_words(current, new)
    current = add_skills(current, new)
    current = add_ws(current, new)
    current.commit()
    current.close()
