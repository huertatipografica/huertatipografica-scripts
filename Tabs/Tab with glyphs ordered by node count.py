# MenuTitle: Tab with glyphs ordered by node count
# -*- coding: utf-8 -*-
__doc__ = """
Window with glyphs ordered by node count
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

# Create array
glyphs = []

# Fill array
for thisLayer in selectedLayers:
    count = 0
    if thisLayer.parent.subCategory != "Space":
        for thisPath in thisLayer.paths:
            count += len(thisPath.nodes)
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
