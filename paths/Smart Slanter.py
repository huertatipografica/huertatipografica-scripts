# MenuTitle: Smart Slanter
# -*- coding: utf-8 -*-

from math import radians
__doc__ = """
A slanting workflow that do many things:
- slant the foreground,
- cursify the background,
- and adds a "slanted" layer,
- and adds a "cursified" layer,
- and adds a "roundSlanted" layer with the glyph slanted with vertical compensation (based in Jacques Le Bailly method and Alexei Vanyashin script).

It takes the italicAngle declared in the Master as reference.
"""

thisFont = Glyphs.font  # frontmost font
selectedLayers = thisFont.selectedLayers  # active layers of selected glyphs
thisMaster = thisFont.selectedFontMaster


def jacquesSlanting(layer, angle):
    myX = radians(angle)  # horizontal skew = italic angle
    myY = -radians(angle)  # vertical skew = -0.5 * italic angle

    layer.applyTransform([1, myY/2, myX, 1, 0, 0])
    layer.anchors = []
    layer.background.paths = []

    return layer


def slant(layer, angle, cursified=False):
    layer.slant_Origin_doCorrection_(
        angle, (0, thisMaster.xHeight * 0.5), cursified)
    return layer


def process(layer):
    angle = layer.master.italicAngle

    # Replacing MAIN layers
    layer.setBackground_(layer)
    slant(layer, angle, False)
    slant(layer.background, angle, True)

    # slanted layer
    slanted = layer.copy()
    slanted.name = 'slanted'
    slant(slanted, angle, False)
    thisFont.glyphs[layer.parent.name].layers.append(slanted)

    # roundSlanted layer
    cursified = layer.copy()
    cursified.name = 'cursified'
    slant(cursified, angle, True)
    thisFont.glyphs[layer.parent.name].layers.append(cursified)

    # roundSlanted layer
    roundSlanted = layer.copy()
    roundSlanted.name = 'roundSlanted'
    jacquesSlanting(roundSlanted, angle)
    thisFont.glyphs[layer.parent.name].layers.append(roundSlanted)


    # move back:
    oldPos = layer.bounds.origin
    newPos = roundSlanted.bounds.origin
    xShiftBack = oldPos.x-newPos.x
    yShiftBack = oldPos.y-newPos.y
    roundSlanted.applyTransform([1, 0, 0, 1, xShiftBack, yShiftBack])


if(thisMaster.italicAngle == 0):
    Message(
        "Set a Italic Angle",
        "Italic Angle in current Master should be different than zero"
    )

else:
    # Do the thing
    thisFont.disableUpdateInterface()
    for layer in selectedLayers:
        layer.parent.beginUndo()

        process(layer)
        layer.parent.endUndo()

    thisFont.enableUpdateInterface()
