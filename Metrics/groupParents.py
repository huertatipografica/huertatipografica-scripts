# MenuTitle: Group parents
# -*- coding: utf-8 -*-
import GlyphsApp

__doc__ = """
Goes through the kerning groups of the selected glyphs. Then opens a new tab with all the group parents so you can check kerning groups.
"""


thisFont = Glyphs.font  # frontmost font
selectedLayers = thisFont.selectedLayers  # active layers of selected glyphs
thisFontMaster = thisFont.selectedFontMaster  # active master

Glyphs.clearLog()


def char(name):
    character = thisFont[name]
    if character is None:
        print(f"{name} not found in font.")
        return ("", None)

    layer = character.layers[0]
    order_key = f"{character.category}-{character.subCategory}-{character.case}-{character.script}-{layer.LSB}-{name}"

    return order_key, name


def keyList(selectedLayers):
    keys = set(
        [l.parent.leftKerningGroup for l in selectedLayers if l.parent.leftKerningGroup]
        + [
            l.parent.rightKerningGroup
            for l in selectedLayers
            if l.parent.rightKerningGroup
        ]
    )
    keys = sorted(map(char, keys))
    return [x for x in [k[1] for k in keys] if x]


keys = keyList(selectedLayers)
tabString = "KerningGroups parents:\n%s\n\n" % ("/" + "/".join(keys))


if len(keys):
    thisFont.newTab(tabString)
else:
    Message("No kerning groups set :|", "", OKButton="OK")
