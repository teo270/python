

class predmet:
    def __init__(self, predmet, ocena):
        self.predmet = predmet
        self.ocena = ocena



class student(predmet):
    def __init__(self, letnik, napredovanje):
        super().__init__(predmet, ocena)
        self.letnik = letnik

    def napredovanje(self):
        self.letnik += 1

    







def main():
    
if __name__ == "__main__":
    main()
