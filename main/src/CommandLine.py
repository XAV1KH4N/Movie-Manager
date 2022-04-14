from Database import Database
from Scanner import Scanner
from TomatoScraper import TomatoScraper


class CommandLine:
    def __init__(self):
        self.ts = TomatoScraper()
        self.db = Database()
        self.scanner = Scanner()

    def loop(self):
        while True:
            ## Rescan hard drive
            ## Only add new films
            ##

    def exit(self):
        self.db.close()
