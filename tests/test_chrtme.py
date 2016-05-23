#!/usr/bin/env python

import unittest

try:
    from unittest import mock  # py3
except ImportError:
    import mock  # requires "pip install mock"

class ChrtmeTestToolkit(unittest.TestCase):
    """Base class for all Chrtme tests."""

    @classmethod
    def setUp(cls):
        """Pre-test setup steps"""
        from .context import chrtme
        cls.chrtme_lib = chrtme
        cls.chrtme_local_obj = cls.chrtme_lib.Chrtme(url='',location='',cmd='')

    @classmethod
    def tearDown(cls):
        """Post-test cleaning steps"""
        del cls.chrtme_lib
        del cls.chrtme_local_obj


class ChrtmeTest(ChrtmeTestToolkit):
    """Basic tests for the Chrtme Class."""

    def testImportAsLibrary(self):
        """Testing library import"""
        try:
            from .context import chrtme
        except ImportError:
            self.fail('Importing chrtme library failed')
        except:
            self.fail('Unexpected failure during chrtme import')
        

    def testObject(self):
        """Testing creating chrtme object"""
        try:
            chrtme_local_obj = self.chrtme_lib.Chrtme(url='',location='',cmd='')
        except:
            self.fail('Error during chrtme object creation')
        self.assertIsInstance(chrtme_local_obj, self.chrtme_lib.Chrtme)

    def testObjHasDownloadURL(self):
        """Testing Object URL attribute existence"""
        with self.assertRaises(TypeError, msg="URL not provided") as e:
            new_chrtme_obj = self.chrtme_lib.Chrtme()

    def testObjURLCorrectlySet(self):
        """Test if chrtme object URL correct set"""
        test_url = 'fake_URL'
        new_chrtme_obj = self.chrtme_lib.Chrtme(url=test_url, location='', cmd='')
        self.assertEqual(new_chrtme_obj.__url__, test_url)


if __name__ == '__main__':
    unitttest.main()
