# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm


class FaimesImporterSettingsForm(ImporterSettingsForm):
    """ """


class FaimesImporterSettings(ImporterSettings):
    """ """
    form = FaimesImporterSettingsForm


class FaimesImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = FaimesImporterSettings
