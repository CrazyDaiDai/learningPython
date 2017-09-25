'访问数据库'
'sqlite3'

'建表和插入数据'

# import sqlite3
# # 连接到sqlite数据库
# # 数据库文件test.db
# # 如果文件不存在,会在当前目录创建
# conn = sqlite3.connect('test.db')
# # 创建一个 cursor
# cursor = conn.cursor()
# # 执行一条SQL语句,创建user表
# cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
# # 继续执行一条SQL语句,插入一条记录
# cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')
# # 通过rowcount获取插入的行数
# print(cursor.rowcount)
# # 关闭 cursor
# cursor.close()
# # 提交事务
# conn.commit()
# # 关闭 connection
# conn.close()

'查询记录'
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句
cursor.execute('select * from user where id=?',('1',))
# 获得查询结果
value = cursor.fetchall()
print(value)

'使用Python的db-API时,只要高清楚Connection和Cursor对象,打开后一定记得关闭,就可以放心的使用了'
'使用Cursor对象执行 insert,update,delete语句时,执行结果由 rowcount 返回影响的行数,就可以拿到执行结果'
'使用Cursor对象执行 select 语句时,通过 fetchall() 可以拿到结果集.结果是一个list,每个元素都是一个tuple,对应一行记录'
'如果SQL语句带有参数,那么需要把参数按照位置传递给 execute() 方法,有几个?占位符就必须对应几个参数'
cursor.execute('select * from user where name=? and pwd=?' , ('abc','password'))
cursor.close()
conn.close()


'SQLite 的特点是轻量级,可嵌入,但是不能承受高并发访问,适合桌面和移动应用'


