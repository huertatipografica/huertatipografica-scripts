# MenuTitle: Delete Anchors for all Layers
# -*- coding: utf-8 -*-
import GlyphsApp

__doc__ = """
Works for all layers on selected glyphs
"""

Font = Glyphs.font
selectedGlyphs = [x.parent for x in Font.selectedLayers]

# Run
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
    thisGlyph.beginUndo()
    for layer in thisGlyph.layers:
        layer.anchors = []

    thisGlyph.endUndo()

Font.enableUpdateInterface()
