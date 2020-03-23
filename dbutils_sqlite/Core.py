from .SQLs import insert_SQL, create_SQL, select_SQL, delete_SQL, update_SQL


def toString(obj):
    res = ""
    for key in obj.__dict__:
        if obj.__dict__.get(key) != "":
            res += "{} : {}\n".format(key, obj.__dict__.get(key))
    return res


class DBUtils:
    def __init__(self, connection, auto_close=True):
        self.conn = connection
        self.auto_close = auto_close

    def execute(self, SQL):

        cursor = self.conn.cursor()
        try:
            cursor.execute(SQL)
            print("操作成功 ", end=' ')
            return True
        except Exception:
            print("数据库操作失败", end=' ')
            return False
        finally:
            print(SQL.replace('\n', ' '))
            cursor.close()

    def fetch(self, SQL, count=0):

        cursor = self.conn.cursor()
        try:
            print("数据库操作成功", end=' ')
            cursor.execute(SQL)
            if count == 0:
                res = cursor.fetchall()
            elif count == 1:
                res = [cursor.fetchone()]
            else:
                res = cursor.fetchall()[0:count]
            return res
        except Exception:
            print("数据库操作失败", end=' ')
            return False
        finally:
            print(SQL.replace('\n', ' '))
            cursor.close()

    def create(self, table_name, columns):
        SQL = create_SQL(table_name, columns)
        return self.execute(SQL)

    def insert(self, table_name, values, columns=None):
        SQL = insert_SQL(table_name, values, columns=columns)
        return self.execute(SQL)

    def select(self, table_name, columns=None, where=None, count=0):
        SQL = select_SQL(table_name, columns=columns, where=where)
        return self.fetch(SQL, count=count)

    def delete(self, table_name, where=None):
        SQL = delete_SQL(table_name, where=where)
        return self.execute(SQL)

    def update(self, table_name, keyValues, where=None):
        SQL = update_SQL(table_name, keyValues, where=where)
        return self.execute(SQL)

    def __enter__(self):
        print("dbutils open")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn is not None:
            self.conn.commit()
            if self.auto_close:
                self.conn.close()
                print("sqlite database close")

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    import sqlite3

    conn = sqlite3.connect('ffi.db')
    with DBUtils(conn) as db:
        db.create('nt', [
            ['id varchar(4)']
        ])
        db.insert('nt', ['我'])
        print(db.select('nt'))
        # db.update('nt', [('id', '555')])
        # c = db.select('nt')
        # print(c)
