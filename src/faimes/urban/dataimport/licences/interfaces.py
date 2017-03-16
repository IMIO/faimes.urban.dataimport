# -*- coding: utf-8 -*-


from plone.theme.interfaces import IDefaultPloneLayer

from imio.urban.dataimport.urbaweb.interfaces import IUrbawebDataImporter


class IFaimesDataImporter(IUrbawebDataImporter):
    """ marker interface for Faimes Agorawin importer """


class IFaimesUrbanDataimportLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""
