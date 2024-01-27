from Config.settings import *
from Config.glSettings import GL_ATTRUBUITES
from Setup.load import *
STEP = 0
try:
    print("[INFO]: Loading modules")
    print("[INFO]: Loading PyGame")
    import pygame as pg
    print("[INFO]: Loaded PyGame")
    STEP = STEP + 1
    print("[INFO]: Loading ModernGL")
    import moderngl as mgl
    print("[INFO]: ModernGL loaded")
    STEP = STEP + 1
    print("[INFO]: Loading SYS")
    import sys
    print("[INFO]: SYS Loaded")
    STEP = STEP + 1
    print("[Info]: Loaded Modules")
except (ImportError,ImportWarning) as ImportFailed:
    print("[IMPORT-ERROR]: Failed to import modules, CODE: "+str(STEP))

class Engine:
    def __init__(self):
        pg.init()
        SettingIndex = 0
        for Setting in GL_ATTRUBUITES:
            print("[INFO]: Loading Setting, Index: "+str(SettingIndex))
            SettingIndex = SettingIndex + 1
            pg.display.gl_set_attribute(Setting[0],Setting[1])
        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = "auto"
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        self.running = True
        self.on_init()
    def on_init(self):
        self.textures = Textures(self)

if __name__ == "__main__":
    EngineClass = Engine()