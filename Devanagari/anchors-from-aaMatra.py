#MenuTitle: Anchors from aaMatra
font=Glyphs.font
masters=Glyphs.font.masters
selectedLayers = Glyphs.currentDocument.selectedLayers()

output=''

def isComponent(components,name):
	for component in components:
		if component.componentName == name:
			return True
			break
	
def setAnchorPos(layer,anchor_name):
	for anchor in layer.anchors:
		if anchor.name == anchor_name:
			anchor.x=layer.width-getAnchorPos(layer,'aaMatra-deva',anchor_name)
			
def getAnchorPos(layer,glyph,anchor_name):
	id=layerid(layer)
	for anchor in font.glyphs[glyph].layers[id].anchors:
		if anchor.name == anchor_name:
			return font.glyphs[glyph].layers[id].width-anchor.x

def layerid(layer):
	actualId=layer.layerId
	i=0
	for l in layer.parent.layers:
		if actualId == l.layerId:
			id=i
		i=i+1
	return id
	

def anchors(selectedLayers,masters,font):
	
	for layer in selectedLayers:
		g=layer.parent
		components=layer.components
		#if isComponent(components,'aaMatra-deva') or layer.parent.rightMetricsKey=='aaMatra-deva':
		#print layer.parent.rightMetricsKey
		setAnchorPos(layer,'top')
		setAnchorPos(layer,'bottom')
		

anchors(selectedLayers,masters,font)

	

