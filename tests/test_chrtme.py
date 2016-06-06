#!/usr/bin/env python

import unittest

try:
    from unittest import mock  # py3
except ImportError:
    import mock  # requires "pip install mock"

class ChrtmeTestToolkit(unittest.TestCase):
    """Base class for all Chrtme tests."""

    @classmethod
    def _get_working_val(cls, var_name):
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
        test_url = cls._get_working_val('url')
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

    def test_import_as_library(self):
        """Testing library import"""
        try:
            from .context import chrtme
        except ImportError:
            self.fail('Importing chrtme library failed')
        except:
            self.fail('Unexpected failure during chrtme import')

    def test_object(self):
        """Testing creating chrtme object"""
        try:
            test_url = self._get_working_val('url')
            cmd = ''
            chrtme_local_obj = self.chrtme_lib.Chrtme(
                url=test_url,
                cmd=cmd,
            )
        except:
            self.fail('Error during chrtme object creation')
        self.assertIsInstance(chrtme_local_obj, self.chrtme_lib.Chrtme)

    def test_object_has_download_url(self):
        """Testing Object URL attribute existence"""
        with self.assertRaises(TypeError, msg="URL not provided") as e:
            cmd = ''
            self.chrtme_lib.Chrtme(
                cmd=cmd
            )

    def test_obj_url_correctly_set(self):
        """Test if chrtme object URL correct set"""
        test_url = self._get_working_val('url')
        cmd = ''
        chrtme_local_obj = self.chrtme_lib.Chrtme(
            url=test_url,
            cmd=cmd
        )
        self.assertEqual(chrtme_local_obj._url, test_url)

    def test_obj_url_verifies_validity(self):
        """Test if broken URLs are identified"""
        cmd = ''
        broken_url = 'not_http://i.should.not.be.working.com'
        with self.assertRaises(ValueError, msg="Invalid URL not caught") as e:
            self.chrtme_lib.Chrtme(
                url=broken_url,
                cmd=cmd,
            )

    def test_obj_url_validity_location(self):
        """Test if the URL is correctly validated using file://"""
        test_url = 'file://i.should.be.working'
        cmd = ''
        chrtme_local_obj = self.chrtme_lib.Chrtme(
            url=test_url,
            cmd=cmd
        )
        self.assertEqual(chrtme_local_obj._url, test_url)

if __name__ == '__main__':
    unittest.main()
