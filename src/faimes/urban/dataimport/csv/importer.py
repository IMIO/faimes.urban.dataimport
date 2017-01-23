# -*- coding: utf-8 -*-
from faimes.urban.dataimport.csv import objectsmapping
from faimes.urban.dataimport.csv import valuesmapping
from imio.urban.dataimport.config import IMPORT_FOLDER_PATH
from imio.urban.dataimport.csv.importer import CSVImportSource, CSVDataExtractor, CSVDataImporter
from imio.urban.dataimport.csv.interfaces import ICSVImportSource, ICSVImporter

from zope.interface import implements

import csv

from imio.urban.dataimport.mapping import ObjectsMapping, ValuesMapping


class FaimesCSVMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return objectsmapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return objectsmapping.FIELDS_MAPPINGS


class FaimesCSVValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):

        return valuesmapping.VALUES_MAPS.get(mapping_name, None)
