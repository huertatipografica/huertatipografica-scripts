#MenuTitle: Deva composer
# -*- coding: utf-8 -*-
__doc__="""
Makes a new tab with the characters needed to type the selected conjuncts or halfforms.
"""

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

outputString = ''

for thisGlyph in selectedGlyphs:
	# Conjuncts
	if thisGlyph.script == 'devanagari' and thisGlyph.category =='Letter' and thisGlyph.subCategory =='Ligature':
		outputString += '/' + thisGlyph.name.replace("_","a-deva/halant-deva/") + '  '
	# Halform
	elif thisGlyph.script == 'devanagari' and thisGlyph.category =='Letter' and thisGlyph.subCategory =='Halfform':
		outputString += '/' + thisGlyph.name.replace("-","a-deva/halant-") + '  '
	# Others
	else:
		outputString += '/' + thisGlyph.name + '  '

# print outputString

Glyphs.currentDocument.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", outputString, True )