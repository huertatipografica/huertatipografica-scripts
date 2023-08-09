# MenuTitle: Alignment: enable except for last base letter's component
# -*- coding: utf-8 -*-
__doc__ = """
Automatically align all components in the selected glyphs, except for the last letter. Useful for characters such as Ꞓ, ꞓ, Ħ, ħ, ł. Component positions remain linked while still allowing editable metrics. Hold down SHIFT to do it on all layers.
"""

import GlyphsApp
from AppKit import NSEvent, NSShiftKeyMask

Font = Glyphs.font
selectedLayers = Font.selectedLayers

Glyphs.clearLog()


def process(thisLayer):
    base_chars = [
        comp.componentName
        for comp in thisLayer.components
        if Font.glyphs[comp.componentName].category == "Letter"
    ]
    disabled_aligned_char = next(reversed(base_chars), None)

    for comp in thisLayer.components:
        comp.automaticAlignment = comp.componentName != disabled_aligned_char

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
