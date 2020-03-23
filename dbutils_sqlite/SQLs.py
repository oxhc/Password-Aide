def insert_SQL(table_name, values, columns=None):
    if columns is not None:
        columns_str = "({})".format(pack(columns, isStr=False))
    else:
        columns_str = ''
    return "insert into {} {} values ({})".format(table_name, columns_str, pack(values, all_str=False))


def create_SQL(table_name, columns):
    return 'create table IF NOT EXISTS {} ({})'.format(table_name,
                                                       ','.join(
                                                           list(map(lambda x: pack(x, isStr=False, sep=' '), columns))))


def select_SQL(table_name, columns=None, where=None):
    cols = pack(columns, isStr=False, default='*')
    return 'select {} from {} {}'.format(cols, table_name, where_SQL(where))


def delete_SQL(table_name, where=None):
    return "delete from {} {}".format(table_name, where_SQL(where))


def update_SQL(table_name, keyValues, where=None):
    content = ', '.join(map(lambda k: "{}='{}'".format(k[0], k[1]), keyValues))
    return 'update {} set {} {}'.format(table_name, content, where_SQL(where))


def where_SQL(s):
    if s is None:
        return ''
    else:
        if isinstance(s, str):
            s = [s]
        return ' where ' + ' and '.join(s) + ' '


def quote(s, all=False):
    if isinstance(s, str) or all:
        if s == 'null':
            return 'null'
        return "'" + s + "'"
    else:
        return str(s)


def pack(args, isStr=True, sep=',', default='', all_str=True):
    if args is None:
        return default
    if isStr:
        args = list(map(lambda x: quote(x, all=all_str), args))
    res = sep.join(args)
    return res


if __name__ == '__main__':
    print(update_SQL('tt', [('ff', '1'), ('dd', '22')], ['a = 1']))
