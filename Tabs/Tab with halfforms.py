# MenuTitle: Tab with Deva-Halfforms
import GlyphsApp
from PyObjCTools.AppHelper import callAfter

font = Glyphs.font
layers = Glyphs.currentDocument.selectedLayers()
layer = layers[0]
glyphname = layer.parent.name
outputString = "/" + glyphname + "/space/" + glyphname + "/aaMatra-deva"
for thisGlyph in font.glyphs:
    if (
        thisGlyph.script == "devanagari"
        and thisGlyph.category == "Letter"
        and thisGlyph.subCategory == "Halfform"
    ):
        outputString += "/" + glyphname + "/" + thisGlyph.name + "/space"


callAfter(Glyphs.currentDocument.windowController().addTabWithString_, outputString)
print(outputString)
print("Fin")
