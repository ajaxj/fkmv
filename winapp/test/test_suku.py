# -*- coding:utf-8 -*-
import unittest
from winapp.suku import Suku

class TestSuku(unittest.TestCase):
    app = None

    def setUp(self):
        self.app = Suku()

    def testReadUrlToHtml(self):
        url = self.app.url_dongzuo
        result = self.app.readUrlToHtml(url)
        self.assertNotEqual(None,result)
