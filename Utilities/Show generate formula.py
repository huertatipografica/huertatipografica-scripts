# MenuTitle: Show generate formula
# -*- coding: utf-8 -*-
__doc__ = """
Output in scripts panel the formula for generating the selected glyphs. Only for components based characters
"""

import GlyphsApp

thisFont = Glyphs.font  # frontmost font
listOfSelectedLayers = thisFont.selectedLayers  # active layers of selected glyphs

Glyphs.clearLog()
Glyphs.showMacroWindow()

withPaths = []


def process(thisLayer):
    # component names
    components = [c.componentName for c in thisLayer.components]

    if len(thisLayer.paths) > 0:
        withPaths.append(thisLayer.parent.name)
    else:
        if len(components):
            # print generating formula
            print("%s=%s" % ("+".join(components), thisLayer.parent.name))
        else:
            print(thisLayer.parent.name)


thisFont.disableUpdateInterface()  # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
    process(thisLayer)

if withPaths:
    print("\n\n---------\nWarning: %s have paths" % (", ".join(withPaths)))

thisFont.enableUpdateInterface()  # re-enables UI updates in Font View
