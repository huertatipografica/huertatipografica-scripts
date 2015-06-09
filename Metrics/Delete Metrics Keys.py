#MenuTitle: Delete Metrics Keys
# -*- coding: utf-8 -*-
__doc__="""
Leave only numbers and delete all metrics keys in selected Glyphs.
"""

import GlyphsApp
Font = Glyphs.font
selectedLayers = Font.selectedLayers

Font.disableUpdateInterface()

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyph.beginUndo()
	thisGlyph.leftMetricsKey=None
	thisGlyph.rightMetricsKey=None
	thisGlyph.endUndo()

Font.enableUpdateInterface()