#MenuTitle: OT Find and Replace
# -*- coding: utf-8 -*-
__doc__="""
Replace code in features and classes. Requires Vanilla
"""

import GlyphsApp
import vanilla

Font = Glyphs.font
Classes = Font.classes
Features = Font.features


class Replace(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow( (360, 130), "OT Find and Replace", autosaveName="com.juandelperal.OTfindreplace.mainwindow" )
		self.w.text = vanilla.TextBox( (13, 15, 250, 20), "Search", sizeStyle='small')
		self.w.find = vanilla.EditText( (15, 30, 200, 20), "search", sizeStyle='small', callback=self.SavePreferences )
		self.w.text2 = vanilla.TextBox( (13, 60, 250, 20), "Replace", sizeStyle='small')
		self.w.replace = vanilla.EditText( (15, 75, 200, 20), "replace", sizeStyle='small', callback=self.SavePreferences )
		self.w.go = vanilla.Button( (220, 30, 60, 30), "Replace", sizeStyle='small', callback=self.OTfindreplace )
		self.w.cancel = vanilla.Button( (285, 30, 60, 30), "Close", sizeStyle='small', callback=self.Close )
		
		self.w.setDefaultButton( self.w.go )

		if not self.LoadPreferences( ):
			print "Error: Could not load preferences. Will resort to defaults."

		self.w.open()
		self.w.makeKey()


	def SavePreferences( self, sender ):
		Glyphs.defaults["com.juandelperal.OTfindreplace.mainwindow.find"] = self.w.find.get()
		Glyphs.defaults["com.juandelperal.OTfindreplace.mainwindow.replace"] = self.w.replace.get()
		
		return True

	def LoadPreferences( self ):
		try:
			self.w.find.set( Glyphs.defaults["com.juandelperal.OTfindreplace.mainwindow.find"] )
			self.w.replace.set( Glyphs.defaults["com.juandelperal.OTfindreplace.mainwindow.replace"] )
		except:
			return False
		
		return True
		
	def OTfindreplace(self, sender):
		searchFor = self.w.find.get()
		replaceBy = self.w.replace.get()
		for each in (Features and Classes):
			oldCode = each.code
			each.code = oldCode.replace(searchFor,replaceBy)

	def Close(self, sender):
		self.w.close()
		
Replace()