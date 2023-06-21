# MenuTitle: OpenType Helper
# -*- coding: utf-8 -*-
__doc__ = """
Helps to generate OpenType replacements finding the coincidences based on given suffix.
"""
import GlyphsApp
import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

glyphList = [g.name for g in Font.glyphs]


class OpenTab(object):
    def __init__(self):
        self.tabString = ""

        self.w = vanilla.FloatingWindow(
            (360, 80), "OTHelper", autosaveName="com.juandelperal.OTHelper.mainwindow"
        )
        self.w.text = vanilla.TextBox(
            (13, 15, 320, 20), "suffix to find (ex sc)", sizeStyle="small"
        )
        self.w.suffix = vanilla.EditText(
            (15, 35, 200, 20),
            "H",
            sizeStyle="small",
            placeholder="ss01",
            callback=self.SavePreferences,
        )
        self.w.go = vanilla.Button(
            (220, 30, 60, 30), "Go", sizeStyle="small", callback=self.GoForIt
        )
        self.w.cancel = vanilla.Button(
            (285, 30, 60, 30), "Close", sizeStyle="small", callback=self.Close
        )

        self.w.setDefaultButton(self.w.go)

        if not self.LoadPreferences():
            print("Error: Could not load preferences. Will resort to defaults.")

        self.w.open()
        self.w.makeKey()

    def SavePreferences(self, sender):
        Glyphs.defaults[
            "com.juandelperal.OTHelper.mainwindow.suffix"
        ] = self.w.suffix.get()

        return True

    def LoadPreferences(self):
        try:
            self.w.suffix.set(
                Glyphs.defaults["com.juandelperal.OTHelper.mainwindow.suffix"]
            )
        except:
            return False

        return True

    def GoForIt(self, sender):
        Glyphs.clearLog()
        Glyphs.showMacroWindow()
        self.w.close()

        suffix = self.w.suffix.get()
        targetGlyphs = [g for g in glyphList if "." + suffix in g]

        for glyph in targetGlyphs:
            replacement = glyph.replace("." + suffix, "")
            if replacement in glyphList:
                print("sub %s by %s;" % (replacement, glyph))

    def Close(self, sender):
        self.w.close()


OpenTab()
