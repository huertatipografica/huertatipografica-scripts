#MenuTitle: Tab with punctuation
# -*- coding: utf-8 -*-
__doc__="""
Combine selected glyphs in a new Tab with all the punctuation characters present in the font
"""
import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font

selectedGlyphs = [ x.parent.name for x in Font.selectedLayers]
combiningGroup = [glyph.name for glyph in Font.glyphs if glyph.category == 'Punctuation']

outputString = ''

# Print all glyphs
for glyph in selectedGlyphs:
	outputString +='/'+glyph
outputString += '\n'

# Combining loop
for glyph in selectedGlyphs:
	# Each combining
	for combining in combiningGroup:
		outputString +='/'+combining+'/'+glyph+'/'+combining+'/space'


Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", outputString, True )
