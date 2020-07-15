def process(thisGlyph, reset=False):
    thisGlyph.beginUndo()
    for layer in thisGlyph.layers:
        if reset:
            layer.anchors = []

        layer.addMissingAnchors()

    thisGlyph.endUndo()
