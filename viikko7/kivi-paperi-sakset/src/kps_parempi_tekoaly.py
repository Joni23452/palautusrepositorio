from tekoaly_parannettu import TekoalyParannettu
from kps_peli import KPSpeli


class KPSParempiTekoaly(KPSpeli):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto