# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-06-11 19:33

import pymysql

dbinfo = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "port": 3309}


class Dbconnect():
    def __init__(self, db_cof, database=""):
        self.db_cof = db_cof
        # 打开数据库
        self.db = pymysql.connect(database=database, cursorclass=pymysql.cursors.DictCursor, **db_cof)
        # 使用corsor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.cursor.close()
        self.db.close()


def select_sql(select_sql):
    '''sql查询函数'''
    db = Dbconnect(dbinfo, database="apps")
    result = db.select(select_sql)  # 查询
    db.close()
    return result


def execute_sql(insert_sql):
    '''执行sql 删除、提交、修改函数'''
    db = Dbconnect(dbinfo, database="apps")
    db.execute(insert_sql)  # 执行
    db.close()


if __name__ == '__main__':
    sql = 'SELECT * FROM auth_user where username = "admin"'
    a = select_sql(sql)
    print(a)
    print(a[0]["email"])
    # for i in a:
    #     print(i)
    insert_sql1 = "INSERT INTO apps.apiapp_card(id, card_id, card_user, add_time) VALUES (1222222, '', 'test77777', '2019-12-17')"
    execute_sql(insert_sql1)

