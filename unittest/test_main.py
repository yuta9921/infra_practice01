import unittest
from main import *
import os


class TestMain(unittest.TestCase):

    #名前が入っているカラムがｓｔｒかどうか------------------------------
    def test_name_column_type(self):
        self.assertEqual(type(name_column), str)


    #性別が male か female かのテスト-----------------------------------
    def test_gender_column(self):
        self.assertEqual(gender_column, "Male" or "Female")


    #身長が int かどうか -------------------------------------------
    def test_height_column_type(self):
        self.assertEqual(type(height_column), int)


    #計算後の身長が int かどうか-----------------------------------
    def test_new_height_type(self):
        self.assertEqual(type(new_height), int)


    #計算後の身長が０より大きいかどうか--------------------------------
    def test_new_height_size(self):
        self.assertTrue(new_height)


    #取得したい列数が1以上かどうか----------------------
    def test_GET_LINE(self):
        self.assertTrue(GET_LINE)


    #取得するファイルパスに ’.csv’ が含まれているかのテスト--------------
    def test_FILE_PATH(self):
        self.assertIn('.csv', FILE_PATH)


    #取得するファイルのサイズが1以上か---------------------------------
    def test_FILE_PATH_size(self):
        self.assertTrue(os.path.getsize(FILE_PATH))


    #出力するファイルパスに ’.csv’ が含まれているかのテスト-------------------
    def test_NEW_FILE_PATH(self):
        self.assertIn('.csv', NEW_FILE_PATH)

    
    #出力するファイルのサイズが1以上か----------------------------------------
    def test_NEW_FILE_PATH_size(self):
        self.assertTrue(os.path.getsize(NEW_FILE_PATH))


    #文字コードが宣言されているか-----------------------------------------
    def test_ENCODING(self):
        self.assertTrue(ENCODING)




if __name__ == '__main__':
    unittest.main()