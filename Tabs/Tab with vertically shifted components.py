# MenuTitle: Tab with vertically shifted components
# -*- coding: utf-8 -*-

thisFont = Glyphs.font  # frontmost font
thisFontMaster = thisFont.selectedFontMaster  # active master
listOfSelectedLayers = thisFont.selectedLayers  # active layers of selected glyphs

glyphList = []

for layer in listOfSelectedLayers:
    if hasattr(layer.parent, "name"):
        components = [
            component for component in layer.components if component.position.y != 0.0
        ]
        if len(components):
            glyphList.append(layer.parent.name)


if len(glyphList):
    tabString = "/" + "/".join(glyphList)
    thisFont.newTab(tabString)
else:
    Message("Everything ok", "Not vertically shifted components")
