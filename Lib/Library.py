import mysql.connector
from mysql.connector import MySQLConnection, Error

class Library:
    host = 'localhost'
    database = 'LIBRARY'
    user = 'root'
    password = 'mypass'

    def __init__(self,host,database,user,password):
        try:
            conn = mysql.connector.connect(host=host,
                                       database=database,
                                       user=user,
                                       password=password)
            if conn.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(e)

    def stop_con(self):
        conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
        conn.close()


    # метод для распечатки общзего списка книг и журналов в библиотеке
    def printerAuthor(self):
        try:
            sql = "SELECT idAUTHOR, First_name, Last_name FROM Author"
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql)
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)

    def printerBooks(self):
        try:
            sql = "SELECT B.NameB, B.YearB, B.Shelve, A.First_name, A.Last_name FROM Author A, Books B WHERE A.idAUTHOR=B.idAUTHOR"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql)
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)

    def printerJournal(self):
        try:
            sql = "SELECT J.nameJ, J.YearJ, J.shelve, A.First_name, A.Last_name FROM Author A, journals J WHERE A.idAUTHOR=J.idAUTHOR"
            conn = mysql.connector.connect(host=self.host,
                                               database=self.database,
                                               user=self.user,
                                               password=self.password)
            c = conn.cursor()
            c.execute(sql)
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)

    def addAuthor(self, id, first_name, last_nasme):
        try:
            sql = "INSERT INTO Author(idAUTHOR, First_name, Last_name)" \
                      " VALUES(%s,%s,%s)"
            args = (id, first_name, last_nasme)
            conn = mysql.connector.connect(host=self.host,
                                               database=self.database,
                                               user=self.user,
                                               password=self.password)
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            return "Автор добавлен!"
        except Error as e:
            return e

    # метод добавление книг query = "INSERT INTO books(title,isbn) " \ "VALUES(%s,%s)"
    def addBook(self,id, name, year, shelve, idauthor):
        try:
            sql = "INSERT INTO Books(idBooks, NameB, YearB, Shelve, idAUTHOR)"\
                    " VALUES(%s,%s,%s,%s,%s)"
            args=(id, name, year, shelve, idauthor)
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql,args)
            conn.commit()
        except Error as e:
            print(e)

    # метод добавление журналов
    def addJournal(self,id, name, year, shelve, publisher,idauthor ):
        try:
            sql = "INSERT INTO journals(idjournals, nameJ, yearJ, shelve, publisher, idAUTHOR)" \
                " VALUES(%s,%s,%s,%s,%s, %s)"
            args = (id, name, year, shelve, publisher, idauthor)
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
        except Error as e:
            print(e)

    def deleteAuthor(self,id):
        try:
            sql = "DELETE FROM Author WHERE idAUTHOR = %s"
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql, (id,))
            conn.commit()
            return "Автор удален!"
        except Error as e:
            return e

    def deleteBook(self,id):
        try:
            sql = "DELETE FROM Books WHERE idBooks = %s"
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql, (id,))
            conn.commit()
        except Error as e:
            print(e)

    def deleteJournal(self,id):
        try:
            sql = "DELETE FROM journals WHERE idjournals = %s"
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql, (id,))
            conn.commit()
        except Error as e:
            print(e)

    def searchBook(self, name):
        try:
            sql = "SELECT B.NameB, B.YearB, B.Shelve, A.First_name, A.Last_name FROM Author A, Books B WHERE A.idAUTHOR=B.idAUTHOR and B.NameB = %s"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)

            c = conn.cursor()
            c.execute(sql,(name,))
            print("Книга найдена")
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)

    def updateBook(self, name, id):
        try:
            sql = "UPDATE Books SET NameB = %s WHERE idBooks = %s"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)

            c = conn.cursor()
            c.execute(sql,(name,id))
            conn.commit()
            return "Название книги изменено!"
        except Error as e:
            print(e)

