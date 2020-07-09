# MenuTitle: Reset Anchors for all Layers
# -*- coding: utf-8 -*-
import GlyphsApp
__doc__ = """
Like a cmd + alt + u for all layers on selected glyphs
"""


Font = Glyphs.font
selectedGlyphs = [x.parent for x in Font.selectedLayers]


def process(thisGlyph):
    thisGlyph.beginUndo()
    for layer in thisGlyph.layers:
        layer.anchors = []
        layer.addMissingAnchors()

    thisGlyph.endUndo()

# Run
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
    process(thisGlyph)

Font.enableUpdateInterface()
