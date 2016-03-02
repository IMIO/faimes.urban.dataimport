# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.interfaces import IAccessImporter

from plone.theme.interfaces import IDefaultPloneLayer


class IFaimesDataImporter(IAccessImporter):
    """ marker interface for Faimes Agorawin importer """


class IFaimesUrbanDataimportLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""
