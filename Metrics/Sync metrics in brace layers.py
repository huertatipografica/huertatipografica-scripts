#MenuTitle: Sync metrics in brace layers
# -*- coding: utf-8 -*-
__doc__="""
Sync spacing interpolating values between extreme masters
"""

import GlyphsApp
import re

thisFont = Glyphs.font # frontmost font
masters = thisFont.masters # masters
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs

firstMaster = masters[0]
lastMaster = masters[-1]


def interpolate(x1, y1, x3, y3, x2):
	return ((float(x2) - float(x1)) * (float(y3) - float(y1)) / (float(x3) - float(x1))) + float(y1)

def getWeight(string):
	return re.sub(".*{|}.*", "", string)

def getSidebearings(name, weight):
	firstMasterLayer = thisFont.glyphs[name].layers[firstMaster.id]
	lastMasterLayer = thisFont.glyphs[name].layers[lastMaster.id]

	interpolatedLSB = interpolate(firstMaster.weightValue, firstMasterLayer.LSB, lastMaster.weightValue, lastMasterLayer.LSB, weight)
	interpolatedRSB = interpolate(firstMaster.weightValue, firstMasterLayer.RSB, lastMaster.weightValue, lastMasterLayer.RSB, weight)

	# Debugging
	# print "LEFT\t %s:\t%i <- -> %i\t(weight %s)" % (firstMaster.name, firstMasterLayer.LSB, firstMasterLayer.RSB, firstMaster.weightValue)
	# print "RIGHT\t %s:\t%i <- -> %i\t(weight %s)" % (lastMaster.name, lastMasterLayer.LSB, lastMasterLayer.RSB, lastMaster.weightValue)

	sidebearings = [interpolatedLSB, interpolatedRSB]

	return sidebearings

def process(thisLayer):
	thisGlyph = thisLayer.parent
	for i in range( len( thisGlyph.layers ) )[::-1]:
		currentLayer = thisGlyph.layers[i]
		# check name
		if currentLayer.name.endswith("}"):

			# Calculate and apply the thing
			weight = getWeight(currentLayer.name)
			interpolatedSidebearings = getSidebearings(thisGlyph.name, weight)
			currentLayer.LSB = interpolatedSidebearings[0]
			currentLayer.RSB = interpolatedSidebearings[1]
			print "%s:\t%i <- -> %i\t(weight %s)" % (currentLayer.name, currentLayer.LSB, currentLayer.RSB, weight)


thisFont.disableUpdateInterface()
Glyphs.clearLog()

if len(masters) == 2:
	for thisLayer in listOfSelectedLayers:
		thisGlyph = thisLayer.parent

		thisGlyph.beginUndo()

		process(thisLayer)

		thisGlyph.endUndo()
else:
	Message("Hey, wait a moment", 'This scripts needs a 2 masters font to work', OKButton="OK")

thisFont.enableUpdateInterface()

