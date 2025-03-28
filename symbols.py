TOCKE = "\033[0;37m"
HODNIK = "\033[0;35m"
VRATA = "\033[0;34m"
IGRAC = "\033[1;97m"
CILJ = "\033[0;32m"
ZID = "\033[0;91m"
PUT = "\033[1;33m"
CUDOVISTE = "\033[1;95m"
OPASNOST = "\033[0;35m"

class Simboli:
    def __init__(self, simbol: str, boja: str):
        self.simbol = f"{boja}{simbol}\033[0m"

tocke = Simboli(".", TOCKE)
hodnik = Simboli("#", HODNIK)
vrata = Simboli("+", VRATA)
igrac = Simboli("@", IGRAC)
cilj = Simboli(">", CILJ)
zid = Simboli("I", ZID)
put_zvjezdica = Simboli("*", PUT)
cudoviste = Simboli("Č", CUDOVISTE)
opasnost  = Simboli(".", OPASNOST)
mac = Simboli(":", TOCKE)