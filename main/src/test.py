import sqlite3

class DB:
    def __init__(self):
        self.con = sqlite3.connect("resources/movies.db")
        self.cur = self.con.cursor()
        self.createTables()

    def createTables(self):
        self.cur.execute("DROP TABLE lang")
        self.con.commit()

        self.cur.execute("CREATE TABLE lang(name, first_appeared)")
        self.con.commit()

    def insert(self):
        self.cur.execute("INSERT INTO lang VALUES(?, ?)", ("C", 1972))

        # The qmark style used with executemany():
        lang_list = [
            ("Fortran", 1957),
            ("Python", 1991),
            ("Go", 2009),
        ]
        self.cur.executemany("INSERT INTO lang VALUES(?, ?)", lang_list)
        self.con.commit()

    def check(self):
        # And this is the named style:
        self.cur.execute("SELECT * FROM movies")
        print(self.cur.fetchall())

    def close(self):
        self.con.close()