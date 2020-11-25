# MenuTitle: Smart Slanter
# -*- coding: utf-8 -*-

from math import radians
__doc__ = """
A slanting workflow that do many things:
- slant the foreground,
- cursify the background,
- adds a "backup" layer with the current drawing,
- and adds a "roundSlanting" layer with the glyph slanted with vertical compensation (method by Jacques Le Bailly and a script from Alexei Vanyashin).

It takes the italicAngle declared in the Master as reference
"""

thisFont = Glyphs.font  # frontmost font
selectedLayers = thisFont.selectedLayers  # active layers of selected glyphs
thisMaster = thisFont.selectedFontMaster


def jacquesSlanting(layer, angle):
    myX = radians(angle)  # horizontal skew = italic angle
    myY = -radians(angle)  # vertical skew = -0.5 * italic angle

    # shear:
    oldPos = layer.bounds.origin
    layer.applyTransform([1, myY/2, myX, 1, 0, 0])

    # move back:
    newPos = layer.bounds.origin
    xShiftBack = oldPos.x-newPos.x
    yShiftBack = oldPos.y-newPos.y
    layer.applyTransform([1, 0, 0, 1, xShiftBack, yShiftBack])

    return layer


def slant(layer, angle, cursify=False):
    layer.slant_Origin_doCorrection_(
        angle, (0, thisMaster.xHeight * 0.5), cursify)
    return layer


def process(layer):
    angle = layer.master.italicAngle

    # Copy foreground to background
    layer.setBackground_(layer)

   # Backup layer
    backup = layer.copy()
    backup.name = 'backup'
    thisFont.glyphs[layer.parent.name].layers.append(backup)

    # roundSlanting layer
    roundSlanting = layer.copy()
    roundSlanting.name = 'roundSlanting'
    jacquesSlanting(roundSlanting, angle)
    thisFont.glyphs[layer.parent.name].layers.append(roundSlanting)

    # Slanting foreground, cursify background
    slant(layer, angle, False)
    slant(layer.background, angle, True)


if(thisMaster.italicAngle == 0):
    raise("Italic Angle should be different than zero. Set a Italic Angle in Font Master")

# Do the thing
thisFont.disableUpdateInterface()
for layer in selectedLayers:
    layer.parent.beginUndo()

    process(layer)
    layer.parent.endUndo()

thisFont.enableUpdateInterface()
