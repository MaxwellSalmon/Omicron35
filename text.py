#Text module
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import *

class Text:

    def __init__(self):
        string = ''
        self.text = OnscreenText(text=string, pos=(0, -0.8), scale=0.07, align=TextNode.ACenter,
                                  wordwrap=30, fg=(255,255,255,1), shadow=(0,0,0,0.8), mayChange=True)

    def new_text(self, string):
        self.text.text = string

    def new_colour(self, rgba):
        self.text.fg = rgba

    def new_pos(self, x,y):
        #lol weird coordinates.
        self.text.set_pos(x,0,y)

    def new_size(self, size):
        self.text.set_scale(size)
        
        
