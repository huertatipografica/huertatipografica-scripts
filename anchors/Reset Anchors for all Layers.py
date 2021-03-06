# MenuTitle: Reset Anchors for all Layers
# -*- coding: utf-8 -*-
import GlyphsApp
from anchorReset import process

__doc__ = """
Like a cmd + alt + u for all layers on selected glyphs
"""

Font = Glyphs.font
selectedGlyphs = [x.parent for x in Font.selectedLayers]

# Run
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
    process(thisGlyph, True)

Font.enableUpdateInterface()
