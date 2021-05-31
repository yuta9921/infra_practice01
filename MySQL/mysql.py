import MySQLdb


#データベースへの接続
conn = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    password = 'kondouyuta',
    db = 'python_db',
    charset = 'utf8'
)


cursor = conn.cursor()

#NBAチームjazzの今日の試合の得点などをテーブルにまとめる--------------------------

# cursor.execute('create table jazz('
#     'id int not null auto_increment, '
#     'name varchar(14) not null,'
#     'age INT(3) NOT NULL,'
#     'height INT(3) NOT NULL,'
#     'points INT(3) NOT NULL,'
#     'PRIMARY KEY(id) )')


#insert で名前　年齢　身長　得点　をテーブルにーーーーーーーーーーーーーーーーーーー

# cursor.execute("""insert into jazz(name, age, height, points)
#                 values("conley", 34, 185, 27)
# """)
# cursor.execute("""insert into jazz(name, age, height, points)
#                 values("gobert", 29, 215, 15)
# """)
# cursor.execute("""insert into jazz(name, age, height, points)
#                 values("ONeale", 27, 193, 12)
# """)
# cursor.execute("""insert into jazz(name, age, height, points)
#                 values("ingles", 33, 203, 3)
# """)
# conn.commit()

#------------------------------------------------------------------

#ミッチェルの身長を変更

cursor.execute('update jazz set height = 184 where id = 1')
conn.commit()

#消去---------------------------------------------------------------

#マイケルジョーダンを消すために追加ーーーーーーー
# cursor.execute("""insert into jazz(name, age, height, points)
#                 values("jordan", 35, 198, 100)
# """)


#マイケルジョーダンを消すーーーーーーー
# cursor.execute('delete from jazz where name = "jordan" ')
# conn.commit()


cursor.close()
conn.close()
