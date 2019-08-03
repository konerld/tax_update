#! /usr/bin/python3
# -*- coding: utf-8 -*
import sqlite3
import os

db_filename = 'car_tax.db'
schema_filename = 'db_schema.sql'

def create_db(db_filename, schema_filename):
    """
    Тестовая функция
    Функция создает тестовую базу для проверки основных функций
    """
    if not os.path.exists(db_filename):
        print(f'Создание БД {db_filename}')
        conn = sqlite3.connect(db_filename)
        print('Creating schema...')
        with open(schema_filename, 'r') as f:
    	    schema = f.read()
    	    conn.executescript(schema)
    	    print('database', db_filename, 'created !')
    	    conn.close()
        print(f'База {db_filename} успешно создана')
    else:
        print('файл БД {db_filename} уже существует')
        return True



if __name__ =='__main__':
    create_db(db_filename, schema_filename)