#MenuTitle: Lowest and highest glyphs
# -*- coding: utf-8 -*-
__doc__="""
Reports and open a new tab with lowest and highest glyphs in selected layers. This is stolen from mekkablue :)
"""

import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers
Doc = Glyphs.currentDocument

Glyphs.clearLog()
Glyphs.showMacroWindow()

# Config
limit = 20

print "%s (master: %s)" % (Font.familyName, Font.selectedFontMaster.name)
print "Highest selected glyphs:"
outputString = 'Highest\n'


sortedNameHeightPairs = sorted([[l.parent.name,  l.bounds.origin.y + l.bounds.size.height] for l in selectedLayers], key=lambda x: -x[1])
for thisLayerPair in sortedNameHeightPairs[:limit]:
	print "- %s: %.1f" % ( thisLayerPair[0], thisLayerPair[1] )
	outputString +='/'+thisLayerPair[0]

print "\nLowest selected glyphs:"
outputString += '\nLowest\n'

sortedNameHeightLowestPairs = sorted([ [l.parent.name,  l.bounds.origin.y] for l in selectedLayers], key=lambda x: x[1])
for thisLayerPair in sortedNameHeightLowestPairs[:limit]:
	print "- %s: %.1f" % ( thisLayerPair[0], thisLayerPair[1] )
	outputString +='/'+thisLayerPair[0]

Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", outputString, True )
