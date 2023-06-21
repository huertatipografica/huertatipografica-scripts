# MenuTitle: Adjust headstroke
__doc__ = """
Re arrange headstroke nodes in selected glyphs. You need to declare a headstroke glyph for y coordinates reference
"""
# -*- coding: utf-8 -*-

import GlyphsApp

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers

excedente = 30  # distance from sidebearings
halfspace = 10  # dont worry

# headstroke reference
techo = Font.glyphs["devaTecho"]


def getCenter(selection):
    izq = min((n.x for n in selection))
    der = max((n.x for n in selection))
    centro = round((der + izq) / 2)
    return centro


def getSides(selection):
    rangex = 70
    izq = []
    der = []
    centro = getCenter(selection)
    for thisNode in selection:
        if thisNode.x < centro - rangex:
            izq.append(thisNode)
        if thisNode.x > centro + rangex:
            der.append(thisNode)
    return izq, der


def nodesListRange(layer, min, max):
    nodes = []
    for path in layer.paths:
        for node in path.nodes:
            if node.y >= min < (min + 1) and node.y <= max > (max - 1):
                nodes.append(node)
    return nodes


def layerid(layer):
    actualId = layer.layerId
    i = 0
    for l in layer.parent.layers:
        if actualId == l.layerId:
            id = i
        i = i + 1
    return id


def detectRange(layer):
    n = layerid(layer)
    layer = techo.layers[n]
    box = layer.bounds
    return box[0].y, box[0].y + box[1][1]


if techo:
    Font.disableUpdateInterface()
    for layer in selectedLayers:
        rango = detectRange(layer)
        nodes = nodesListRange(layer, rango[0], rango[1])
        if len(nodes) > 2:
            lados = getSides(nodes)
            width = layer.width
            offsetL = min((n.x for n in lados[0]))
            offsetR = width - (max((n.x for n in lados[1])))
            for nodo in lados[0]:
                if nodo.x < 70:
                    if layer.parent.leftMetricsKey == "halfspace":
                        nodo.x -= offsetL + halfspace
                    else:
                        nodo.x -= offsetL + excedente
            for nodo in lados[1]:
                if nodo.x > (width - 70):
                    if layer.parent.rightMetricsKey == "halfspace":
                        nodo.x += offsetR + halfspace
                    else:
                        nodo.x += offsetR + excedente

            # layer.parent.color=0

    Font.enableUpdateInterface()
else:
    print("Debe crear primero un glifo de referencia para el techo.")
