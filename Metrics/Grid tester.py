# MenuTitle: Grid tester
# -*- coding: utf-8 -*-
__doc__ = """
Makes a grid combining selected glyphs in a new Tab. Useful for seeing unbalanced weights in glyphs.
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers
qty = len(selectedLayers)

# Config
repetitions = 1

# Clean
Glyphs.clearLog()
outputString = ""

# Make grid
for times in xrange(0, repetitions):
    for i in xrange(0, qty):
        outputString += "\n"

        for g in selectedLayers[i:] + selectedLayers[:i]:
            outputString += "/" + g.parent.name


Font.newTab(outputString)
