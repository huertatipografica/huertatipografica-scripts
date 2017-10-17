#MenuTitle: Tab with compound glyphs
# -*- coding: utf-8 -*-
__doc__="""
Based con mekablue's "New Edit tab with compound glyphs".
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
FontMaster = Font.selectedFontMaster
selectedLayers = Font.selectedLayers

editString = ""
Output = ""

for thisLayer in selectedLayers:
	thisGlyphName = thisLayer.parent.name
	compoundList = [ g.name for g in Font.glyphs if thisGlyphName in [ c.componentName for c in g.layers[ FontMaster.id ].components ] ]
	if len(compoundList) > 1 :
		Output += "Compounds with %s: " % thisGlyphName + " ".join( compoundList ) + "\n"
		editString += "\n/" + thisGlyphName + "/colon  /" + "/".join( compoundList )
		# editString += "\n /%s:  /%s" % ( thisGlyphName, "/".join( compoundList ) )
	else :
		Output += "No compound glyphs with %s\n" % thisGlyphName

editString = editString.lstrip()
print Output

thisFont.newTab(editString)