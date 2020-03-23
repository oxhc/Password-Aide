import hashlib

from dbutils_sqlite import DBUtils


class Password:
    name: str
    url: str
    username: str
    password: str

    def __init__(self, id, name, url, username, password):
        self.name = name
        self.url = url
        self.username = username
        self.password = password
        self.id = id


class Pdb(DBUtils):
    def __init__(self, connection, auto_close=True):
        super().__init__(connection=connection, auto_close=auto_close)
        self.table_name = 'passwords'

    def create_table(self):
        self.create(self.table_name, [
            ['id varchar(35) primary key'],
            ['name varchar(50) not null'],
            ['url varchar(200)'],
            ['username varchar(50) not null'],
            ['password text not null'],
        ])

    def add(self, password: Password):
        return self.insert(self.table_name, [
            self.md5(password), password.name, password.url, password.username, password.password
        ])

    def remove(self):
        pass

    def modify(self):
        pass

    def clear(self):
        return self.delete(self.table_name)

    def get(self, search_key=None):
        if search_key != None:
            SQL = "select * from {} where name like '%{}%' or url like '%{}%' or username like '%{}%'" \
                .format(self.table_name, search_key, search_key, search_key)
        else:
            SQL = "select * from " + self.table_name
        res = self.fetch(SQL, count=0)
        return [Password(*i) for i in res]

    def md5(self, password):
        hl = hashlib.md5()
        s = password.name + password.url + password.username + password.password
        print(s)
        hl.update(s.encode(encoding='utf-8'))
        print('MD5加密前为 ：' + s)
        print('MD5加密后为 ：' + hl.hexdigest())
        return hl.hexdigest()
