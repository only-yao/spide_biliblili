import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1',        # 服务器地址
                       port=3306,               # 服务器端口号
                       user='root',             # 用户名
                       passwd='00000000',       # 用户密码
                       db='mysql',
                       charset='utf8mb4')

# 创建游标
cursor = conn.cursor()          # 使用连接创建并返回游标commit提交rollback回滚close关闭


#
# def create_db():
#     global cursor
#     cursor.execute("use spider")
#     cursor.execute(
#             """create table spider_bili
#                 (COUNT INT ZEROFILL,
#                  SCORE TINYINT ZEROFILL,
#                  SEASON_ID INT ZEROFILL,
#                  DANMAKU INT ZEROFILL,
#                  FOLLOW INT ZEROFILL,
#                  VIEW INT ZEROFILL,
#                  TITLE CHAR(30))"""
#     )
#

def save_db(result):
    # 将数据保存至本地
    cursor.execute("use spider")
    sql = "insert into spider_bili(COUNT,SCORE,SEASON_ID," \
        "DANMAKU,FOLLOW,VIEW,TITLE) values(%s, %s, %s, %s, %s, %s, %s)"
    for row in result:
        try:
            cursor.execute(sql, list(row))
        except:
            conn.rollback()
    conn.commit()
    result = []
    return result
#
# def query_db():
#     global cursor
#
#     sql = "SELECT * FROM spider_bili"
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 获取所有记录列表
#         results = cursor.fetchall()
#         for evaluate in results:
#             for i in range(len(evaluate)):
#                 print(evaluate[i])
#         print('\n')
#     except:
#         print("Error: unable to fecth data")

# # query_db()
cursor.execute("use spider")
# # cursor.execute("show index from spider_bili\G")
#
sql = "select * from spider_bili"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    use = cursor.fetchall()
    for evaluate in use:
        for i in range(len(evaluate)):
            print(evaluate[i])
    print('\n')
    conn.commit()

except:
    conn.rollback()
    print("Error: unable to fecth data")
