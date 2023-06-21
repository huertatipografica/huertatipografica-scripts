# MenuTitle: Check different anchors in masters
__doc__ = """
Check if the anchors are different in masters, and if so, color-marks the glyph and reports in the macro window.
"""

selectedLayers = Glyphs.font.selectedLayers
Glyphs.clearLog()


def glyphReport(glyph):
    anchors = []
    for layer in glyph.layers:
        if layer.isSpecialLayer or layer.isMasterLayer:
            anchors.append(len(layer.anchors))

    numberOfAnchorsIsNotConsistent = max(anchors) != min(anchors)
    if numberOfAnchorsIsNotConsistent:
        output = ""
        glyph.color = 1
        output = "\n%s:\n" % glyph.name
        for layer in glyph.layers:
            if layer.isSpecialLayer or layer.isMasterLayer:
                output += "- %i anchors on layer '%s': %s\n" % (
                    len(layer.anchors),
                    layer.name,
                    ", ".join([a.name for a in layer.anchors]),
                )
        return output

    return None


def anchors(selectedLayers):
    output = ""
    for layer in selectedLayers:
        g = layer.parent
        glyphOutput = glyphReport(g)
        if glyphOutput:
            output += glyphOutput

    if not output:
        return "Sin problemas. No problems found."
    else:
        # brings macro window to front:
        Glyphs.showMacroWindow()
        return output


print(anchors(selectedLayers))
