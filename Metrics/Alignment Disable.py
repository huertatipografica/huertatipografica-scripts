# MenuTitle: Alignment: disable
# -*- coding: utf-8 -*-
__doc__ = """
Disable automatic alignment for all components in all selected glyphs. Thanks @mekkablue
"""

import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers

Glyphs.clearLog()


def process(thisLayer):
    for thisComp in thisLayer.components:
        disable(thisLayer)


def disable(thisLayer):
    for thisComp in thisLayer.components:
        thisComp.setDisableAlignment_(True)
    print("Disabled automatic alignment in", thisLayer.parent.name)


for thisLayer in selectedLayers:
    thisGlyph = thisLayer.parent

    thisGlyph.beginUndo()
    process(thisLayer)
    thisGlyph.endUndo()
