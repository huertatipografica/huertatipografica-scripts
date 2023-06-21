# MenuTitle: Tab with dangerous interpolation glyphs
# -*- coding: utf-8 -*-
__doc__ = """
Opens a new tab with glyphs that may produce funny interpolations. Useful for compatible glyphs
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

# Create array
glyphList = []

# Functions for checking
def hasRepeatedPaths(thisLayer):
    items = []
    for thisPath in thisLayer.paths:
        items.append(len(thisPath.nodes))
    if len(items) != len(set(items)):
        return True
    return False


def hasRepeatedComponents(thisLayer):
    items = []
    for thisComponent in thisLayer.components:
        items.append(thisComponent.componentName)
    if len(items) != len(set(items)):
        return True
    return False


# Run the script
for thisLayer in selectedLayers:
    if (
        hasRepeatedPaths(thisLayer)
        or hasRepeatedComponents(thisLayer)
        or not thisLayer.parent.mastersCompatible
    ):
        glyphList.append(thisLayer.parent.name)

if glyphList:
    tabString = "/" + "/".join(glyphList)
    Font.newTab(tabString)
else:
    Message(
        "No dangerous glyphs",
        "There are not repeated components, paths with the same ammount of points or incompatible glyphs in current selection.",
        OKButton="Yeah",
    )
