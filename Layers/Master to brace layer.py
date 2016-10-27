#MenuTitle: Master to brace layer
# -*- coding: utf-8 -*-
__doc__="""
Duplicates the selected master in a brace layer in selected characters.
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs



def process( thisLayer ):
	thisGlyph = thisLayer.parent

	# duplicate this master into a new brace layer
	newLayer = thisLayer.copy()
	newLayer.name = "{%d}" % thisFontMaster.weightValue
	newLayer.associatedMasterId = thisFont.masters[0].id # attach to first master

	thisFont.glyphs[thisGlyph.name].layers.append(newLayer)


thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
	thisGlyph = thisLayer.parent
	print "Re-interpolating", thisGlyph.name
	thisGlyph.beginUndo() # begin undo
	process( thisLayer )
	thisGlyph.endUndo()   # end undo


thisFont.enableUpdateInterface() # re-enables UI updates in Font View
