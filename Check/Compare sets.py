# MenuTitle: Compare Sets
# -*- coding: utf-8 -*-
__doc__ = """
Compare character sets between fonts. Thanks Guido Ferreyra
"""

from GlyphsApp import *


class ListDiff(object):
    if len(Glyphs.fonts) < 2:
        Message("Please open two files to compare sets", "Not enought fonts")
        stop()

    font1 = Glyphs.fonts[0]
    font2 = Glyphs.fonts[1]
    styleName1 = font1.instances[0].name
    styleName2 = font2.instances[0].name

    lista1 = []
    lista2 = []

    # Create lists with the name of the glyphs of each font
    for a in font1.glyphs:
        lista1.append(a.name)  # A, B, C, D, etc.
    for a in font2.glyphs:
        lista2.append(a.name)
    # Create sets of the lists for later comparision.
    font1Set = set(lista1)
    font2Set = set(lista2)
    # Create new sets with the differences.
    OneDiff = font1Set.difference(font2Set)
    TwoDiff = font2Set.difference(font1Set)
    # Transorm the sets in list again to send it to the UI
    lista1 = list(OneDiff)
    lista2 = list(TwoDiff)

    Glyphs.clearLog()

    print("Missing on %s %s:" % (font2.familyName, styleName2))
    print("")
    for name in lista1:
        print(name)
    print("")
    print("")

    print("Missing on %s %s:" % (font1.familyName, styleName1))
    print("")
    for name in lista2:
        print(name)
    print("")
    print("")

    Glyphs.showMacroWindow()


ListDiff()
