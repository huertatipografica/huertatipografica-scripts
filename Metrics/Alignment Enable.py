# MenuTitle: Alignment: enable
# -*- coding: utf-8 -*-
__doc__ = """
Enable automatic alignment for all components in all selected glyphs. Hold down SHIFT to do it on all layers.
"""

import GlyphsApp
from AppKit import NSEvent, NSShiftKeyMask

Font = Glyphs.font
selectedLayers = Font.selectedLayers

Glyphs.clearLog()


def process(thisLayer):
    for thisComp in thisLayer.components:
        thisComp.automaticAlignment = True

    print("Enabled automatic alignment in", thisLayer.parent.name)

keysPressed = NSEvent.modifierFlags()
shiftKeyPressed = keysPressed & NSShiftKeyMask == NSShiftKeyMask

for thisLayer in selectedLayers:
    thisGlyph = thisLayer.parent

    thisGlyph.beginUndo()
    if shiftKeyPressed:
        for thisLayer in thisGlyph.layers:
            if thisLayer.isSpecialLayer or thisLayer.isMasterLayer:
                process(thisLayer)
    else:
        process(thisLayer)

    thisGlyph.endUndo()
