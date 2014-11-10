#MenuTitle: Check different anchors in masters
__doc__="""
Check if the anchors are different in masters
"""
font=Glyphs.font
masters=Glyphs.font.masters
selectedLayers = Glyphs.currentDocument.selectedLayers()

output=''


Glyphs.clearLog()


def anchors(selectedLayers,masters,font):
	mNum=len(masters)
	layersids=range(mNum)
	output='Sin problemas.'
	
	for layer in selectedLayers:
		g=layer.parent
		anchors=[]
		for id in layersids:
			anchors.append(len(g.layers[id].anchors))
		if max(anchors)!=min(anchors):
			output=''
			g.color=1
			for id in layersids:
				output+=g.name+"\n"+str(g.layers[id].anchors)+"\n"
	return output

print anchors(selectedLayers,masters,font)

	

