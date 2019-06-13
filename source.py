import sqlite3
conn=sqlite3.connect('database.db')
cu=conn.cursor()
#获取表名，保存在tab_name列表
cu.execute("select name from sqlite_master where type='table'")
tab_name=cu.fetchall()
tab_name=[line[0] for line in tab_name] 
#获取表的列名（字段名），保存在col_names列表,每个表的字段名集为一个元组
col_names=[]
for line in tab_name:
    cu.execute('pragma table_info({})'.format(line))
    col_name=cu.fetchall()
    col_name=[x[1] for x in col_name]
    col_names.append(col_name)
    col_name=tuple(col_name)

print(tab_name)
print(col_name)