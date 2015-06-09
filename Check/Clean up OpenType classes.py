#MenuTitle: Clean up OpenType classes
# -*- coding: utf-8 -*-
__doc__="""
Delete all inexistent glyphs from OpenType classes.
"""

import GlyphsApp
Font = Glyphs.font
Classes = Font.classes

for thisclase in Classes:
	code = ''
	content = thisclase.code.split()
	amount = str(len(content)) # original amount of members
	for glyph in content:
		if Font.glyphs[glyph]: # check is glyph exists
			code += glyph + ' '

	newAmount = str(len(code.split())) # new amount of members
	if amount != newAmount:
		thisclase.code = code
		print thisclase.name + ': from ' + amount + " to " + newAmount