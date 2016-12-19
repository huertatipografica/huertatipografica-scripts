#MenuTitle: Window with different cases
# -*- coding: utf-8 -*-
__doc__="""
Opens a new edit tab with current glyphs in both cases —and small caps (configurable).
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs

# Config
separator = False # Setup separator if you want, for example 'space'
sc = True # If you wanna include smallcaps

glyphList = []

for layer in listOfSelectedLayers:
	name = layer.parent.name
	# Uppercase
	glyphList.append(name[0].upper() + name[1:] )
	# Small Caps
	if sc:
		glyphList.append(name.lower() + ".sc")
	# Lower
	glyphList.append(name.lower())
	# Separator
	if separator:
		glyphList.append(separator)


tabString = "/"+"/".join(glyphList)
thisFont.newTab(tabString)