#MenuTitle: Width comparing
# -*- coding: utf-8 -*-
__doc__="""
Comparing widths in different masters. Mark when is different
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs

Glyphs.clearLog()

# Config
color = 0
precision = 5 # Range for comparing results. Lower values results in more accuracy


def process( thisGlyph ):
	firstMasterWidth = thisGlyph.layers[thisFont.masters[0].id].width
	for master in thisFont.masters:
		width = thisGlyph.layers[master.id].width
		if width - firstMasterWidth not in range(-precision,precision):
			thisGlyph.color = color
			break


thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyph.beginUndo() # begin undo
	process( thisGlyph )
	thisGlyph.endUndo()   # end undo


thisFont.enableUpdateInterface() # re-enables UI updates in Font View

