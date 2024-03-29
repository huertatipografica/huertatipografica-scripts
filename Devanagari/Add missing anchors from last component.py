# MenuTitle: Add missing anchors from last component
# -*- coding: utf-8 -*-
__doc__ = """
Copy the missing the anchors contained in the last component that has the selected glyph
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
    # components = [ component for component in thisLayer.components if Font.glyphs[ component.componentName ].category == 'Letter']
    components = [component for component in thisLayer.components]
    anchors = [anchor.name for anchor in thisLayer.anchors]
    last = len(components) - 1

    if len(components) > 0:
        # select last component
        componentName = thisLayer.components[last].componentName
        componentOffsetX = thisLayer.components[last].position.x
        componentOffsetY = thisLayer.components[last].position.y

        # select glyph referenced on last component
        componentLayer = Font.glyphs[componentName].layers[FontMaster.id]

        print(thisLayer.parent.name.upper())
        # Copy all anchors
        for anchor in componentLayer.anchors:

            thisAnchorPosition = NSPoint()
            thisAnchorPosition.x = anchor.x + componentOffsetX
            thisAnchorPosition.y = anchor.y + componentOffsetY

            thisAnchorName = anchor.name
            thisAnchor = GSAnchor(thisAnchorName, thisAnchorPosition)

            if thisAnchorName not in anchors:
                thisLayer.addAnchor_(thisAnchor)
                print(
                    "-- Added %s (%i, %i) from %s"
                    % (
                        thisAnchorName,
                        thisAnchorPosition.x,
                        thisAnchorPosition.y,
                        componentName,
                    )
                )
            else:
                print(thisAnchorName, "already exists in this layer")
