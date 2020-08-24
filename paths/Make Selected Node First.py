# MenuTitle: Make Selected Node First
# -*- coding: utf-8 -*-
import GlyphsApp

__doc__ = """
Makes Selected nodes first on the path, if nothing selected will run Correct Path direction
"""

Font = Glyphs.font

# Run
Font.disableUpdateInterface()

for layer in Font.selectedLayers:
    if layer.selection:
        for node in layer.selection:
            node.makeNodeFirst()
    else:
        layer.correctPathDirection()

Font.enableUpdateInterface()
