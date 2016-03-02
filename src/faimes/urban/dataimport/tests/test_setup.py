# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from faimes.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of faimes.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if faimes.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('faimes.dataimport'))

    def test_uninstall(self):
        """Test if faimes.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['faimes.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('faimes.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IFaimesDataimportLayer is registered."""
        from faimes.dataimport.interfaces import IFaimesDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IFaimesDataimportLayer in utils.registered_layers())
