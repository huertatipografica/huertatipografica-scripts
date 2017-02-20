ç#MenuTitle: add/rename suffix
# -*- coding: utf-8 -*-
__doc__="""
Requires vanilla
"""
import GlyphsApp
import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

class OpenTab(object):

	def __init__(self):
		self.tabString = ''

		self.w = vanilla.FloatingWindow( (360, 95), "Add or rename suffix", autosaveName="com.juandelperal.renamer.mainwindow" )
		self.w.text = vanilla.TextBox( (13, 15, 320, 20), "New suffix (include.)", sizeStyle='small')
		self.w.suffix = vanilla.EditText( (15, 35, 200, 20), "H", sizeStyle='small', placeholder='.ss08', callback=self.SavePreferences )
		self.w.remove = vanilla.CheckBox( (15, 60, 200, 20), "Remove current suffix", sizeStyle='small', value=False, callback=self.SavePreferences )
		self.w.go = vanilla.Button( (220, 30, 60, 30), "Go", sizeStyle='small', callback=self.GoForIt )
		self.w.cancel = vanilla.Button( (285, 30, 60, 30), "Close", sizeStyle='small', callback=self.Close )

		self.w.setDefaultButton( self.w.go )

		if not self.LoadPreferences( ):
			print "Error: Could not load preferences. Will resort to defaults."

		self.w.open()
		self.w.makeKey()


	def SavePreferences( self, sender ):
		Glyphs.defaults["com.juandelperal.renamer.mainwindow.suffix"] = self.w.suffix.get()
		Glyphs.defaults["com.juandelperal.renamer.mainwindow.remove"] = self.w.remove.get()

		return True

	def LoadPreferences( self ):
		try:
			self.w.suffix.set( Glyphs.defaults["com.juandelperal.renamer.mainwindow.suffix"] )
			self.w.remove.set( Glyphs.defaults["com.juandelperal.renamer.mainwindow.remove"] )
		except:
			return False

		return True

	def GoForIt(self, sender):
		Glyphs.clearLog()
		Glyphs.showMacroWindow()
		self.w.close()

		suffix = self.w.suffix.get()

		for l in selectedLayers:
			glyph = l.parent
			oldName = glyph.name

			if self.w.remove.get():
				newName = oldName.split(".")[0] + suffix
			else :
				newName = oldName  + suffix

			glyph.name = newName
			print "%s --> %s" % (oldName, newName)


	def Close(self, sender):
		self.w.close()

OpenTab()