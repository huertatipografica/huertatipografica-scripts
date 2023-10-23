# MenuTitle: Compare widths with next font
# -*- coding: utf-8 -*-
__doc__ = """
Opens a new tab comparing the widths of current master with the next font corresponding one. The list is sorted starting by the bigger difference. Hold SHIFT to only measure glyphs with outlines
"""

from AppKit import NSEvent, NSShiftKeyMask

Font = Glyphs.font
selectedLayers = Font.selectedLayers
Doc = Glyphs.currentDocument


def main():
    threshold = 10

    if len(Glyphs.fonts) < 2:
        Glyphs.showNotification(
            "No enough fonts", "You need 2 fonts open to make this comparison"
        )

        return

    font1 = Glyphs.fonts[0]
    font2 = Glyphs.fonts[1]

    current_master_index = Font.masters.index(Font.selectedFontMaster)

    master1 = font1.masters[current_master_index]
    master2 = font2.masters[current_master_index]

    keysPressed = NSEvent.modifierFlags()
    shiftKeyPressed = keysPressed & NSShiftKeyMask == NSShiftKeyMask

    comparison = []

    for glyph in font1.glyphs:
        layer1 = glyph.layers[master1.id]

        if shiftKeyPressed and not len(layer1.paths):
            continue

        if not font2[glyph.name]:
            continue

        layer2 = font2[glyph.name].layers[master2.id]
        comparison.append([abs(layer1.width - layer2.width), glyph.name])

    sorted_list = [
        res[1] for res in sorted(comparison, reverse=True) if res[0] > threshold
    ]

    Font.newTab(
        f"{font1.familyName} {master1.name} VS \n{font2.familyName} {master2.name} \n(Master {current_master_index+1}) characters sorted by width diff: \n\n"
        + "/"
        + "/".join(sorted_list)
    )


main()
