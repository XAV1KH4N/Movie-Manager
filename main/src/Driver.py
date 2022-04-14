from Scanner import Scanner
from Database import Database
from TomatoScraper import TomatoScraper, TomoatoError
from test import DB


class Driver:
    def main(self):
        movies = self.scanFilms()
        #self.displayFilms(movies)
        self.saveMovies(movies)

    def saveMovies(self, movies):
        db = Database()
        id = 1
        for name in movies:
            db.addFilm(name, movies[name])
            id += 1
        db.getId()
        db.close()

    def scanFilms(self):
        scanner = Scanner()
        ts = TomatoScraper()

        files = scanner.readMovies()
        files = scanner.formatMovies(files)

        dic = {}

        for name in files:
            try:
                dic[name] = ts.getTomato(name)
            except TomoatoError:
                pass
        return dic

    def displayFilms(self, movies):
        for name in movies:
            print("--", name, movies[name], "%")


if __name__ == '__main__':
    driver = Driver()
    driver.main()
