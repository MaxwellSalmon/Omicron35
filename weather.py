from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import *
from panda3d.physics import LinearVectorForce

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

       # self.wsnows[1].place()

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
            self.wsnows[1].set_pos_hpr(-9,0,5,90,0,0)
            self.wsnows[2].set_pos(-3,-16.2,4)
            self.wsnows[3].set_pos(9.5,-8,4)
            self.wsnows[1].get_force_group_list()[1].disable()

        elif settings.environment[:4] == 'hang':
            self.wsnows[0].set_pos_hpr(-20,-1.5,5, 90,0,0)
            self.wsnows[0].get_force_group_list()[1].disable()
            self.wsnows[1].set_pos_hpr(-20,4.5,5, 90,0,0)
            self.wsnows[1].get_force_group_list()[1].disable()
            self.wsnows[2].set_pos_hpr(-20,-7.5,5, 90,0,0)
            self.wsnows[2].get_force_group_list()[1].disable()
            self.wsnows[3].disable()

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
            if settings.snow == "heavy":
                self.fog.setExpDensity(0.005)
                render.setFog(self.fog)
            else:
                render.clearFog()

    def set_fog_color(self):
        if settings.time == 1:
            self.fog.setColor(0.9,0.9,0.9)
        elif setting.time == 3:
            self.fog.setColor(0.1,0.1,0.2)
