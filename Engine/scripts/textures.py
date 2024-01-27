import pygame as pg
import moderngl as mgl

class Textures:
    def __init__(self,app,texture_dir):
        self.app = app
        self.ctx = self.app.ctx
        self.texture_dir = texture_dir

        self.textures = [] # For import by setup 
        TextureIndex = 0
        for Texture in self.textures:
            TextureClass = Texture[0]
            IsArray = Texture[1]
            TextureClass.use(location=TextureIndex)
            TextureIndex = TextureIndex + 1
    def load(self, file_name, is_tex_array=False):
        texture = pg.image.load(f"{self.texture_dir}/{file_name}")
        texture = pg.transform.flip(texture, flip_x=True, flip_y=False)

        if is_tex_array:
            num_layers = 3 * texture.get_height() // texture.get_width()
            texture = self.app.ctx.texture_array()

