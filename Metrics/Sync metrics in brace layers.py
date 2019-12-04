#MenuTitle: Sync metrics in brace layers
# -*- coding: utf-8 -*-
__doc__="""
Sync spacing interpolating the metrics in the brace layers
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
masters = thisFont.masters # masters
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs

def process(thisLayer):
    thisGlyph = thisLayer.parent
    for i in range( len( thisGlyph.layers ) )[::-1]:
        currentLayer = thisGlyph.layers[i]
        # check name
        if currentLayer.name.startswith("{") and currentLayer.name.endswith("}"):
            old = currentLayer.copy()

            # Reinterpolate
            currentLayer.reinterpolate()

            # apply oldData except metrics
            currentLayer.guides = old.guides
            currentLayer.annotations = old.annotations
            currentLayer.hints = old.hints
            currentLayer.anchors = old.anchors
            currentLayer.paths = old.paths
            currentLayer.leftMetricsKey = old.leftMetricsKey
            currentLayer.rightMetricsKey = old.rightMetricsKey
            currentLayer.widthMetricsKey = old.widthMetricsKey
            currentLayer.background = old.background
            currentLayer.backgroundImage = old.backgroundImage

            if old.RSB != currentLayer.RSB or old.LSB != currentLayer.LSB:
                print "%s:\t%i <- -> %i" % (currentLayer.name, currentLayer.LSB, currentLayer.RSB)

thisFont.disableUpdateInterface()
Glyphs.clearLog()


for thisLayer in listOfSelectedLayers:
    thisGlyph = thisLayer.parent

    thisGlyph.beginUndo()

    process(thisLayer)

    thisGlyph.endUndo()

thisFont.enableUpdateInterface()

