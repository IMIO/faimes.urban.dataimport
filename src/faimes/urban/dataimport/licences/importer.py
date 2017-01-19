# -*- coding: utf-8 -*-

from zope.interface import implements

from faimes.urban.dataimport.licences import objectsmapping
from faimes.urban.dataimport.licences import valuesmapping
from imio.urban.dataimport.mapping import ObjectsMapping, ValuesMapping
from imio.urban.dataimport.urbaweb.importer import UrbawebDataImporter
from faimes.urban.dataimport.interfaces import IFaimesDataImporter


class FaimesDataImporter(UrbawebDataImporter):
    """ """

    implements(IFaimesDataImporter)


class LicencesMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return objectsmapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return objectsmapping.FIELDS_MAPPINGS


class LicencesValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):

        return valuesmapping.VALUES_MAPS.get(mapping_name, None)
