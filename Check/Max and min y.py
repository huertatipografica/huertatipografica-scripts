#MenuTitle: Max/Min y in selected
import GlyphsApp

Doc = Glyphs.currentDocument
font = Glyphs.font
selectedLayers = Font.selectedLayers

def layerIndex(font,layer):
	actualId=layer.layerId
	for i in range(len(font.masters)):
		if actualId==font.masters[i].id:
			index=i
	return index

top=[0,None]
bottom=[0,None]
for layer in selectedLayers:
	yorigin=layer.bounds[0][1]
	height=layer.bounds[1][1]
	ytop=yorigin+height
	if ytop>top[0] and '.comb' not in layer.parent.name:
		top=[ytop,layer.parent.name]
	if yorigin<bottom[0]:
		bottom=[yorigin,layer.parent.name]

print "-Highest glyph: %s (%.1f)" % (top[1], top[0])
print "-Lowest glyph: %s (%.1f)" % (bottom[1], bottom[0])
print "-BBox: (%.1f)" % (top[0] + bottom[0] * -1)