"""
Minecraft Clone using Ursina Engine.

A voxel-based sandbox game clone built with Python and Ursina Engine.
Compatible with Python 3.13+ and Ursina Engine 8.3.0+.
"""

from __future__ import annotations

import random

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# Initialize Minecraft app using Ursina Engine
minecraft_app = Ursina()

# Block texture paths (snake_case)
BLOCK_TEXTURES = {
    'Sand Block': 'assets/graphical_assets/sand.png',
    'Stone Block': 'assets/graphical_assets/stone_block.png',
    'Stone Brick': 'assets/graphical_assets/stone_brick.png',
    'Wood Plank': 'assets/graphical_assets/wood_plank.jpg',
    'Leaves': 'assets/graphical_assets/leaves.png',
    'Obsidian': 'assets/graphical_assets/obsidian.png',
    'Sponge': 'assets/graphical_assets/sponge.jpg',
    'Gold Ore Block': 'assets/graphical_assets/gold_ore_block.png',
    'Diamond Ore Block': 'assets/graphical_assets/diamond_ore_block.png',
    'Emerald Ore Block': 'assets/graphical_assets/emerald_ore_block.png',
}

# Load all block textures
sand_block_texture = load_texture(BLOCK_TEXTURES['Sand Block'])
stone_block_texture = load_texture(BLOCK_TEXTURES['Stone Block'])
stone_brick_texture = load_texture(BLOCK_TEXTURES['Stone Brick'])
wood_plank_texture = load_texture(BLOCK_TEXTURES['Wood Plank'])
leaves_texture = load_texture(BLOCK_TEXTURES['Leaves'])
obsidian_texture = load_texture(BLOCK_TEXTURES['Obsidian'])
sponge_texture = load_texture(BLOCK_TEXTURES['Sponge'])
gold_ore_block_texture = load_texture(BLOCK_TEXTURES['Gold Ore Block'])
diamond_ore_block_texture = load_texture(BLOCK_TEXTURES['Diamond Ore Block'])
emerald_ore_block_texture = load_texture(BLOCK_TEXTURES['Emerald Ore Block'])

# Sky texture
sky_texture = load_texture('assets/graphical_assets/sky.png')

# Block placing/destroying sound
block_sound = Audio('assets/sound_assets/block_sound.mp3', loop=False, autoplay=False)

# Player WASD movement sound
player_movement_sound = Audio('assets/sound_assets/player_movement_sound.mp3', loop=True, autoplay=False)

# Block choice mapping
TEXTURE_MAP = {
    'Sand Block': sand_block_texture,
    'Stone Block': stone_block_texture,
    'Stone Brick': stone_brick_texture,
    'Wood Plank': wood_plank_texture,
    'Leaves': leaves_texture,
    'Obsidian': obsidian_texture,
    'Sponge': sponge_texture,
    'Gold Ore Block': gold_ore_block_texture,
    'Diamond Ore Block': diamond_ore_block_texture,
    'Emerald Ore Block': emerald_ore_block_texture,
}

# Default block choice is Sand Block
block_choice: str = 'Sand Block'

# Key to block choice mapping
KEY_BLOCK_MAP = {
    '1': 'Sand Block',
    '2': 'Stone Block',
    '3': 'Stone Brick',
    '4': 'Wood Plank',
    '5': 'Leaves',
    '6': 'Obsidian',
    '7': 'Sponge',
    '8': 'Gold Ore Block',
    '9': 'Diamond Ore Block',
    '0': 'Emerald Ore Block',
}


def update() -> None:
    """
    Update function for block selection and hand movements.

    Called every frame by the Ursina engine.
    """
    global block_choice

    # Block selection via number keys
    for key, block in KEY_BLOCK_MAP.items():
        if held_keys[key]:
            block_choice = block

    # Hand movement on mouse click
    if held_keys['left mouse'] or held_keys['right mouse']:
        player_hand.active()
    else:
        player_hand.passive()

    # WASD movement sound control
    if held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']:
        pass  # Sound plays when moving
    else:
        player_movement_sound.play()


class Voxel(Button):
    """
    Voxel class representing a block in the Minecraft world.

    Handles block placement and destruction interactions.
    """

    def __init__(self, position: tuple[float, float, float] = (0, 0, 0), texture: Texture = sand_block_texture) -> None:
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.gray,
        )

    def input(self, key: str) -> None:
        """
        Handle mouse input for block placement and destruction.

        Args:
            key: The input key/event to handle.
        """
        if not self.hovered:
            return

        if key == 'left mouse down':
            # Play block placing sound
            block_sound.play()

            # Get texture for current block choice
            texture = TEXTURE_MAP.get(block_choice, sand_block_texture)

            # Place new block
            Voxel(position=self.position + mouse.normal, texture=texture)

        elif key == 'right mouse down':
            # Play block destroying sound
            block_sound.play()

            # Destroy block
            destroy(self)


class Sky(Entity):
    """Sky entity for the Minecraft world."""

    def __init__(self) -> None:
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True,
        )


class PlayerHand(Entity):
    """
    Player hand entity for block interaction visualization.

    Handles hand animation when placing/destroying blocks.
    """

    def __init__(self) -> None:
        super().__init__(
            parent=camera.ui,
            model='cube',
            scale=(0.1, 0.99, 0.1),
            texture='assets/graphical_assets/player_arm.png',
            rotation=Vec3(50, 55, -60),
            position=Vec2(0.406, -0.42),
        )

    def active(self) -> None:
        """Move hand to active (clicking) position."""
        self.position = Vec2(0.39, -0.39)

    def passive(self) -> None:
        """Return hand to passive (idle) position."""
        self.position = Vec2(0.406, -0.42)


# Create Minecraft world area (20x20 blocks)
dimension: int = 20
for i in range(dimension):
    for j in range(dimension):
        Voxel(position=(i, 0, j))

# Initialize player with FPP view
minecraft_player = FirstPersonController()

# Initialize sky
sky = Sky()

# Initialize player hand
player_hand = PlayerHand()

# Window configuration
window.title = 'Minecraft Clone Using Ursina Engine'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# Run Minecraft app
minecraft_app.run()
