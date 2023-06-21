# MenuTitle: Rhythmic test
# -*- coding: utf-8 -*-
__doc__ = """
Repeat and combine selected glyphs in a new Tab. Create a 'spacingGlyph' character with zero spacing for better results.
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

repetitions = 5

outputString = ""
Glyphs.clearLog()

# Check if spacingGlyph exists
if Font.glyphs["spacingGlyph"]:
    spacingGlyph = "spacingGlyph"
    print("Showing results with spacingGlyph")
else:
    spacingGlyph = "bar"
    print(
        "The glyph spacingGlyph is not created. Showing results with "
        + spacingGlyph
        + " as fallback"
    )

# Add three times
for thisLayer in selectedLayers:
    thisGlyphName = thisLayer.parent.name
    for x in range(0, repetitions):
        outputString += "/" + thisGlyphName

# Add one time
outputString += "\n"
for thisLayer in selectedLayers:
    thisGlyphName = thisLayer.parent.name
    outputString += "/" + thisGlyphName

# Add character for center glyphs
outputString += "\n/" + spacingGlyph

for thisLayer in selectedLayers:
    thisGlyphName = thisLayer.parent.name
    outputString += "/" + thisGlyphName + "/" + spacingGlyph

# print outputString
Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_(
    "addTabWithString:", outputString, True
)
