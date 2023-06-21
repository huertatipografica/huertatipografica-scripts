# MenuTitle: Alignment: enable
# -*- coding: utf-8 -*-
__doc__ = """
Enable automatic alignment for all components in all selected glyphs. Thanks @mekkablue
"""

import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers

Glyphs.clearLog()


def process(thisLayer):
    for thisComp in thisLayer.components:
        enable(thisLayer)


def enable(thisLayer):
    for thisComp in thisLayer.components:
        thisComp.setDisableAlignment_(False)
    print("Enabled automatic alignment in", thisLayer.parent.name)


for thisLayer in selectedLayers:
    thisGlyph = thisLayer.parent

    thisGlyph.beginUndo()
    print(process(thisLayer))
    thisGlyph.endUndo()
