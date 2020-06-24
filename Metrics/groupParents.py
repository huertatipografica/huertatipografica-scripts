# MenuTitle: Group parents
# -*- coding: utf-8 -*-
import GlyphsApp
__doc__ = """
Goes through the kerning groups of the selected glyphs. Then opens a new tab with all the posible combinations so you can focus only in what you need to kern.
"""


thisFont = Glyphs.font  # frontmost font
selectedLayers = thisFont.selectedLayers  # active layers of selected glyphs
thisFontMaster = thisFont.selectedFontMaster  # active master

Glyphs.clearLog()


def char(name):
    if thisFont[name] is None:
        print "%s not found in font." % (name)
        return("", None)

    category = thisFont[name].category
    subCategory = thisFont[name].subCategory
    script = thisFont[name].script

    return (
        "%s%s%s%s" % (category, subCategory, script, name),
        name,
    )


def keyList(selectedLayers):
    keys = set([l.parent.leftKerningGroup for l in selectedLayers if l.parent.leftKerningGroup] +
               [l.parent.rightKerningGroup for l in selectedLayers if l.parent.rightKerningGroup])
    keys = sorted(map(char, keys))
    return filter(lambda x: x, [k[1] for k in keys])


keys = keyList(selectedLayers)
tabString = 'KerningGroups parents:\n%s\n\n' % ("/" + "/".join(keys))


if len(keys):
    thisFont.newTab(tabString)
else:
    Message("No kerning groups set :|", '', OKButton="OK")
