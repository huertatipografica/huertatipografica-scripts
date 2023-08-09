# MenuTitle: Alignment: enable except in last base letter's component
# -*- coding: utf-8 -*-
__doc__ = """
Enable automatic alignment for all components in all selected glyphs except for the last letter.
"""

import GlyphsApp

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


for thisLayer in selectedLayers:
    thisGlyph = thisLayer.parent

    thisGlyph.beginUndo()
    process(thisLayer)
    thisGlyph.endUndo()
