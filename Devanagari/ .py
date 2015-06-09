#MenuTitle: Zerowidth
# -*- coding: utf-8 -*-
__doc__="""
Set width to zero
"""

import GlyphsApp
Font = Glyphs.font
selectedLayers = Font.selectedLayers

# Alternate width
ancho = 600

Font.disableUpdateInterface()

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyph.beginUndo()
	if thisLayer.width == 0:
		thisLayer.width = ancho
		# thisLayer.LSB = ( thisLayer.LSB + thisLayer.RSB ) // 2
		# thisLayer.width = ancho
	elif thisLayer.width == ancho:
		# thisLayer.LSB = -( thisLayer.LSB + thisLayer.RSB ) // 2
		thisLayer.width = 0
	thisGlyph.endUndo()

Font.enableUpdateInterface()