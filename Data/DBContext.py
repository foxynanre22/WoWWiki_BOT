import sqlite3

from project.WoWWiki_BOT.Parser.ArticleModel import ArticleModel


class DBContext:
    """
    A class to represent a connection to the database.

    ...

    Attributes
    ----------
    connection : Connection
        represent connection to the database
    cursor : Cursor
        object to execute sql commands on the connection

    Methods
    -------
    find_article(article_name):
        find article in the database by the name
    add_article(article):
        add new article to the database
    update_article(article):
        update exciting article in the database
    close(memberUrl):
        close connection with database
    """

    def __init__(self, database):
        """
        Constructs all the necessary attributes for the DBContext object.

        Parameters
        ----------
            database : str
                a path to the database
        """
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def find_article(self, article_name):
        """find article in the database by the name"""
        with self.connection:
            result = self.cursor.execute(
                "SELECT * FROM `Articles` " "WHERE LOWER(`name`) = ?",
                (article_name,)
            ).fetchone()

            article = ArticleModel(
                name=result[1],
                link=result[2],
                photo_link=result[3],
                text=result[4],
                parseCategory=result[5],
            )

            return article

    def add_article(self, article):
        """add new article to the database"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `Articles` "
                "(`name`, `link`, `photo_link`, `text`, `parse_category`) "
                "VALUES(?,?,?,?,?)",
                (
                    str(article.name),
                    str(article.link),
                    str(article.photo_link),
                    str(article.text),
                    str(article.parseCategory),
                ),
            )

    def update_article(self, article):
        """update exciting article in the database"""
        with self.connection:
            return self.cursor.execute(
                "UPDATE `Articles` SET `link` = ?, "
                "`photo_link` = ?, `text` = ? WHERE `name` = ?",
                (
                    str(article.link),
                    str(article.photo_link),
                    str(article.text),
                    article.name,
                ),
            )

    def close(self):
        """close connection with database"""
        self.connection.close()
