import random
import sqlite3
import string

from dao import Pdb, Password
from configparser import ConfigParser

# load config file
cp = ConfigParser()
cp.read('default.cfg', encoding='utf8')

db_name = cp.get('database', 'path')
db_connect = None


def get(keyword, page=0):
    conn = sqlite3.connect(db_name)
    with Pdb(conn) as pdb:
        res = pdb.get(search_key=keyword)
    return res


def add(name, url, username, password):
    password = Password(None, name, url, username, password)
    conn = sqlite3.connect(db_name)
    with Pdb(conn) as pdb:
        return pdb.add(password)


def del_(id):
    conn = sqlite3.connect(db_name)
    with Pdb(conn) as pdb:
        return pdb.delete(pdb.table_name, where="id='{}'".format(id))


def clear():
    conn = sqlite3.connect(db_name)
    with Pdb(conn) as pdb:
        return pdb.clear()


def gen(length, symbol='.?'):
    r = random.Random()
    first_char = r.choice(string.ascii_letters)
    vong = [r.choice(string.ascii_letters + string.digits) for i in range(length - 1)]
    ran = r.randint(1, length) - 2
    vong[ran] = r.choice(symbol)
    chars = ''.join(vong)
    print(first_char + chars)
    return first_char + chars


def get_default_username():
    usernames = cp.get('default', 'usernames')
    return usernames.split(',')


def remove_repetation():
    conn = sqlite3.connect(db_name)
    with Pdb(conn) as pdb:
        res = pdb.select(pdb.table_name)
    removed = list(set(res))
    print(res)


def import_by_csv(file_path):
    with open(file_path) as csv:
        content = csv.read().splitlines()
    for row in content[1:]:
        row_data = row.split(',')
        print(row_data)
        flag = add(*row_data)
    return True


if __name__ == '__main__':
    import_by_csv(r'C:\Users\Administrator\Desktop\Chrome 密码.csv')
    # conn = sqlite3.connect(db_name)
    # with Pdb(conn) as pdb:
    #     pdb.md5(Password('3','2','','4','5'))
