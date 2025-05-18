import arcade
import random


class Fish1(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish1"
        self.difficulty = 0, 5
        self.value = 10
        self.fish1_texture = arcade.load_texture("")
        self.fish1_sprite = arcade.Sprite(self.fish1_texture)


class Fish2(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish2"
        self.difficulty = 0, 5
        self.value = 10
        self.fish2_texture = arcade.load_texture("")
        self.fish2_sprite = arcade.Sprite(self.fish2_texture)


class Fish3(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish3"
        self.difficulty = 0, 10
        self.value = 30
        self.fish3_texture = arcade.load_texture("")
        self.fish3_sprite = arcade.Sprite(self.fish3_texture)


class Fish4(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish4"
        self.difficulty = 0, 10
        self.value = 30
        self.fish4_texture = arcade.load_texture("")
        self.fish4_sprite = arcade.Sprite(self.fish4_texture)


class Fish5(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish5"
        self.difficulty = 0, 15
        self.value = 50
        self.fish5_texture = arcade.load_texture("")
        self.fish5_sprite = arcade.Sprite(self.fish5_texture)


class Fish6(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish6"
        self.difficulty = 0, 15
        self.value = 60
        self.fish6_texture = arcade.load_texture("")
        self.fish6_sprite = arcade.Sprite(self.fish6_texture)


class Fish7(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish7"
        self.difficulty = 0, 20
        self.value = 70
        self.fish7_texture = arcade.load_texture("")
        self.fish7_sprite = arcade.Sprite(self.fish7_texture)


class Fish8(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish8"
        self.difficulty = 0, 20
        self.value = 80
        self.fish8_texture = arcade.load_texture("")
        self.fish8_sprite = arcade.Sprite(self.fish8_texture)


class Fish9(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish9"
        self.difficulty = 0, 25
        self.value = 90
        self.fish9_texture = arcade.load_texture("")
        self.fish9_sprite = arcade.Sprite(self.fish9_texture)


class Fish10(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "fish10"
        self.difficulty = 0, 25
        self.value = 100
        self.fish10_texture = arcade.load_texture("")
        self.fish10_sprite = arcade.Sprite(self.fish10_texture)


class Fish11(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "Naval Bomb"
        self.bomb_texture = arcade.load_texture("")
        self.bomb_sprite = arcade.Sprite(self.bomb_texture)
