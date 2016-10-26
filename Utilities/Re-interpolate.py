#MenuTitle: Re-interpolate Regular master
# -*- coding: utf-8 -*-
__doc__="""
Re interpolate the regular weight. Useful for sync contours adjustments in a 3 master set up.
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs

# Config
# Applies on the following masters
admitedMasters = [
	'Regular',
	'Regular Italic',
]

def process( thisLayer ):
	thisGlyph = thisLayer.parent

	for thatLayer in thisGlyph.layers:
		if thatLayer.name in admitedMasters:
			thatLayer.reinterpolate()

thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
	thisGlyph = thisLayer.parent
	print "Re-interpolating", thisGlyph.name
	thisGlyph.beginUndo() # begin undo
	process( thisLayer )
	thisGlyph.endUndo()   # end undo

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
