import sqlite3


class Database:
    def __init__(self):
        address = "resources/movies.db"
        self.conn = sqlite3.connect(address)
        self.cursor = self.conn.cursor()
        self.construct()

    def execute(self, query, parms=""):
        self.conn.execute(query, parms)

    def addFilm(self, name, score):
        try:
            movie_id = self.getId()
            self.execute("INSERT INTO movies VALUES(?, ?, ?)", (movie_id, name, score))
            self.conn.commit()
        except sqlite3.DatabaseError:
            self.execute("UPDATE movies SET movie_score = ? WHERE movie_name = ?",(score, name))
            self.conn.commit()

    def getId(self):
        self.cursor.execute("SELECT max(movie_id) FROM movies")
        data = self.cursor.fetchall()
        if len(data) == 0 or len(data[0]) == 0 or data[0][0] is None:
            return 1
        else:
            return data[0][0] + 1

    def construct(self):
        self.createTables()

    def createTables(self):
        #self.execute("DROP TABLE IF EXISTS movies")
        self.execute("CREATE TABLE IF NOT EXISTS movies("
                          "movie_id     SERIAL PRIMARY KEY, "
                          "movie_name   VARCHAR UNIQUE NOT NULL, "
                          "movie_score  INTEGER NOT NULL)")
        self.conn.commit()



    def close(self):
        self.conn.close()

