from collections import deque
from symbols import vrata, igrac, cilj, tocke, zid, cudoviste, opasnost, mac
from random import randint

class Mapa:
    def __init__(self, sirina: int, visina: int):
        self.ima_mac = False
        self.sirina = sirina
        self.visina = visina
        self.podaci_mape = []

        self.kreiraj_mapu()
        self.postavi_zidove()
        self.postavi_igraca_i_cilj()
        self.postavi_cudovista()
        self.postavi_mac()

    def kreiraj_mapu(self):
        self.podaci_mape = []
        for _ in range(self.visina):
            red = []
            for _ in range(self.sirina):
                red.append(tocke)
            self.podaci_mape.append(red)

    def prikazi_mapu(self):
        okvir = "-" * (self.sirina + 2)
        print(okvir)
        for red in self.podaci_mape:
            print("|" + "".join(element.simbol for element in red) + "|")
        print(okvir)

    def postavi_zidove(self):
        for _ in range(randint(60, 80)):
            x, y = randint(1, self.sirina - 2), randint(1, self.visina - 2)
            duzina = randint(3, 6)
            horizontalno = randint(0, 1)
            vrata_index = randint(0, duzina - 1)

            for i in range(duzina):
                if horizontalno and x + i < self.sirina - 1:
                    self.podaci_mape[y][x + i] = vrata if i == vrata_index else zid
                elif not horizontalno and y + i < self.visina - 1:
                    self.podaci_mape[y + i][x] = vrata if i == vrata_index else zid

    def postavi_igraca_i_cilj(self):
        while True:
            igrac_x, igrac_y = randint(1, self.sirina - 2), randint(1, self.visina - 2)
            cilj_x, cilj_y = randint(1, self.sirina - 2), randint(1, self.visina - 2)

            if self.podaci_mape[igrac_y][igrac_x] != zid and self.podaci_mape[cilj_y][cilj_x] != zid:
                if (igrac_x, igrac_y) != (cilj_x, cilj_y):
                    self.podaci_mape[igrac_y][igrac_x] = igrac
                    self.podaci_mape[cilj_y][cilj_x] = cilj
                    break


    def pomakni_igraca(self, smjer):
        trenutni_x, trenutni_y = 0, 0
        for y, red in enumerate(self.podaci_mape):
            if igrac in red:
                trenutni_x, trenutni_y = red.index(igrac), y
                break

        pomaci = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
        dx, dy = pomaci.get(smjer, (0, 0))
        novi_x, novi_y = trenutni_x + dx, trenutni_y + dy

        if 0 <= novi_x < self.sirina and 0 <= novi_y < self.visina:
            cilj_polja = self.podaci_mape[novi_y][novi_x]

            if cilj_polja == cilj:
                return True
            if cilj_polja == mac:
                self.ima_mac = True
            if cilj_polja in [opasnost, cudoviste] and not self.ima_mac:
                return "smrt"
            if cilj_polja != zid:
                self.podaci_mape[trenutni_y][trenutni_x] = tocke
                self.podaci_mape[novi_y][novi_x] = igrac

        return False

    def postavi_cudovista(self):
        for _ in range(2):
            while True:
                x, y = randint(1, self.sirina - 2), randint(1, self.visina - 2)
                if self.podaci_mape[y][x] not in [zid, vrata, igrac, cilj, cudoviste]:
                    self.podaci_mape[y][x] = cudoviste
                    for yy in range(max(0, y - 1), min(self.visina, y + 2)):
                        for xx in range(max(0, x - 1), min(self.sirina, x + 2)):
                            if self.podaci_mape[yy][xx] not in [zid, vrata, igrac, cilj, cudoviste]:
                                self.podaci_mape[yy][xx] = opasnost
                    break

    def postavi_mac(self):
        while True:
            x, y = randint(1, self.sirina - 2), randint(1, self.visina - 2)
            x, y = randint(1, self.sirina - 2), randint(1, self.visina - 2)
            if self.podaci_mape[y][x] not in [zid, vrata, igrac, cilj, cudoviste, opasnost]:
                self.podaci_mape[y][x] = mac
                break


    def dohvati_susjede(self, cvor):
        x, y = cvor
        susjedi = []
        pomaci = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in pomaci:
            novi_x, novi_y = x + dx, y + dy
            if 0 <= novi_x < self.sirina and 0 <= novi_y < self.visina:
                if self.podaci_mape[novi_y][novi_x] not in [zid, cudoviste, opasnost]:
                    susjedi.append((novi_x, novi_y))
        return susjedi

    def dfs(self):
        for indeks, element in enumerate(self.podaci_mape):
            if igrac in element:
                v = (element.index(igrac), indeks)
                break

        for indeks, element in enumerate(self.podaci_mape):
            if cilj in element:
                z = (element.index(cilj), indeks)
                break

        stog = deque()
        posjeceni = set()
        roditelji = {}

        stog.append(v)

        while stog:
            trenutni_cvor = stog.pop()

            if trenutni_cvor in posjeceni:
                continue

            posjeceni.add(trenutni_cvor)

            if trenutni_cvor == z:
                putanja = []
                while trenutni_cvor in roditelji:
                    putanja.append(trenutni_cvor)
                    trenutni_cvor = roditelji[trenutni_cvor]
                putanja.append(v)
                return putanja [::-1]

            for susjed in self.dohvati_susjede(trenutni_cvor):
                if susjed not in posjeceni:
                    stog.append(susjed)
                    roditelji[susjed] = trenutni_cvor

        return []
