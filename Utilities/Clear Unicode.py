#MenuTitle: Clear Unicode
# -*- coding: utf-8 -*-
__doc__="""
Clear unicode values. WARNING!
"""

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]


def process( thisGlyph ):
	thisGlyph.setUnicode_('')

# Run
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process( thisGlyph )

Font.enableUpdateInterface()