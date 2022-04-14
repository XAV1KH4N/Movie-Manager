import requests

from Scanner import Scanner


class TomatoScraper:
    def __init__(self):
        self.url = "https://www.rottentomatoes.com/m/"
        self.url_search = "https://www.rottentomatoes.com/search?search="
        self.line_identifier = "@context"

    def runInterface(self):
        scanner = Scanner()
        film = scanner.input()

        if film.upper() == "EXIT":
            return

        score = "N/A"
        try:
            score = self.getTomato(film)
        except:
            pass

        finally:
            scanner.output(score)

        self.runInterface()

    def getTomatoBackup(self, film):
        film = film.strip()
        film = film.replace(" ", "%20")
        new_url = self.url_search + film
        page = requests.get(new_url).text
        perc = self.filterBackup(page)
        return perc

    def filterBackup(self, page):
        after = page.split("search-page-media-row")[1]
        for line in after.split("\n"):
            if "tomatometerscore" in line:
                line = line.replace(" ", "")
                line = line.replace('''"''', "")
                perc = line.split("=")[1]
                return perc
        raise TomatoScraper("Could not find score from backup")

    def getTomato(self, film_org):
        film = film_org.strip()
        film = film.replace(" ", "_")

        try:
            file = self.fetch(film)
            line = self.filterLine(file)
            perc = self.breakLine(line)
            return perc
        except TomatoScraper:
            return self.getTomatoBackup(film_org)

    def fetch(self, film):
        f = requests.get(self.url + film)
        return f.text

    def filterLine(self, page):
        for line in page.split("\n"):
            if self.line_identifier in line:
                return line
        raise TomoatoError("Could not find "+self.line_identifier)

    def breakLine(self, line):
        identifier = "ratingValue"
        if identifier not in line:
            raise TomoatoError(identifier+" not in line")
        posA = line.index(identifier) + len(identifier) + 3
        posB = posA + 3
        return line[posA:posB].replace('''"''', "")


    def save(self, page):
        with open("page.txt", "w") as file:
            file.write(page)


class TomoatoError(Exception):
    def __init__(self, message="Error has occurred"):
        self.message = message


def main():
    ts = TomatoScraper()
    db = Database()
    dic = ts.runScore()
    db.writeDict(dic)
    db.close()
    # ts.runInterface()


if __name__ == '__main__':
    # main()
    db = Database()
    db.getId()
    db.close()
