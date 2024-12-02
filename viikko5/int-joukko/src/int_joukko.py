OLETUSSYOTE = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = tarkista_syote(kapasiteetti)
        self.kasvatuskoko = tarkista_syote(kasvatuskoko)

        self.lista = self._luo_lista(self.kapasiteetti)

        self.koko = 0

    def kasvata_kokoa(self):
        self.koko += 1

    def kuuluu(self, n):
        return n in self.lista

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lista[self.koko] = n
            self.kasvata_kokoa()

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.koko % len(self.lista) == 0:
                taulukko_old = self.lista
                self.kopioi_lista(self.lista, taulukko_old)
                self.lista = self._luo_lista(self.koko + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.lista)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.koko):
            if n == self.lista[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lista[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.koko - 1):
                apu = self.lista[j]
                self.lista[j] = self.lista[j + 1]
                self.lista[j + 1] = apu

            self.koko -= 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.koko

    def to_int_list(self):
        taulu = self._luo_lista(self.koko)

        for i in range(0, len(taulu)):
            taulu[i] = self.lista[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.koko == 0:
            return "{}"
        elif self.koko == 1:
            return "{" + str(self.lista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.koko - 1):
                tuotos = tuotos + str(self.lista[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lista[self.koko - 1])
            tuotos = tuotos + "}"
            return tuotos

def tarkista_syote(syote):
    if syote is None:
        return OLETUSSYOTE
    elif type(syote) != int or syote < 0:
        raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
    else:
        return syote