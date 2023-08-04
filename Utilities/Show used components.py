# MenuTitle: Show used components
# -*- coding: utf-8 -*-
__doc__ = """
Output in scripts panel the components used in current selection
"""

import GlyphsApp

thisFont = Glyphs.font  # frontmost font
listOfSelectedLayers = thisFont.selectedLayers  # active layers of selected glyphs

Glyphs.clearLog()
Glyphs.showMacroWindow()


def process(listOfSelectedLayers):

    components = []

    for thisLayer in listOfSelectedLayers:
        [components.append(c.componentName) for c in thisLayer.components]

    for component in set(components):
        print(component)


thisFont.disableUpdateInterface()  # suppresses UI updates in Font View

process(listOfSelectedLayers)

thisFont.enableUpdateInterface()  # re-enables UI updates in Font View
