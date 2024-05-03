# MenuTitle: Check glyphs with no top anchor
# -*- coding: utf-8 -*-
__doc__ = """
Mark and opens a new windows with no top anchors.
"""
import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

outputString = ""

for thisLayer in selectedLayers:
    thisGlyphName = thisLayer.parent.name
    if "top" not in [a.name for a in thisLayer.anchors]:
        thisLayer.parent.color = 0
        outputString += "/" + thisGlyphName


Font.newTab(outputString)
