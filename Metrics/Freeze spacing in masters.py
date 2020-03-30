#MenuTitle: Freeze spacing in masters
# -*- coding: utf-8 -*-
__doc__="""
Set metric keys for each layer of selected glyphs. Useful for setting exceptions to HT Letterspacer
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs


for thisLayer in listOfSelectedLayers:
    thisGlyph = thisLayer.parent

    thisGlyph.beginUndo()

    for layer in thisGlyph.layers:
        if layer.associatedMasterId:
            # Freeze Values
            layer.rightMetricsKey = '==%s' % (layer.RSB)
            layer.leftMetricsKey = '==%s' % (layer.LSB)
            layer.syncMetrics()

    thisGlyph.endUndo()



