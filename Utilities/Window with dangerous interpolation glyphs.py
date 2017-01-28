#MenuTitle: Window with dangerous interpolation glyphs
# -*- coding: utf-8 -*-
__doc__="""
Opens a new tab with glyphs that may produce funny interpolations. Useful for compatible glyphs
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

# Create array
glyphList = []

# Functions for checking
def checkPaths( thisLayer ):
	previousCount = 0
	for thisPath in thisLayer.paths:
		if len(thisPath.nodes) == previousCount:
			return True
		previousCount = len(thisPath.nodes)
	return False

def checkComponents( thisLayer ):
	componentList = []
	for thisComponent in thisLayer.components:
		componentList.append(thisComponent.componentName)
	if len(componentList) != len(set(componentList)):
		return True
	return False

# Run the script
for thisLayer in selectedLayers:
	if checkPaths(thisLayer) or checkComponents(thisLayer):
		glyphList.append(thisLayer.parent.name)

if glyphList:
	tabString = "/"+"/".join(glyphList)
	Font.newTab(tabString)
else:
	Message("No dangerous glyphs", "There are not repeated components or paths with the same ammount of points in selected glyphs.", OKButton="Yeah")