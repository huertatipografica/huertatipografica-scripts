# MenuTitle: Tab with different cases
# -*- coding: utf-8 -*-
__doc__ = """
Opens a new edit tab with current glyphs in both cases —and small caps (configurable).
"""

import GlyphsApp

thisFont = Glyphs.font  # frontmost font
thisFontMaster = thisFont.selectedFontMaster  # active master
listOfSelectedLayers = thisFont.selectedLayers  # active layers of selected glyphs


# Config
separator = "space"  # Setup separator if you want, for example 'space'
sc = True  # If you wanna include smallcaps

glyphList = []

for layer in listOfSelectedLayers:
    if hasattr(layer.parent, "name"):
        name = layer.parent.name.replace(".sc", "")
        name = name.replace(".smcp", "")
        segments = name.split(".")

        segment = segments[0]
        lc = segment[0].lower() + segments[0][1:]
        uc = segment[0].upper() + segments[0][1:]
        all_uc = segment.upper()

        # Uppercase
        segments[0] = uc
        glyphList.append(".".join(segments))

        if all_uc != uc:
            segments[0] = all_uc
            glyphList.append(".".join(segments))

        segments[0] = lc

        # Small Caps
        if sc:
            glyphList.append(".".join(segments) + ".sc")
        # Lower
        glyphList.append(".".join(segments))

        # Separator
        if separator:
            glyphList.append(separator)
    else:
        glyphList.append("\n")

# glyphList = set(glyphList)
tabString = "/" + "/".join(glyphList)
thisFont.newTab(tabString)
