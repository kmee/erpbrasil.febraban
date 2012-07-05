# -*- coding: utf-8 -*-
import unittest
import datetime

from pyboleto.bank.hsbc import BoletoHsbc

from testutils import BoletoTestCase


class TestBancoHsbc(BoletoTestCase):
    def setUp(self):
        d = BoletoHsbc()
        d.agencia_cedente = '1172-0'
        d.conta_cedente = '3903036'
        d.data_vencimento = datetime.date(2009, 05, 25)
        d.data_documento = datetime.date(2009, 05, 25)
        d.data_processamento = datetime.date(2009, 05, 25)
        d.valor_documento = 35.00
        #d.nosso_numero = '2125525'
        d.numero_documento = '0100010103120'
        self.dados = d

    def test_render(self):
        self.check_pdf_rendering('hsbc', self.dados)

    def test_linha_digitavel(self):
        self.assertEqual(self.dados.linha_digitavel,
            '39993.90309 36010.001018 03120.145929 3 42480000003500'
        )

    def test_codigo_de_barras(self):
        self.assertEqual(self.dados.barcode,
            '39993424800000035003903036010001010312014592'
        )

    def test_agencia(self):
        self.assertEqual(self.dados.agencia_cedente, '1172-0')

    def test_conta(self):
        self.assertEqual(self.dados.conta_cedente, '3903036')

    def test_nosso_numero(self):
        self.assertEqual(self.dados.nosso_numero, '0100010103120947')

suite = unittest.TestLoader().loadTestsFromTestCase(TestBancoHsbc)


if __name__ == '__main__':
    unittest.main()