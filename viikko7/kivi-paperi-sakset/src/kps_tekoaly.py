from tekoaly import Tekoaly
from kps_peli import KPSpeli


class KPSTekoaly(KPSpeli):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto