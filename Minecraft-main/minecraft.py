from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

oyna = Ursina()


osmon_texture = load_texture('assets/skybox.png')
maysa_texture = load_texture('assets/grassblock.png')
tosh_texture = load_texture('assets/stone_block.png')
loy_texture = load_texture('assets/dirt_block.png')
grass_texture = load_texture('assets/grass_block.png')
brick_texture = load_texture('assets/brick_block.png')
arm_texture = load_texture('assets/arm_texture.png')
ovoz_effekt = Audio('assets/seffect.wav', loop = False, autoplay = False)

block_check = 1

camera.fov = 100

def update():
    global block_check

    if held_keys['right mouse'] or held_keys['left mouse']:
        hand.avtive()
    else:
        hand.passive()

    if held_keys['1']: block_check = 1
    if held_keys['2']: block_check = 2
    if held_keys['3']: block_check = 3
    if held_keys['4']: block_check = 4
    if held_keys['5']: block_check = 5

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture= maysa_texture):
        super().__init__(
        parent = scene,
        position = position,
        model = 'assets/block',
        origin_y = 0.5,
        texture = texture,
        color = color.color(0, 0, random.uniform(0.9, 1)),
        scale = 0.5,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                ovoz_effekt.play()

                if block_check == 1: voxel = Voxel(position = self.position + mouse.normal, texture= maysa_texture)
                if block_check == 2: voxel = Voxel(position = self.position + mouse.normal, texture= tosh_texture)
                if block_check == 3: voxel = Voxel(position = self.position + mouse.normal, texture= loy_texture)
                if block_check == 4: voxel = Voxel(position = self.position + mouse.normal, texture= brick_texture)
                if block_check == 5: voxel = Voxel(position = self.position + mouse.normal, texture= grass_texture)

            elif  key == 'right mouse down':
                ovoz_effekt.play()
                destroy(self)

class Osmon(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = osmon_texture,
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "assets/arm",
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
            )

    def avtive(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.4, -0.6)
        


for x in range(20):
    for z in range(20):
        voxel = Voxel(position = (x,0,z))

oyinchi = FirstPersonController()
osmon = Osmon()
hand = Hand()

def input(key):
     if key == 'k':
        quit()

oyna.run()


