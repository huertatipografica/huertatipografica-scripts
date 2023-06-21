# MenuTitle: Lowest and highest glyphs
# -*- coding: utf-8 -*-
__doc__ = """
Reports and open a new tab with lowest and highest glyphs in selected layers. This is stolen from mekkablue :)
"""

import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers
Doc = Glyphs.currentDocument


# Config
limit = 20

print(f"{Font.familyName} (master: {Font.selectedFontMaster.name})")
print("Highest selected glyphs:")
outputString = "Highest:\n"


sortedNameHeightPairs = sorted(
    [[l.parent.name, l.bounds.origin.y + l.bounds.size.height] for l in selectedLayers],
    key=lambda x: -x[1],
)
for thisLayerPair in sortedNameHeightPairs[:limit]:
    print("- %s: %.1f" % (thisLayerPair[0], thisLayerPair[1]))
    outputString += f"/{thisLayerPair[0]}"

print("\nLowest selected glyphs:")
outputString += "\nLowest:\n"

sortedNameHeightLowestPairs = sorted(
    [[l.parent.name, l.bounds.origin.y] for l in selectedLayers], key=lambda x: x[1]
)
for thisLayerPair in sortedNameHeightLowestPairs[:limit]:
    print("- %s: %.1f" % (thisLayerPair[0], thisLayerPair[1]))
    outputString += f"/{thisLayerPair[0]}"

print(
    "\n\n- Height sum: %.1f"
    % (abs(sortedNameHeightPairs[0][1]) + abs(sortedNameHeightLowestPairs[0][1]))
)

Glyphs.clearLog()
Glyphs.showMacroWindow()

Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_(
    "addTabWithString:", outputString, True
)
