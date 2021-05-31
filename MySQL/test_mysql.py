
import unittest
from . mysql import *


# データベース名を1行ずつタプルに入れる
#*******    思うような結果にならず    ＊＊＊＊＊＊＊＊＊＊
# cursor.execute('show tables;')
# tables = cursor.fetchone()


#テーブルのデータを1行ずつタプルに入れる
sql = 'select * from jazz;'
cursor.execute(sql)
databases = cursor.fetchall()


#databasesタプルから”1行目”を取り出すときに使用する数字を分かりやすく変数にする

first_line = 0

#databasesタプル”1行目”から要素を取り出すときに使用する数字を分かりやすく変数にする

check_id     = 0
check_name   = 1
check_age    = 2
check_height = 3
check_points = 4


class TestMysql(unittest.TestCase):


    #データベース一覧を取得して今回使用している python_db が含まれているかテストしたかったーーーーーー
    #データベースの個数しか取得できなかったため、データベースが１つ以上存在するかどうかを
    #assertTrue でテストしている  


    def test_database(self):
        self.assertTrue(cursor.execute('show databases;'))



    #テーブル名一覧を取得してjazz が含まれているかテストしたかったーーーーーーーー
    #テーブル名も個数しか取得できなかった

    def test_table(self):
        self.assertTrue(cursor.execute('show tables;'))


    #idカラムがintになっているかーーーーーーーーーーーーーーーーーー
    #テーブル1行目の id に格納されているデータが文字列かテスト
    def test_jazz_name_int(self):
        self.assertEqual(type(databases[first_line][check_id]), int)


    #年齢カラムがstrになっているかーーーーーーーーーーーーーーーーーー
    #テーブル1行目の name に格納されているデータが文字列かテスト
    def test_jazz_name_int(self):
        self.assertEqual(type(databases[first_line][check_name]), str)



    #年齢カラムがintになっているかーーーーーーーーーーーーーーーーーー
    #テーブル1行目の age に格納されているデータが int かテスト
    def test_jazz_age_int(self):
        self.assertEqual(type(databases[first_line][check_age]), int)



    #身長カラムがintになっているかーーーーーーーーーーーーーーーーーー
    #テーブル1行目の height に格納されているデータが int かテスト
    def test_jazz_height_int(self):
        self.assertEqual(type(databases[first_line][check_height]), int)



    #得点カラムがintになっているかーーーーーーーーーーーーーーーーーーーーーーーーーー
    #テーブル1行目の point に格納されているデータが int かテスト
    def test_jazz_points_int(self):
        self.assertEqual(type(databases[first_line][check_points]), int)




if __name__ == '__main__':
    unittest.main()