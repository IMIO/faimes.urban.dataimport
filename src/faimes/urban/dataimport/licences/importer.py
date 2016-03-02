# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.urbaweb.importer import UrbawebDataImporter
from faimes.urban.dataimport.interfaces import IFaimesDataImporter


class FaimesDataImporter(UrbawebDataImporter):
    """ """

    implements(IFaimesDataImporter)
