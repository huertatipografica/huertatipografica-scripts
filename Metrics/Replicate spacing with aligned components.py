#MenuTitle: Replicate spacing with aligned components
# -*- coding: utf-8 -*-
__doc__="""
Enables alignment and adds metric keys to replicate the current spacing
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs


# Config
# Range of tolerance. Will avoid keys for variations within the offset value:
offset = 5

def enable( thisLayer ):
	# Delete actual keys
	thisLayer.setLeftMetricsKey_(None)
	thisLayer.setWidthMetricsKey_(None)
	thisLayer.setRightMetricsKey_(None)

	# enables alignment
	for thisComp in thisLayer.components:
		thisComp.setDisableAlignment_( False )


Glyphs.clearLog()
for thisLayer in listOfSelectedLayers:
	thisGlyph = thisLayer.parent

	thisGlyph.beginUndo()

	# Store Values
	oldRSB = thisLayer.RSB
	oldLSB = thisLayer.LSB

	enable( thisLayer )

	# Store New values
	newRSB = thisLayer.RSB
	newLSB = thisLayer.LSB

	# Calculate difference
	diffRSB = oldRSB - newRSB
	diffLSB = oldLSB - newLSB

	# Set new keys
	if abs(diffRSB) > abs(offset):
		newKey = "==%+d" % (diffRSB)
		thisLayer.setRightMetricsKey_(newKey)
		print "--%s -> %s" % (thisLayer.parent.name, newKey)

	if abs(diffLSB) > abs(offset):
		newKey = "==%+d" % (diffLSB)
		thisLayer.setLeftMetricsKey_(newKey)
		print "--%s <- %s" % (thisLayer.parent.name, newKey)


	thisGlyph.endUndo()



