from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import *

import settings

class Weather:

    def __init__(self):
        base.enableParticles()
        snow_path= 'particles/'+settings.snow+'_snow.ptf'
        self.player_snow = ParticleEffect()
        self.player_snow.loadConfig(snow_path)
        self.start_snow()
        
        wsnowpath = 'particles/'+settings.snow+'_window_snow.ptf'
        self.wsnows = [ParticleEffect(), ParticleEffect(),
                  ParticleEffect(), ParticleEffect()]
        for snow in self.wsnows:
            snow.loadConfig(wsnowpath)
        self.start_window_snow()

        self.fog = Fog("fog")

        self.control_fog()
        self.control_snow()

       # self.wsnows[3].place()

    def move_player_snow(self):
        if self.player_snow.is_enabled():
            self.player_snow.set_pos(base.player.body.get_pos())
            self.player_snow.set_z(8)

    def control_snow(self):
        if settings.snow:
            if settings.environment[:4] == 'exte':
                self.stop_window_snow()
                self.start_snow()
            else:
                self.player_snow.disable()
                self.start_window_snow()
        else:
            self.player_snow.disable()

    def start_snow(self):
        self.player_snow.start(parent=render, renderParent=render)

    def stop_window_snow(self):
        for snow in self.wsnows:
            snow.disable()
            
    def start_window_snow(self):
        for snow in self.wsnows:
            snow.start(parent=render, renderParent=render)
        if settings.environment[:4] == 'inte':
            self.wsnows[0].set_pos(-3,12,4)
            self.wsnows[1].set_pos(-12,-1,5) #Remove wind force
            self.wsnows[2].set_pos(-3,-16,4)
            self.wsnows[3].set_pos(9,-8,4) #Remove wind force

           # self.wsnows[1].SetLinearVectorForce(Vec3(2.0000, 0.0000, -5.0000), 1.0000, 0)
            
            
        

    def control_fog(self):
        if not settings.snow:
            return
        
        self.set_fog_color()
            
        if settings.snow == 'heavy':
            self.fog.setExpDensity(0.05)

        elif settings.snow == 'light':
            self.fog.setExpDensity(0.0001)

        if settings.environment[:4] == 'exte':
            render.setFog(self.fog)
        else:
            self.fog.setExpDensity(0.001) #test this

    def set_fog_color(self):
        if settings.time == 1:
            self.fog.setColor(0.9,0.9,0.9)
        elif setting.time == 3:
            self.fog.setColor(0.1,0.1,0.2)
            



##        self.p = ParticleEffect()
##        self.p.loadConfig('particles/heavy_snow.ptf')
##        self.p.start(parent=render, renderParent=render)
##        self.taskMgr.add(self.temp, "temp")
##
##        self.fog = Fog("fog")

