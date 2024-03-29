import pygame as pg
# OpenGL settings
MAJOR_VER, MINOR_VER = 3, 3
DEPTH_SIZE = 24
NUM_SAMPLES = 1
GL_ATTRUBUITES = [
    [pg.GL_CONTEXT_MAJOR_VERSION, MAJOR_VER],
    [pg.GL_CONTEXT_MINOR_VERSION, MINOR_VER],
    [pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE],
    [pg.GL_DEPTH_SIZE, DEPTH_SIZE],
    [pg.GL_MULTISAMPLESAMPLES, NUM_SAMPLES]
]