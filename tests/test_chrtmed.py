#!/usr/bin/env python

import unittest

try:
    from unittest import mock  # py3
except ImportError:
    import mock  # requires "pip install mock"

class ChrtmeDaemonTestToolkit(unittest.TestCase):
    """Base class for all ChrtmeD tests."""

    @classmethod
    def setUp(cls):
        """Pre-test setup steps"""
        from .context import chrtmed
        cls.chrtmed_lib = chrtmed
        cls.chrtmed_local_obj = cls.chrtmed_lib.ChrtmeDaemon()

    @classmethod
    def tearDown(cls):
        """Post-test cleaning steps"""
        del cls.chrtmed_lib
        del cls.chrtmed_local_obj


class ChrtmeDaemonTest(ChrtmeDaemonTestToolkit):
    """Basic tests for the ChrtmeDaemon Class."""

    def testImportAsLibrary(self):
        """Testing library import"""
        try:
            from .context import chrtmed
        except ImportError:
            self.fail('Importing chrtmed library failed')
        except:
            self.fail('Unexpected failure during chrtmed import')
        

