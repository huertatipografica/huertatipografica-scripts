# MenuTitle: Tab with symmetric symbols
# -*- coding: utf-8 -*-

thisFont = Glyphs.font  # frontmost font
thisFontMaster = thisFont.selectedFontMaster  # active master
listOfSelectedLayers = thisFont.selectedLayers  # active layers of selected glyphs

symbols = [
    ("exclamdown", "exclam"),
    ("questiondown", "question"),
    ("quotedblleft", "quotedblright"),
    ("quoteleft", "quoteright"),
    ("guillemetleft", "guillemetright"),
    ("guilsinglleft", "guilsinglright"),
    ("guillemetleft.case", "guillemetright.case"),
    ("parenleft", "parenright"),
    ("braceleft", "braceright"),
    ("bracketleft", "bracketright"),
    ("parenleft.case", "parenright.case"),
    ("braceleft.case", "braceright.case"),
    ("bracketleft.case", "bracketright.case"),
]

tabString = ""

for before, after in symbols:
    if thisFont[before] and thisFont[after]:
        for layer in listOfSelectedLayers:
            if hasattr(layer.parent, 'name'):
                tabString += "/%s/%s/%s" \
                    % (before, layer.parent.name, after)
        tabString += "/%s\n\n" % layer.parent.name

if tabString:
    thisFont.newTab(tabString)
else:
    Message("Please open two files to compare sets", "Not enought fonts")
