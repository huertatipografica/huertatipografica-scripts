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

outputString = ''

class OpenTab(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow( (360, 80), "Intercalation", autosaveName="com.juandelperal.Intercalation.mainwindow" )
		self.w.text = vanilla.TextBox( (13, 15, 250, 20), "String to intercal with selected glyphs", sizeStyle='small')
		self.w.interCharacter = vanilla.EditText( (15, 35, 200, 20), "H", sizeStyle='small', callback=self.SavePreferences )
		self.w.go = vanilla.Button( (220, 30, 60, 30), "Go", sizeStyle='small', callback=self.Intercal )
		self.w.cancel = vanilla.Button( (285, 30, 60, 30), "Close", sizeStyle='small', callback=self.Close )
		
		self.w.setDefaultButton( self.w.go )

		if not self.LoadPreferences( ):
			print "Error: Could not load preferences. Will resort to defaults."

		self.w.open()
		self.w.makeKey()


	def SavePreferences( self, sender ):
		Glyphs.defaults["com.juandelperal.Intercalation.mainwindow.interCharacter"] = self.w.interCharacter.get()
		
		return True

	def LoadPreferences( self ):
		try:
			self.w.interCharacter.set( Glyphs.defaults["com.juandelperal.Intercalation.mainwindow.interCharacter"] )
		except:
			return False
		
		return True
		
	def Intercal(self, sender):
		interCharacter = self.w.interCharacter.get()
		for thisLayer in selectedLayers:
			thisGlyphName = thisLayer.parent.name
			outputString +='/'+thisGlyphName+ interCharacter
		
		Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", outputString, True )
		self.w.close()

	def Close(self, sender):
		self.w.close()
		
OpenTab()