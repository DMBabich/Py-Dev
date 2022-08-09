from pprint import pprint
from pickle import dump, load
import re
from collections import Counter

from requests import get
from pycbrf import ExchangeRates


def parcer(query, where='all'):
    """
    Получение данных о средней максимальной и минимальной величине суммы в вакансии и 5 самых упоминаемых навыков
    :param query: ключевое слово для поиска
    :param where: место, где будет искать текст
    :return: словарь с навыками
    """
    url = 'https://api.hh.ru/vacancies'
    rate = ExchangeRates()
    # получение первого запроса
    p = {'text': query if where == 'all' else f'NAME: {query}' if where == 'name' else f'COMPANY_NAME: {query}'}
    r = get(url=url, params=p).json()
    area = {}
    pprint(r)
    all_count = len(r['items'])
    result = {
            'keywords': query,
            'count': all_count}
    sal = {'from': [], 'to': [], 'cur': []}
    skillis = []
    p = {'text': query,
         'page': 1}
    ress = get(url=url, params=p).json()
    all_count = len(ress['items'])
    result['count'] += all_count
    # перебор каждой вакансии
    for res in ress['items']:
        # pprint(res)
        skills = set()
        city_vac = res['area']['name']
        if city_vac not in area:
            area[city_vac] = res['area']['id']
        ar = res['area']
        res_full = get(res['url']).json()
        # pprint(res_full)
        pp = res_full['description']
        # print(pp)
        pp_re = re.findall(r'\s[A-Za-z-?]+', pp)
        # print(pp_re)
        its = set(x.strip(' -').lower() for x in pp_re)
        # print(its)
        for sk in res_full['key_skills']:
            skillis.append(sk['name'].lower())
            skills.add(sk['name'].lower())
        # skills |= sk1
        for it in its:
            if not any(it in x for x in skills):
                skillis.append(it)
        if res_full['salary']:
            code = res_full['salary']['currency']
            if rate[code] is None:
                code = 'RUR'
            k = 1 if code == 'RUR' else float(rate[code].value)
            sal['from'].append(k * res_full['salary']['from'] if res['salary']['from'] else k * res_full['salary']['to'])
            sal['to'].append(k * res_full['salary']['to'] if res['salary']['to'] else k*res_full['salary']['from'])
    # создание словаря-счетчика для навыков
    sk2 = Counter(skillis)
    # pprint(sk2)
    up = sum(sal['from']) / len(sal['from'])
    down = sum(sal['to']) / len(sal['to'])
    # формирование результирующего словаря
    result.update({'down': round(up, 2),
                   'up': round(down, 2)})
    add = []
    for name, count in sk2.most_common(5):
        add.append({'name': name,
                    'count': count,
                    'percent': round((count / result['count'])*100, 2)})
    result['requirements'] = add
    with open('area.pkl', mode='wb') as f:
        dump(area, f)
    return result


if __name__ == '__main__':
    vacancy = input('Введите интересующую вакансию: ')
    pprint(parcer(vacancy))
