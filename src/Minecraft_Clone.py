# Import all important modules
from ursina import *    # For usage of all nessecary modules of 'Ursina'. Such as 'Button', 'Entity', etc.
from ursina.prefabs.first_person_controller import FirstPersonController    # For 'FPP (First Person Perspective)' View of 'Minecraft' Character

# Initialize 'Minecraft' app using 'Ursina' Engine
minecraft_app = Ursina()

# All Block Textures
sand_block_texture = load_texture('Assets/Graphical Assets/Sand.png')
stone_block_texture = load_texture('Assets/Graphical Assets/Stone_Block.png')
stone_brick_texture = load_texture('Assets/Graphical Assets/Stone_Brick.png')
wood_plank_texture = load_texture('Assets/Graphical Assets/Wood_Plank.jpg')
leaves_texture = load_texture('Assets/Graphical Assets/Leaves.png')
obsidian_texture = load_texture('Assets/Graphical Assets/Obsidian.png')
sponge_texture = load_texture('Assets/Graphical Assets/Sponge.jpg')
gold_ore_block_texture = load_texture('Assets/Graphical Assets/Gold_Ore_Block.png')
diamond_ore_block_texture = load_texture('Assets/Graphical Assets/Diamond_Ore_Block.png')
emerald_ore_block_texture = load_texture('Assets/Graphical Assets/Emerald_Ore_Block.png')

# Sky Texture
sky_texture = load_texture('Assets/Graphical Assets/Sky.png')

# Block Placing/ Destroying Sound
block_sound = Audio('Assets/Sound Assets/Block_Sound.mp3', loop = False, autoplay = False)

# Player 'WASD' Movement Sound
player_movement_sound = Audio('Assets/Sound Assets/Player_Movement_Sound.mp3', loop = True, autoplay = False)

# By Declaration of 'Block Choice Variable' and by default block was 'Sand Block'
block_choice = 'Sand Block'

# Declare 'update()' function for the 'Choice of Block' and 'Hand Movements' Functionalities
def update():
    # Choice of Block Part
    global block_choice
    if held_keys['1']:
        block_choice = 'Sand Block'
    if held_keys['2']:
        block_choice = 'Stone Block'
    if held_keys['3']:
        block_choice = 'Stone Brick'
    if held_keys['4']:
        block_choice = 'Wood Plank'
    if held_keys['5']:
        block_choice = 'Leaves'
    if held_keys['6']:
        block_choice = 'Obsidian'
    if held_keys['7']:
        block_choice = 'Sponge'
    if held_keys['8']:
        block_choice = 'Gold Ore Block'
    if held_keys['9']:
        block_choice = 'Diamond Ore Block'
    if held_keys['0']:
        block_choice = 'Emerald Ore Block'

    # Hand Movement Part
    if held_keys['left mouse'] or held_keys['right mouse']:
        player_hand.active()
    else:
        player_hand.passive()

    # 'WASD' Movement Sound of Player 
    if not (held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']):
        player_movement_sound.play()
    if (held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']):
        pass

''' 'Minecraft' is a game based on 'Blocks' which is also known as 'Voxel'. 
So, we have declared 'Voxel' class for 'Block' Manipulation in game. '''
class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = sand_block_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color = color.gray
        )

    # Declaration of 'input()' function for 'onClick()' operations such as 'Place Block', 'Remove Block'
    def input(self, key):
        if self.hovered:
            # Press 'Left Click' to 'Place Block' 
            if key == 'left mouse down':
                # Play Block placing Sound
                block_sound.play()

                # Place Block accrding to your Choice
                if block_choice == 'Sand Block':
                    voxel = Voxel(position = self.position + mouse.normal, texture = sand_block_texture)
                if block_choice == 'Stone Block':
                    voxel = Voxel(position = self.position + mouse.normal, texture = stone_block_texture)
                if block_choice == 'Stone Brick':
                    voxel = Voxel(position = self.position + mouse.normal, texture = stone_brick_texture)
                if block_choice == 'Wood Plank':
                    voxel = Voxel(position = self.position + mouse.normal, texture = wood_plank_texture)
                if block_choice == 'Leaves':
                    voxel = Voxel(position = self.position + mouse.normal, texture = leaves_texture)
                if block_choice == 'Obsidian':
                    voxel = Voxel(position = self.position + mouse.normal, texture = obsidian_texture)
                if block_choice == 'Sponge':
                    voxel = Voxel(position = self.position + mouse.normal, texture = sponge_texture)
                if block_choice == 'Gold Ore Block':
                    voxel = Voxel(position = self.position + mouse.normal, texture = gold_ore_block_texture)
                if block_choice == 'Diamond Ore Block':
                    voxel = Voxel(position = self.position + mouse.normal, texture = diamond_ore_block_texture)
                if block_choice == 'Emerald Ore Block':
                    voxel = Voxel(position = self.position + mouse.normal, texture = emerald_ore_block_texture)

            # Press 'Right Click' to 'Remove Block' 
            if key == 'right mouse down':
                # Play Block destroying Sound
                block_sound.play()
                # Destroy Block
                destroy(self)

# Declare 'Sky()' Class
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )

# Declare 'Player_Hand()' Class
class Player_Hand(Entity):
        def __init__(self):
                super().__init__(
                    parent = camera.ui,
                    model = 'cube',
                    scale = (0.1, 0.99, 0.1),
                    texture = 'Assets/Graphical Assets/Player_Arm.png',
                    rotation = Vec3(50, 55, -60),
                    position = Vec2(0.406, -0.42)
                    )

        def active(self):
                self.position = Vec2(0.39, -0.39) 

        def passive(self):
                self.position = Vec2(0.406, -0.42)

# Make Area for your 'Minecraft' World
dimension = 20  # 'Dimension' should be of 20X20 Blocks
for i in range(dimension):
    for j in range(dimension):
        # Initialize 'Voxel' class
        voxel = Voxel(position = (i, 0, j))

# Initialize your 'Minecraft' Player using FPP View
minecraft_player = FirstPersonController()

# Initialize 'Sky' for your 'Minecraft World'
sky = Sky()

# Initialization of 'Player Hand' Class for 'Minecraft Player'
player_hand = Player_Hand()

# The window title
window.title = 'Minecraft Clone Using Ursina Engine'
# Show a border                
window.borderless = False 
# Do not go Fullscreen              
window.fullscreen = False        
# Do not show the in-game red 'X' that 'Closes the Window'       
window.exit_button.visible = False 
# Show the FPS (Frames per second) counter     
window.fps_counter.enabled = True       

# Run 'Minecraft' app
minecraft_app.run()