import unittest
from statements import statement, statement_html
import json



class TestStatement(unittest.TestCase):
    def test_regression(self):
        invoice = json.load(open("tests/invoice.json", 'r'))

        plays = json.load(open("tests/plays.json", 'r'))

        result = statement(invoice, plays)

        exepcted = """Statement for BigCo
 Hamlet: $650.00 (55 seats)
 As You Like It: $580.00 (35 seats)
 Othello: $500.00 (40 seats)
Amount owed is $1,730.00
You earned 47 credits
"""
        self.assertEqual(result, exepcted)