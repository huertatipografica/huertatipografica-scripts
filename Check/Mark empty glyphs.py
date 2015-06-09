#MenuTitle: Mark empty glyphs
# -*- coding: utf-8 -*-
__doc__="""
Mark empty Glyphs in current Layer
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

outputString = ''

for thisLayer in selectedLayers:
	count = len(thisLayer.paths) + len(thisLayer.components)
	if count == 0 and thisLayer.parent.subCategory != 'Space':
		outputString +='/'+thisLayer.parent.name
		thisLayer.parent.color=0

print "Empty Glyphs in master: " + outputString