#MenuTitle: Tab with all possible combinations
# -*- coding: utf-8 -*-
__doc__="""
Combine all selected glyphs in a new tab.
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
selectedLayers = thisFont.selectedLayers # active layers of selected glyphs

Glyphs.clearLog()

tabString = ''

for n in selectedLayers:
	for i in selectedLayers:
		tabString += "/" + n.parent.name
		tabString += "/" + i.parent.name
	tabString += "/" + n.parent.name
	tabString += '\n'

thisFont.newTab(tabString)


