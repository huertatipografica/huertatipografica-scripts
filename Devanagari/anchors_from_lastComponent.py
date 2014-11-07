#MenuTitle: Anchors from last component
# -*- coding: utf-8 -*-
__doc__="""
Copy all the anchors contained in the last component that has the selected glyph. Useful for devanagari conjunts.
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
FontMaster = Font.selectedFontMaster
selectedLayers = Font.selectedLayers

try:
	Glyphs.clearLog()
	# Glyphs.showMacroWindow()
except:
	pass

for thisLayer in selectedLayers:
	# Reset array
	components = [ component for component in thisLayer.components if Font.glyphs[ component.componentName ].category == 'Letter']
	last = len(components) - 1

	if len(components) > 0:
		# select last component
		componentName = thisLayer.components[last].componentName
		componentOffset = thisLayer.components[last].position.x

		# select glyph referenced on last component
		componentLayer = Font.glyphs[ componentName ].layers[ FontMaster.id ]
		
		print thisLayer.parent.name.upper()
		# Copy all anchors
		for anchor in componentLayer.anchors:
			
			thisAnchorPosition = NSPoint()
			thisAnchorPosition.x = anchor.x + componentOffset
			thisAnchorPosition.y = anchor.y

			thisAnchorName = anchor.name

			thisAnchor = GSAnchor( thisAnchorName, thisAnchorPosition )
			thisLayer.addAnchor_( thisAnchor )

			print "-- Added %s (%i, %i) from %s" % (thisAnchorName, thisAnchorPosition.x, thisAnchorPosition.y , componentName)