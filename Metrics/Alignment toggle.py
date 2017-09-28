#MenuTitle: Alignment: toggle
# -*- coding: utf-8 -*-
__doc__="""
Toggle automatic alignment for all components in all selected glyphs. Thanks @mekkablue
"""

import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers

Glyphs.clearLog()

def process( thisLayer ):
	for thisComp in thisLayer.components:
		if thisComp.automaticAlignment:
			return disable(thisLayer)
	return enable( thisLayer )

def disable( thisLayer ):
	for thisComp in thisLayer.components:
		thisComp.setDisableAlignment_( True )
	print "Disabled automatic alignment in", thisLayer.parent.name

def enable( thisLayer ):
	for thisComp in thisLayer.components:
		thisComp.setDisableAlignment_( False )
	print "Enabled automatic alignment in", thisLayer.parent.name

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent

	thisGlyph.beginUndo()
	print process( thisLayer )
	thisGlyph.endUndo()
