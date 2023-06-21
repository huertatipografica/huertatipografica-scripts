# MenuTitle: Copy kerning classes from caps to smcp
# -*- coding: utf-8 -*-
__doc__ = """
Mostly Stolen from mekkablue, but works in a different direction.
Goes through all selected .sc glyphs,
checks if there is a corresponding uppercase glyph,
and if so, copies the uppercase kerning classes to the .sc glyph.
WARNING: will override the actual class
"""

import GlyphsApp

Font = Glyphs.font
exceptionlist = ["Germandbls.c2sc"]
selectedSCs = [
    x.parent
    for x in Font.selectedLayers
    if x.parent.name.endswith(".sc") or x.parent.name.endswith(".smcp")
]


def uppercaser(name):
    """Turns 'aacute.sc' into 'Aacute'."""
    name = name[0].upper() + name[1:]
    return name.split(".")[0]


def process(thisGlyph):
    ucName = uppercaser(thisGlyph.name)

    # Check if the smcpGlyph exists
    if Font.glyphs[ucName] != None:
        ucGlyph = Font.glyphs[ucName]
        thisGlyph.leftKerningGroup = ucGlyph.leftKerningGroup
        thisGlyph.rightKerningGroup = ucGlyph.rightKerningGroup
        print("Processing %s <<< %s." % (thisGlyph.name, ucGlyph.name))
    else:
        print("%s: no %s in font." % (thisGlyph.name, ucName))


Font.disableUpdateInterface()

for thisGlyph in selectedSCs:
    # print ucName(thisGlyph.name)
    if thisGlyph.name not in exceptionlist:
        process(thisGlyph)

Font.enableUpdateInterface()
