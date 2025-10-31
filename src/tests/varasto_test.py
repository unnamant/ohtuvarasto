import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varaston_tilavuus_ei_ylitä_maksimiarvoa(self):
        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_varaston_saldo_ei_mene_negatiiviseksi(self):
        self.varasto = Varasto(10, 2)
        self.varasto.ota_varastosta(5)

        self.assertEqual(self.varasto.saldo, 0)

    def test_negatiivinen_lisäys_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_otto_palauttaa_nolla(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_negatiivinen_konstruktori_saldo(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_konstruktori_tilavuus(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktorin_saldo_yli_tilavuuden(self):
        self.varasto = Varasto(10, 20)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_konstruktori_asettaa_saldon_ja_tilavuuden_oikein(self):
        self.varasto.lisaa_varastoon(6)
        self.assertEqual(str(self.varasto), "saldo = 6, vielä tilaa 4")