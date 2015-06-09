#MenuTitle: Enable alignment for selected glyphs
# -*- coding: utf-8 -*-
__doc__="""
Enables automatic alignment for all components in all selected glyphs. (The opposite to makkablue's Enable alignment for selected glyphs)
"""

import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers

def process( thisLayer ):
	for thisComp in thisLayer.components:
		thisComp.setDisableAlignment_( False )

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	print "Enabling automatic alignment in", thisGlyph.name
	thisGlyph.beginUndo()
	process( thisLayer )
	thisGlyph.endUndo()
