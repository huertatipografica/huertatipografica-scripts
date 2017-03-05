#MenuTitle: Tab with broken components
# -*- coding: utf-8 -*-

import GlyphsApp

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers

glyphList = [g.name for g in thisFont.glyphs]

# Scope glyphs for combine
targetLayers = [g.layers[0] for g in thisFont.glyphs if len(g.layers[0].components)]

lista = []
components = []
missing = []

Glyphs.clearLog()

def process (thisLayer):
	for c in thisLayer.components:
		# Check missing comp
		if c.componentName not in glyphList :
			lista.append(thisLayer.parent.name)
			missing.append(c.componentName)
			break

		# Check empty component
		if len(thisFont.glyphs[c.componentName].layers[0].paths) < 1 and len(thisFont.glyphs[c.componentName].layers[0].components) < 1:
			lista.append(thisLayer.parent.name)
			components.append(c.componentName)
			break

# Process
for thisLayer in targetLayers:
	process (thisLayer)

if len(lista):
	tabString =  "/%s" % "/".join(lista)
	thisFont.newTab( tabString )
else :
	Glyphs.showMacroWindow()
	print "-- No missing components"

if len(components) :
	tabString2 =  "/%s" % "/".join(set(components))
	thisFont.newTab( tabString2 )
else :
	Glyphs.showMacroWindow()
	print "-- No empty components"


# If missing glyphs output
if len(missing):
	Glyphs.showMacroWindow()
	print "-- Missing glyphs:"
	for x in set(missing):
		print x