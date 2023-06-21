# MenuTitle: Check components in font
__doc__ = """
Check existence and order of components in masters
"""
selectedLayers = Glyphs.currentDocument.selectedLayers()
font = Glyphs.font
masters = Glyphs.font.masters
mnum = len(masters)
compList = []
lista = []
for item in font.glyphs:
    # print(item.parent.name)
    layers = item.layers
    comp = []
    if len(layers[0].components) != len(layers[1].components):
        print("Different components in " + item.name)
    elif len(layers[0].components) > 1:
        for component in layers[0].components:
            comp.append(component.componentName)
        for index in range(mnum):
            layer = layers[index]
            for cindex in range(len(layer.components)):
                # 			print(comp[cindex],layer.components[cindex].componentName)
                if comp[cindex] != layer.components[cindex].componentName:
                    lista.append(item.name)

for item in lista:
    print("Diferent component order in " + item)
