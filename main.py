# -*- coding: utf-8 -*
import sqlite3
from sqlite3 import Error


def connection_to_db(db_file='car_tax.db'):
    """
    возвращает переменную для обращения к бд
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def send_request(query):
    """
    Выполняет SQL запрос в БД
    Возвращает список кортежей
    """
    conn = connection_to_db()
    try:
        with conn:
            cur = conn.cursor()
            cur.execute(query)
            return cur.fetchall()
    except sqlite3.IntegrityError as e:
        print('Error occured: ', e)


def get_person_id_list():
    """
    преобразовывает список кортежей вывода функции send_request
        в целочисленный список айдишников
    """
    response = send_request('SELECT id FROM persons;')
    id_list = []
    for n in response:
        id_list.append(n[0])
    return id_list


def get_person_total_car_count(person_id):
    """
    person_id : id человека
    функция возвращает целое число 
    (кол-во автомобилей для person)
    """
    query = f'SELECT COUNT(tax) from cars WHERE id={person_id};'
    car_count = send_request(query)[0][0]
    return car_count


def update_tax():
    """
    функция обновляет поле tax для всех person
    """
    id_list = get_person_id_list()
    for person_id in id_list:
        car_count = get_person_total_car_count(person_id)
        if car_count > 1:
            query = f'''UPDATE persons 
                            SET tax = (SELECT SUM(tax)*1.4 
                                    FROM cars WHERE id={person_id})
                        WHERE id={person_id};'''
            send_request(query)
        elif car_count == 1:
            query = f'''UPDATE persons 
                            SET tax = (SELECT tax 
                                    FROM cars WHERE id={person_id})
                        WHERE id={person_id};'''
            send_request(query)


if __name__ =='__main__':
    update_tax()