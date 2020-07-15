def process(thisGlyph):
    thisGlyph.beginUndo()
    for layer in thisGlyph.layers:
        for path in layer.paths:
            path.addNodesAtExtremes()

    thisGlyph.endUndo()
