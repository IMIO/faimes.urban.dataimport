# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.mapper import AccessMapper as Mapper
from imio.urban.dataimport.exceptions import NoObjectToCreateException
from imio.urban.dataimport.factory import BaseFactory

from Products.CMFPlone.utils import normalizeString

import re


# Factory
class ParcellingFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        return self.site.urban.parcellings

    def getPortalType(self, container, **kwargs):
        return 'ParcellingTerm'


class TitleMapper(Mapper):

    regex = '(?P<subdivider>\D*?)\s+(?P<label>\d+/\d+)'

    def mapLabel(self, line):
        title = self.getData('Lotis')
        if not title:
            raise NoObjectToCreateException

        title = re.search(self.regex, title)
        if title:
            return title.group('label')
        return ''

    def mapSubdividername(self, line):
        title = self.getData('Lotis')
        if not title:
            raise NoObjectToCreateException

        title = re.search(self.regex, title)
        if title:
            return title.group('subdivider')
        return ''


class IdMapper(Mapper):

    def mapId(self, line):
        title = self.getData('Lotis')
        parcelling_id = normalizeString(title)
        return parcelling_id
