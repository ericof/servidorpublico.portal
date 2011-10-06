# -*- coding: utf-8 -*-

import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME

from plone.app.testing import login
from plone.app.testing import setRoles

from servidorpublico.portal.config import PROJECTNAME
from servidorpublico.portal.testing import INTEGRATION_TESTING

DEPENDENCIES = (
    'PloneFormGen',
    'Maps',
    )


class TestInstall(unittest.TestCase):
    """ensure product is properly installed"""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = getattr(self.portal, 'portal_quickinstaller')

    def test_installed(self):
        self.failUnless(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_dependencies_installed(self):
        for p in DEPENDENCIES:
            self.failUnless(self.qi.isProductInstalled(p),
                            '%s not installed' % p)


class TestConfig(unittest.TestCase):
    """ Ensure we have configured this portal """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.pp = getattr(self.portal, 'portal_properties')

    def test_title(self):
        self.failUnless('Portal do Servidor Público' in 
                         self.portal.title, 'Title not applied')

    def test_email_configs(self):
        self.failUnless(self.portal.email_from_address,
                        'E-mail address not set')
        self.failUnless(self.portal.email_from_name,
                        'E-mail name not set')

    def test_localTimeFormat(self):
        self.failUnless(self.pp.site_properties.localTimeFormat == '%d/%m/%Y',
                        'Time format not set')

    def test_allowed_combined_language_code(self):
        self.lang = getattr(self.portal, 'portal_languages')
        self.failUnless(self.lang.use_combined_language_codes == 1,
                        'Combined language code not supported')

    def test_language_set(self):
        self.lang = getattr(self.portal, 'portal_languages')
        self.failUnless(self.lang.getDefaultLanguage() == 'pt-br',
                        'Language not set')


class TestUninstall(unittest.TestCase):
    """ensure product is properly uninstalled"""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.failIf(self.qi.isProductInstalled(PROJECTNAME))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
