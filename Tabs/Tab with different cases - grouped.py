# MenuTitle: Tab with different cases (grouped)
# -*- coding: utf-8 -*-
__doc__ = """
Opens a new edit tab with current glyphs in both cases —and small caps (configurable).
"""

import GlyphsApp

thisFont = Glyphs.font  # frontmost font
thisFontMaster = thisFont.selectedFontMaster  # active master
listOfSelectedLayers = thisFont.selectedLayers  # active layers of selected glyphs


# Config
sc = True  # If you wanna include smallcaps

upper = []
lower = []
sc = []

for layer in listOfSelectedLayers:
    if hasattr(layer.parent, "name"):
        name = layer.parent.name.replace(".sc", "")
        name = name[0].lower() + name[1:]

        # Uppercase
        upper.append(name[0].upper() + name[1:])
        # Small Caps
        if sc:
            sc.append(name.lower() + ".sc")
        # Lower
        lower.append(name.lower())

glyphList = upper + ["\n"] + lower + ["\n"] + sc
tabString = "/" + "/".join(glyphList)

thisFont.newTab(tabString)
