# database initial
import sqlite3

from dao import Pdb
from configparser import ConfigParser

# load config file
cp = ConfigParser()
cp.read('default.cfg', encoding='utf8')

db_name = cp.get('database', 'path')

conn = sqlite3.connect(db_name)

with Pdb(conn) as pdb:
    pdb.create_table()

if __name__ == '__main__':
    pass
