import os


class Scanner:
    def __init__(self):
        self.movie_path = "N:Film/Movies"
        self.movie_path = "D:Film/Movies"

    def output(self, line):
        print("Percentage: ", line, "%")

    def input(self):
        self.menu()
        film = input()
        return film

    def menu(self):
        print("Enter film name: ")

    def readMovies(self):
        try:
            files = os.listdir(self.movie_path)
            return files
        except FileNotFoundError:
            return []

    def formatMovies(self, movies):
        films = [None]*len(movies)
        for i in range(len(movies)):
            films[i] = movies[i].split(".")[0]
        return films


