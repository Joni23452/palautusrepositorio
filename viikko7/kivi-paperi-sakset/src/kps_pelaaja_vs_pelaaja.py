from kps_peli import KPSpeli


class KPSPelaajaVsPelaaja(KPSpeli):
    def _toisen_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")