# MenuTitle: Tab with glyphs ordered by height
# -*- coding: utf-8 -*-
__doc__ = """
Window with glyphs ordered by height
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

# Create array
glyphs = []

# Fill array
for thisLayer in selectedLayers:
    if thisLayer.parent.subCategory != "Space":
        count = thisLayer.bounds.size.height
        glyphs.append([count, thisLayer.parent.name])

# Sort Glyphs by node count
sortedGlyphs = sorted(glyphs)  # order by node count

# Create collection grouped by node count
outputArray = {}
actualCount = False

for g in sortedGlyphs:
    if actualCount == False or actualCount != g[0]:
        # cambia el count y agrega key
        actualCount = g[0]
        outputArray[actualCount] = []

    # Add glyph
    outputArray[actualCount].append(g[1])

# Reset
actualCount = False

# Create output
outputString = ""

for count in outputArray:
    outputString += "\n"

    for x in outputArray[count]:
        outputString += "/" + x


Font.newTab(outputString)
