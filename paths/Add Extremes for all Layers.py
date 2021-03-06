# MenuTitle: Add Extremes for all Layers
# -*- coding: utf-8 -*-
import GlyphsApp
from addExtremes import process

__doc__ = """
Like a cmd + u for all layers on selected glyphs
"""

Font = Glyphs.font
selectedGlyphs = [x.parent for x in Font.selectedLayers]

# Run
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
    process(thisGlyph)

Font.enableUpdateInterface()
