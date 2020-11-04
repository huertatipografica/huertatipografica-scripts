# MenuTitle: Decompose Components for all Layers
# -*- coding: utf-8 -*-
import GlyphsApp

__doc__ = """
Like a cmd + shift + d for all layers on selected glyphs
"""

Font = Glyphs.font
selectedGlyphs = [x.parent for x in Font.selectedLayers]

# Run
Font.disableUpdateInterface()

def process(thisGlyph):
    thisGlyph.beginUndo()
    for layer in thisGlyph.layers:
        layer.decomposeComponents()

    thisGlyph.endUndo()

for thisGlyph in selectedGlyphs:
    process(thisGlyph)

Font.enableUpdateInterface()
