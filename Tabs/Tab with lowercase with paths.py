#MenuTitle: Tab with lowercase with paths
# -*- coding: utf-8 -*-

import GlyphsApp

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers

# Scope glyphs for combine
targetGlyphs = [g.name for g in thisFont.glyphs if g.subCategory == 'Lowercase' and len(g.layers[0].paths) > 1]

lista = []
def process (thisLayer):
	for g in targetGlyphs:
		lista.append(thisLayer.parent.name)
		lista.append(g)
	lista.append(thisLayer.parent.name)
	lista.append("\n")

for thisLayer in selectedLayers:
	process (thisLayer)

tabString =  "/%s" % "/".join(lista)
thisFont.newTab( tabString )
