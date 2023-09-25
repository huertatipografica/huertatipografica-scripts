# MenuTitle: Smart Slanter (wip)
# -*- coding: utf-8 -*-

from AppKit import NSAffineTransform, NSEvent, NSShiftKeyMask
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

    layer.applyTransform([1, myY / 2, myX, 1, 0, 0])
    layer.anchors = []
    # layer.background.paths = []

    return layer


def rotate(layer, angle):
    transformation = NSAffineTransform()
    transformation.rotate(angle * -1)
    layer.transform(transformation)

    # myTransform = NSAffineTransform.transform()
    # myTransform.rotateByDegrees_(angle*-1)
    # layer.applyTransform(myTransform.transformStruct())
    layer.anchors = []
    layer.background = None

    return layer


def slant(layer, angle, cursify):
    layer.slantX_Origin_doCorrection_(angle, (0, thisMaster.xHeight * 0.5), cursify)
    return layer


def process(layer):

    angle = layer.master.italicAngle

    # slanted layer
    slanted = layer.copy()
    slant(slanted, angle, False)
    slanted.name = "slanted"
    thisFont.glyphs[layer.parent.name].layers.append(slanted)

    # roundSlanted layer
    roundSlanted = layer.copy()
    roundSlanted.name = "roundSlanted"
    jacquesSlanting(roundSlanted, angle)
    thisFont.glyphs[layer.parent.name].layers.append(roundSlanted)

    # rotated layer
    rotated = layer.copy()
    rotated.name = "rotated"
    rotate(rotated, angle)
    thisFont.glyphs[layer.parent.name].layers.append(rotated)

    # Replacing MAIN layers
    layer.setBackground_(layer)
    slant(layer, angle, False)
    slant(layer.background, angle, True)

    # cursified layer
    cursified = layer.copy()
    # cursified.paths = layer.background.paths
    cursified.name = "cursified"
    thisFont.glyphs[layer.parent.name].layers.append(cursified)

    # move back:
    oldPos = layer.bounds.origin

    roundSlantedPos = roundSlanted.bounds.origin
    xRoundSlantedShiftBack = oldPos.x - roundSlantedPos.x
    yRoundSlantedShiftBack = oldPos.y - roundSlantedPos.y
    roundSlanted.applyTransform(
        [1, 0, 0, 1, xRoundSlantedShiftBack, yRoundSlantedShiftBack]
    )

    rotatedPos = rotated.bounds.origin
    xrotatedShiftBack = oldPos.x - rotatedPos.x
    yrotatedShiftBack = oldPos.y - rotatedPos.y
    rotated.applyTransform([1, 0, 0, 1, xrotatedShiftBack, yrotatedShiftBack])


if thisMaster.italicAngle == 0:
    Message(
        "Set a Italic Angle",
        "Italic Angle in current Master should be different than zero",
    )

else:
    keysPressed = NSEvent.modifierFlags()
    shiftKeyPressed = keysPressed & NSShiftKeyMask == NSShiftKeyMask

    # Do the thing
    thisFont.disableUpdateInterface()

    for thisLayer in selectedLayers:
        thisGlyph = thisLayer.parent

        thisGlyph.beginUndo()
        if shiftKeyPressed:
            for thisLayer in thisGlyph.layers:
                if thisLayer.isMasterLayer:
                    process(thisLayer)
        else:
            process(thisLayer)

        thisGlyph.endUndo()

    thisFont.enableUpdateInterface()
