import pymysql
import traceback

db_passwd = "1"
db_host = "localhost"
db_name = "test_db"
db_port = "3306"
db_user = "root"

# 单条查询记录对象
class SingleObj(object):
    def __init__(self, data, key_list):
        for i in range(len(key_list)):
            setattr(self, key_list[i], data[i])

# 所有查询记录对象
class SqlObjList(object):
    def __init__(self, cursor):
        cursor = cursor
        data_tuple = cursor.fetchall()
        key_list = []
        for key_tuple in cursor.description:
            key_list.append(key_tuple[0])
        self.result = []
        for data in data_tuple:
            singleObj = SingleObj(data, key_list)
            self.result.append(singleObj)


def getSQLResult():
    # 连接数据库
    db = pymysql.connect(host=db_host, port=int(db_port), user=db_user, password=db_passwd, database=db_name)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = 'select * from name_db'
    try:
        # 执行sql语句
        cursor.execute(sql)
        sql_res = SqlObjList(cursor).result
        # 提交到数据库执行
        db.commit()
        return sql_res
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    result = getSQLResult()
    if result:
        print(type(result))
        for res in result:
            print(res.id, res.name)
    else:
        print("无结果")