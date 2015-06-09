#MenuTitle: iMetralladora
# -*- coding: utf-8 -*-
__doc__="""
Combine selected with iMatra character. Useful for test 'pres' feature on Devanagari fonts
"""
import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

interCharacter = "/iMatra-deva"

outputString = ""

for thisLayer in selectedLayers:
	thisGlyphName = thisLayer.parent.name
	outputString += interCharacter + '/'+ thisGlyphName + '\n'


Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", outputString, True )
