# MenuTitle: Missing kerning groups references
# -*- coding: utf-8 -*-
import GlyphsApp

__doc__ = """
Goes through the kerning groups and metric keys of the selected glyphs and check that the refences are present in font.
"""


thisFont = Glyphs.font  # frontmost font
selectedLayers = thisFont.selectedLayers  # active layers of selected glyphs
thisFontMaster = thisFont.selectedFontMaster  # active master


def missing(name) -> bool:
    return not thisFont[name] if name else False


def check(selectedLayers):
    Glyphs.clearLog()
    missingList = {}
    for l in selectedLayers:

        if missing(l.parent.leftKerningGroup):
            print(
                f" - {l.parent.name} leftKerningGroup references unexistent {l.parent.leftKerningGroup}"
            )
            missingList[l.parent.name] = True

        if missing(l.parent.rightKerningGroup):
            print(
                f" - {l.parent.name} rightKerningGroup references unexistent {l.parent.rightKerningGroup}"
            )
            missingList[l.parent.name] = True

    return missingList


keys = check(selectedLayers)

if len(keys.keys()):
    tabString = "Glyphs with metric references to fix:\n%s\n\n" % (
        "/" + "/".join(keys.keys())
    )
    thisFont.newTab(tabString)
    Glyphs.showMacroWindow()
else:
    Message("No wrong metric references", "", OKButton="OK")
