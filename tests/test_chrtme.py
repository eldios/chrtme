#!/usr/bin/env python

import unittest

try:
    from unittest import mock  # py3
except ImportError:
    import mock  # requires "pip install mock"

from chrtme import ChRtMe

class ChrtmeTestToolkit(unittest.TestCase):
    """Base class for all Chrtme tests."""
    pass

class ChrtmeTest(ChrtmeTestToolkit):
    """Basic tests for the Chrtme Class."""

    def setUp(self):
        """Pre-test setup steps"""
        pass

    def tearDown(self):
        """Post-test cleaning steps"""
        pass

    pass
