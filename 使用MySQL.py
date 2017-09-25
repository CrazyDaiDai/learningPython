'MySQL'
'MySQL 是 Web 世界中使用最广泛的数据库服务器.MySQL是为服务器端设计的数据库,能承受高并发访问,同事占用的内存也远远大于SQLite'
'MySQL 内部有多种数据库引擎,最常用的引擎是支持数据库事务的InnoDB'

# 导入MySQL
import mysql.connector
# 注意把password设为你的root口令
conn = mysql.connector.connect(user='root',password='password',database='test')
cursor = conn.cursor()
# 创建 user 表
cuesor.execute('create table user (id varchar(20) primary key,name varchar(20))')
# 插入一条数据.MySQL的占位符是%s
cursor.execute('inster into user (id,name) values (%s,%s)',('125','Moto'))
print(cursor.rowcount)
cursor.close()
conn.commit()

# 查表
cursor = conn.cursor()
cursor.execute('select * from user where id %s' , ('125',))
values = cursor.fetchall()
print(values)
# 关闭
cursor.close()
conn.close()

