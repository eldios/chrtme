#!/usr/bin/env python

import unittest

try:
    from unittest import mock  # py3
except ImportError:
    import mock  # requires "pip install mock"

class ChrtmeTestToolkit(unittest.TestCase):
    """Base class for all Chrtme tests."""

    @classmethod
    def _getWorkingVal(cls,var_name):
        """Easily get values that are known to work"""
        from os import getcwd
        if var_name == 'url':
            return 'http://working.URL'
        elif var_name == 'location':
            return getcwd()

    @classmethod
    def setUp(cls):
        """Pre-test setup steps"""
        from .context import chrtme
        cls.chrtme_lib = chrtme
        test_url = cls._getWorkingVal('url')
        cmd = ''
        cls.chrtme_obj = cls.chrtme_lib.Chrtme(
            url=test_url,
            cmd=cmd
        )

    @classmethod
    def tearDown(cls):
        """Post-test cleaning steps"""
        del cls.chrtme_lib
        del cls.chrtme_obj


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
            test_url = self._getWorkingVal('url')
            cmd = ''
            chrtme_local_obj = self.chrtme_lib.Chrtme(
                url=test_url,
                cmd=cmd,
            )
        except:
            self.fail('Error during chrtme object creation')
        self.assertIsInstance(chrtme_local_obj, self.chrtme_lib.Chrtme)

    def testObjHasDownloadURL(self):
        """Testing Object URL attribute existence"""
        with self.assertRaises(TypeError, msg="URL not provided") as e:
            cmd = ''
            chrtme_local_obj = self.chrtme_lib.Chrtme(
                cmd=cmd
            )

    def testObjURLCorrectlySet(self):
        """Test if chrtme object URL correct set"""
        test_url = self._getWorkingVal('url')
        cmd = ''
        chrtme_local_obj = self.chrtme_lib.Chrtme(
            url=test_url,
            cmd=cmd
        )
        self.assertEqual(chrtme_local_obj._url, test_url)

    def testObjURLVerifiesValidity(self):
        """Test if broken URLs are identified"""
        cmd = ''
        broken_url = 'not_http://i.should.not.be.working.com'
        with self.assertRaises(ValueError, msg="Invalid URL not caught") as e:
            chrtme_local_obj = self.chrtme_lib.Chrtme(
                url=broken_url,
                cmd=cmd,
            )

    def testObjURLValidityLocation(self):
        """Test if the URL is correctly validated using file://"""
        test_url = 'file://i.should.be.working'
        cmd = ''
        chrtme_local_obj = self.chrtme_lib.Chrtme(
            url=test_url,
            cmd=cmd
        )
        self.assertEqual(chrtme_local_obj._url, test_url)

if __name__ == '__main__':
    unitttest.main()
