import sqlite3

class DBContext:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def find_article(self, article_name):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `Articles` WHERE LOWER(`name`) = ?', (article_name,)).fetchall()
            return result

    def add_article(self, article):
        with self.connection:
            return self.cursor.execute("INSERT INTO `Articles` (`name`, `link`, `photo_link`, `text`, `parse_category`) "
                                       "VALUES(?,?,?,?,?)", (str(article.name), str(article.link), str(article.photo_link),
                                                             str(article.text), str(article.parseCategory)))

    def update_article(self, article):
        with self.connection:
            return self.cursor.execute("UPDATE `Articles` SET `link` = ?, photo_link = ?, text = ? WHERE `name` = ?",
                                       (str(article.link), str(article.photo_link), str(article.text), article.name))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()