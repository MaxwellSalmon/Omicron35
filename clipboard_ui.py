import settings
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib


class ClipboardUI:

    def __init__(self):
        self.img = None
        self.values = None
        self.line1 = None
        self.line2 = None

    def open_ui(self):
        if settings.g_bools['has_clipboard']:
            #Add animation to the UI
            if not settings.ui_open:
                self.img = OnscreenImage(image='textures/ui/clipboardUI.png', pos=(0,0,0), scale=(0.7,1,0.9))
                self.img.setTransparency(TransparencyAttrib.MAlpha)
                settings.ui_open = True
                self.update()
            else:
                self.img.destroy()
                self.destroy_appendix()
                settings.ui_open = False

    def determine_values(self):
        if settings.day == 1:
            return 'd1_values.png'
        

    def destroy_appendix(self):
        if self.line1:
            self.line1.destroy()
        if self.line2:
            self.line2.destroy()
        if self.values:
            self.values.destroy()

    def update(self):
        if settings.g_bools['generator_refilled']:
            self.line1 = OnscreenImage(image='textures/ui/line.png', pos=(-0.31,0,0.08), scale=(0.2,1,0.015))
            self.line1.setTransparency(TransparencyAttrib.MAlpha)
        if settings.g_bools['firewood']:
            self.line2 = OnscreenImage(image='textures/ui/line.png', pos=(-0.31,0,0.015), scale=(0.2,1,0.015))
            self.line2.setTransparency(TransparencyAttrib.MAlpha)
        if settings.g_bools['weather_measured']:
            self.values = OnscreenImage(image='textures/ui/'+self.determine_values(),
                                        pos=(0,0,0.31), scale=(0.05,1,0.06))
            self.values.setTransparency(TransparencyAttrib.MAlpha)
        


