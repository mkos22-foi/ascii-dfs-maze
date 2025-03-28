from map import Mapa
from random import randint
from symbols import put_zvjezdica

def run():
    while True:
        teren.prikazi_mapu()
        print("Koristi W, A, S i D za kretanje. Unesi Q za izlaz\n")
        print("Unesi DFS za automatsko pronalaženje puta do cilja\n")
        naredba = input("> ").strip().lower()

        if naredba == "q":
            print("\nViše sreće drugi put :)\n")
            break

        if naredba in ["w", "a", "s", "d"]:
            rezultat = teren.pomakni_igraca(naredba)
            if rezultat == True:
                print("\nPobijeda!!! Došao si do cilja!\n")
                break
            elif rezultat == "smrt":
                print("\nČudovište te pojelo! Igra je završena!\n")
                break

        if naredba == "dfs":
            putanja = teren.dfs()

            if putanja:
                print(f"\nPutanja pronađena pomoću DFS-a: {putanja}\n")

                for x, y in putanja[1:-1]:
                    teren.podaci_mape[y][x] = put_zvjezdica
                print("\nPronađena je ruta pomoću DFS-a!\n")
            else:
                print("\nNema moguće rute pomoću DFS-a!\n")

if __name__ == "__main__":
    m_sirina = randint(30, 60)
    m_visina = randint(7, 15)
    teren = Mapa(m_sirina, m_visina)
    run()
