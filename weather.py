from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import *
from panda3d.physics import LinearVectorForce
from panda3d.core import CollisionNode, CollisionSphere

import settings
import functions

#This script controls weather effects, but also general particle effects.

class Weather:

    def __init__(self):
        base.enableParticles()

        self.fog = Fog("fog")

        self.shed_window_snow = False

        self.fire = ParticleEffect()
        self.fire.loadConfig('particles/fire.ptf')
        self.steam = ParticleEffect()
        self.steam.loadConfig('particles/steam.ptf')

        self.control_all()
        

    def control_all(self):

        #Before, I called __init__ every time. Causes issues.
        path = 'light'
        if settings.snow:
            path = settings.snow
        snow_path= 'particles/'+path+'_snow.ptf'
        self.player_snow = ParticleEffect()
        self.player_snow.loadConfig(snow_path)
        self.start_snow()
        
        wsnowpath = 'particles/'+path+'_window_snow.ptf'
        self.wsnows = [ParticleEffect(), ParticleEffect(),
                  ParticleEffect(), ParticleEffect()]
        for snow in self.wsnows:
            snow.loadConfig(wsnowpath)
        self.start_window_snow()
        
        self.control_fog()
        self.control_snow()


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
            self.stop_window_snow()

        self.stove_steam()

    def start_snow(self):
        self.player_snow.start(parent=render, renderParent=render)

    def stop_window_snow(self):
        for snow in self.wsnows:
            snow.disable()
            
    def start_window_snow(self):
        for snow in self.wsnows:
            snow.start(parent=render, renderParent=render)
        if settings.environment[:4] == 'inte':
            self.wsnows[0].set_pos(-3,11.4,4) #kitchen
            self.wsnows[1].set_pos_hpr(-9,0,5,90,0,0)
            self.wsnows[2].set_pos(-3,-16.2,4) #bedroom
            self.wsnows[3].set_pos(10,-8.2,4) #bathroom
            self.wsnows[1].get_force_group_list()[1].disable()

        elif settings.environment[:4] == 'hang':
            self.wsnows[0].set_pos_hpr(-19,-1.5,6, 90,-45,0)
            self.wsnows[0].get_force_group_list()[1].disable()
            self.wsnows[1].set_pos_hpr(-19,4.5,6, 90,-45,0)
            self.wsnows[1].get_force_group_list()[1].disable()
            self.wsnows[2].set_pos_hpr(-19,-7.5,6, 90,-45,0)
            self.wsnows[2].get_force_group_list()[1].disable()
            self.wsnows[3].disable()

    def control_fog(self):
        self.fog.setExpDensity(0.0)
        if not settings.snow:
            return

        #Weird behaviour. Manually setting fog color works, but this doesn't
        #Is the fog color changed somewhere else?
        #Threading is a bitch
        
        vec = self.set_fog_color()
        self.fog.setColor(vec)
            
        if settings.snow == 'heavy':
            if settings.environment[:4] == 'exte':
                self.fog.setExpDensity(0.02)
            else:
                self.fog.setExpDensity(0.005)

        elif settings.snow == 'light':
            self.fog.setExpDensity(0.0001)

        else:
            self.fog.setExpDensity(0.0)
            
        settings.fog = self.fog

    def set_fog_color(self):
        if settings.time == 1:
            return LVecBase4f(0.9,0.9,0.9,1)
        elif settings.time == 2:
            return LVecBase4f(0.2,0.2,0.25,1)
        elif settings.time == 3:
            return LVecBase4f(0.1,0.1,0.2,1)

    def shed_snow(self):
        if not self.shed_window_snow:
            self.shed_window_snow = True
            self.player_snow.disable()
            self.start_window_snow()

            self.wsnows[0].set_pos_hpr(55,6,5, 250,0,0)
            self.wsnows[0].set_scale(1.5)
            self.wsnows[0].get_force_group_list()[1].disable()
            self.wsnows[1].set_pos_hpr(67,6,5, 336,0,0)
            self.wsnows[1].set_scale(1.5)
            self.wsnows[1].get_force_group_list()[1].disable()
            self.wsnows[2].set_pos_hpr(63,-13.5,5, 156,0,0)
            self.wsnows[2].set_scale(1.5)
            self.wsnows[2].get_force_group_list()[1].disable()
            self.wsnows[3].set_pos_hpr(50,-5,5, 250,0,0)
            self.wsnows[3].get_force_group_list()[1].disable()
            self.wsnows[3].set_scale(1.5)
        else:
            self.shed_window_snow = False
            self.start_snow()
            self.stop_window_snow()

    def stove_steam(self):
        #Also controls furnace fire
        if settings.environment[:4] == 'inte':
            self.steam.start(parent=render, renderParent=render)
            self.fire.start(parent=render, renderParent=render)
            self.steam.set_pos(5.20,4.30,0.6)
            self.fire.set_pos(5,3.6,-0.9)
        elif settings.environment[:4] == 'exte':
            self.steam.start(parent=render, renderParent=render)
            self.steam.set_pos(5.20,3.5,6.4)
            self.fire.disable()
        else:
            self.steam.disable()
            self.fire.disable()
            
        








