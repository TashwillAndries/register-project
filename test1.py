import unittest
import mysql.connector


conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='lifechoices_login', auth_plugin='mysql_native_password')
cursor = conn.cursor()

class TestDatabase(unittest.TestCase):
    def test(self):
        sql = "SELECT id_number, username,surname,phone ,password, privilege FROM users"
        cursor.execute(sql)
        rows = cursor.fetchall()
        id_no = rows[0][0]
        self.assertTrue(len(id_no), 13)

if __name__ == '__main__':
    unittest.main()
