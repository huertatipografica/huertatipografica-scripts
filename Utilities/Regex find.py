#MenuTitle: Regex find
# -*- coding: utf-8 -*-
__doc__="""
Search for glyph names using Regular expressions. Needs Vanilla
"""

import GlyphsApp
import re
import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

class OpenTab(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow( (360, 80), "Regex Find", autosaveName="com.juandelperal.regex.mainwindow" )
		self.w.text = vanilla.TextBox( (13, 15, 250, 20), "Regular expression string to search", sizeStyle='small')
		self.w.searchFor = vanilla.EditText( (15, 35, 200, 20), "\u.*", sizeStyle='small', placeholder='sc$' ,  callback=self.SavePreferences )
		self.w.go = vanilla.Button( (220, 30, 60, 30), "Find", sizeStyle='small', callback=self.regexFind )
		self.w.cancel = vanilla.Button( (285, 30, 60, 30), "Close", sizeStyle='small', callback=self.Close )

		self.w.setDefaultButton( self.w.go )

		if not self.LoadPreferences( ):
			print "Error: Could not load preferences. Will resort to defaults."

		self.w.open()
		self.w.makeKey()


	def SavePreferences( self, sender ):
		Glyphs.defaults["com.juandelperal.regex.mainwindow.searchFor"] = self.w.searchFor.get()

		return True

	def LoadPreferences( self ):
		try:
			self.w.searchFor.set( Glyphs.defaults["com.juandelperal.regex.mainwindow.searchFor"] )
		except:
			return False

		return True

	def regexFind(self, sender):
		searchFor = self.w.searchFor.get()
		if not searchFor:
			Message("Hey!", "Type a regular expression for make the search.", OKButton="OK")
		else :
			results = [ g.name for g in Font.glyphs if re.search(searchFor, g.name) ]
			Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", '/' + '/'.join(results), True )
			self.w.close()

	def Close(self, sender):
		self.w.close()

OpenTab()