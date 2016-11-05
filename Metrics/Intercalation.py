#MenuTitle: Intercalation
# -*- coding: utf-8 -*-
__doc__="""
Combine selected glyphs in a new Tab with the string that you choose. Needs Vanilla.
"""
import GlyphsApp
import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

class OpenTab(object):

	def __init__(self):
		self.tabString = ''

		self.w = vanilla.FloatingWindow( (360, 80), "Intercalation", autosaveName="com.juandelperal.Intercalation.mainwindow" )
		self.w.text = vanilla.TextBox( (13, 15, 320, 20), "Slashed string to intercal with selected glyphs (ex. /n/o)", sizeStyle='small')
		self.w.interString = vanilla.EditText( (15, 35, 200, 20), "H", sizeStyle='small', placeholder='/n/n/n', callback=self.SavePreferences )
		self.w.go = vanilla.Button( (220, 30, 60, 30), "Go", sizeStyle='small', callback=self.Intercal )
		self.w.cancel = vanilla.Button( (285, 30, 60, 30), "Close", sizeStyle='small', callback=self.Close )

		self.w.setDefaultButton( self.w.go )

		if not self.LoadPreferences( ):
			print "Error: Could not load preferences. Will resort to defaults."

		self.w.open()
		self.w.makeKey()


	def SavePreferences( self, sender ):
		Glyphs.defaults["com.juandelperal.Intercalation.mainwindow.interString"] = self.w.interString.get()

		return True

	def LoadPreferences( self ):
		try:
			self.w.interString.set( Glyphs.defaults["com.juandelperal.Intercalation.mainwindow.interString"] )
		except:
			return False

		return True

	def Intercal(self, sender):
		interString = self.w.interString.get()
		for thisLayer in selectedLayers:
			thisGlyphName = thisLayer.parent.name
			self.tabString += "/%s%s" % (thisGlyphName, interString)

		Font.newTab(self.tabString)
		self.w.close()

	def Close(self, sender):
		self.w.close()

OpenTab()