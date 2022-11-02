import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virhe_varasto = Varasto(-1, -1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_konstruktori_asettaa_negatiivisen_tilavuuden_nollaksi(self):
        self.assertAlmostEqual(self.virhe_varasto.tilavuus, 0)
    
    def test_konstruktori_asettaa_negatiivisen_saldon_nollaksi(self):
        self.assertAlmostEqual(self.virhe_varasto.saldo, 0)
    
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
    
    def test_alkusaldon_ylittäessä_tilavuuden_ylimääräinen_saldo_poistetaan(self):
        yli_ayraiden = Varasto(10,20)
        self.assertAlmostEqual(yli_ayraiden.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_negatiivinen_lisays_ei_tee_mitaan(self):
        saldo_alussa = self.varasto.saldo
        self.varasto.lisaa_varastoon(-8)
        self.assertAlmostEqual(self.varasto.saldo, saldo_alussa)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
    
    def test_tilavuudesta_yli_meneva_lisays_menee_hukkaan(self):
        self.varasto.lisaa_varastoon(self.varasto.paljonko_mahtuu() + 10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_negatiivinen_ottaminen_ei_toimi(self):
        self.varasto.lisaa_varastoon(8)
        otettu = self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(otettu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_yli_saldon_ottaminen_asettaa_saldon_nollaan(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(100)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_oikean_merkkijonon(self):
        self.assertEqual(self.varasto.__str__(), 'saldo = 0, vielä tilaa 11')