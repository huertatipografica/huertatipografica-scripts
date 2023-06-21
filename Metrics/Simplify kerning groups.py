# MenuTitle: Simplify kerning groups
# -*- coding: utf-8 -*-
__doc__ = """
Goes through the kerning groups of the selected glyphs and try to reduce them looking for its parents
"""

import GlyphsApp

thisFont = Glyphs.font  # frontmost font
thisFontMaster = thisFont.selectedFontMaster  # active master
listOfSelectedLayers = thisFont.selectedLayers  # active layers of selected glyphs


def setParent(layer):

    glyph = layer.parent
    left = glyph.leftKerningGroup
    right = glyph.rightKerningGroup

    if left and thisFont.glyphs[left]:
        while (
            left != thisFont.glyphs[left].leftKerningGroup
            and thisFont.glyphs[left].leftKerningGroup
        ):
            left = thisFont.glyphs[left].leftKerningGroup

    if right and thisFont.glyphs[right]:
        while (
            right != thisFont.glyphs[right].rightKerningGroup
            and thisFont.glyphs[right].rightKerningGroup
        ):
            right = thisFont.glyphs[right].rightKerningGroup

    glyph.leftKerningGroup = left
    glyph.rightKerningGroup = right


Glyphs.clearLog()
for thisLayer in listOfSelectedLayers:
    thisGlyph = thisLayer.parent
    thisGlyph.beginUndo()
    setParent(thisLayer)
    thisGlyph.endUndo()
