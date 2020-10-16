#Text module
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import *

#Features:
'''paid version: Sequence with text being shown along with speech
Free version: text advances, when clicking
Do we need conversation options?
Change colour on text, depending on who is speaking
Read strings from another file.

So, keep track of how long each string should be shown for.
Keep track of colour of string.'''

class Text:

    def __init__(self):
        string = 'TEST'
        self.text = OnscreenText(text=string, pos=(0, -0.8), scale=0.07, align=TextNode.ACenter,
                                  wordwrap=30, fg=(255,255,255,1), shadow=(0,0,0,0.8), mayChange=True)

    def new_text(self, string):
        print(string)
        self.text.text = string

    def new_colour(self, rgba):
        self.text.fg = rgba
        
        
