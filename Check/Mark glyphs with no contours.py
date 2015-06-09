#MenuTitle: Mark glyphs with no contours
# -*- coding: utf-8 -*-
__doc__="""
Mark glyphs with no contours in the current Layer
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

outputString = ''

for thisLayer in selectedLayers:
	count = 0
	if thisLayer.parent.subCategory != 'Space':
		for thisPath in thisLayer.paths:
			count += len(thisPath.nodes)
		if count < 2:
			thisLayer.parent.color=6
			outputString +='/'+thisLayer.parent.name

print "Glyphs with no contours in master: " + outputString