from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class KPSpeli:
    def __init__(self):
        pass
    
    def valitse_pelityyppi(self):
        print("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
                )

        vastaus = input()
        return vastaus
    
    def luo_peli(self, tyyppi):
        if tyyppi.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            kaksinpeli = KPSPelaajaVsPelaaja()
            kaksinpeli.pelaa()
        elif tyyppi.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            yksinpeli = KPSTekoaly()
            yksinpeli.pelaa()
        elif tyyppi.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            haastava_yksinpeli = KPSParempiTekoaly()
            haastava_yksinpeli.pelaa()
        else:
            return "quit"

    def aloita(self):
        while True:
            pelityyppi = self.valitse_pelityyppi()
            peli = self.luo_peli(pelityyppi)
            if peli == "quit":
                break
            