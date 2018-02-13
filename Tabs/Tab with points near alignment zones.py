#MenuTitle: Tab with points near alignment zones
# -*- coding: utf-8 -*-
__doc__="""
Useful for checking vertical alignment / hinting problems. Partialy stolen from guidoferreyra's script
"""
import GlyphsApp

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs
fontMaster = thisFont.selectedFontMaster # active master

# Init
glyphList = []

# Config
umbral = 15

# Thanks Guido :)
def zoneList( master ):
	zoneList = []
	for z in master.alignmentZones:
		zoneOrigin, zoneSize = int(z.position), int(z.size)
		zoneList.append( ( zoneOrigin, zoneOrigin+zoneSize ) )
	return zoneList

def inZone(thisLayer, masterZones, posX, posY, umbral):
	for thisZone in masterZones:
		zoneOrigin = thisZone[0]
		zoneEnd = thisZone[1]

		if zoneOrigin < zoneEnd:
			if posY >= zoneOrigin-umbral and posY <= zoneEnd+umbral:
				return True
		elif zoneOrigin > zoneEnd:
			if posY <= zoneOrigin+umbral and posY >= zoneEnd-umbral:
				return True

masterZones = zoneList( fontMaster )
# print masterZones


for thisLayer in listOfSelectedLayers:
	for thisPath in thisLayer.paths:
		for thisNode in thisPath.nodes:
			if thisNode.type != GSOFFCURVE:
				posY = thisNode.y
				posX = thisNode.x
				if inZone (thisLayer, masterZones, posX, posY, umbral=0):
					pass
				elif inZone (thisLayer, masterZones, posX, posY, umbral):
					glyphList.append(thisLayer.parent.name)
					break
	else:
		continue
	break


if len(glyphList):
	tabString = "/"+"/".join(set(glyphList))
	thisFont.newTab(tabString)
else:
	Message("Nice :)", "No suspicious points in selected glyphs.", OKButton="OK")




