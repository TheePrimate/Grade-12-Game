import random

from constants import *
from library import *


class FishingMiniGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        self.fishing_ticks = 0
        self.fishing_seconds = 0
        self.indicator_ticks = 0
        self.indicator_change_speed = 0
        self.indicator_change_direction = 0
        self.indicator_change_speed_ticks = 0
        self.indicator_change_direction_ticks = 0

        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, fullscreen=True)
        self.fishing_sprite_list = arcade.SpriteList()
        self.wall_block = arcade.SpriteList()
        self.progress_bar_height = 30

        self.hook_texture = arcade.load_texture("assets/KaydenGameBarBeerAnimation.gif")
        self.hook_sprite = arcade.Sprite(self.hook_texture)
        self.hook_sprite.center_x = WINDOW_WIDTH / 2
        self.hook_sprite.center_y = WINDOW_HEIGHT / 2
        self.fishing_sprite_list.append(self.hook_sprite)

        self.indicator_texture = arcade.load_texture("assets/KaydenGameBarDarrienAsCustomer.png")
        self.indicator_sprite = arcade.Sprite(self.indicator_texture)
        self.indicator_sprite.center_x = WINDOW_WIDTH / 2
        self.indicator_sprite.center_y = WINDOW_HEIGHT / 3
        self.fishing_sprite_list.append(self.indicator_sprite)

        self.hook_center_texture = arcade.load_texture("assets/KaydenGameBarDarrienAsCustomer.png")
        self.hook_center_sprite = arcade.Sprite(self.hook_center_texture, scale=0.1)
        self.hook_center_sprite.center_x = self.hook_sprite.center_x
        self.hook_center_sprite.center_y = self.hook_sprite.center_y
        self.fishing_sprite_list.append(self.hook_center_sprite)

        self.hooking_container_top_texture = arcade.load_texture("assets/funnypfp.png")
        self.hooking_container_top_sprite = arcade.Sprite(self.hooking_container_top_texture, scale=0.05)
        self.hooking_container_top_sprite.center_x = WINDOW_WIDTH / 2
        self.hooking_container_top_sprite.center_y = 100
        self.fishing_sprite_list.append(self.hooking_container_top_sprite)
        self.wall_block.append(self.hooking_container_top_sprite)

        self.hooking_container_bot_texture = arcade.load_texture("assets/funnypfp.png")
        self.hooking_container_bot_sprite = arcade.Sprite(self.hooking_container_bot_texture, scale=0.05)
        self.hooking_container_bot_sprite.center_x = WINDOW_WIDTH / 2
        self.hooking_container_bot_sprite.center_y = 800
        self.fishing_sprite_list.append(self.hooking_container_bot_sprite)
        self.wall_block.append(self.hooking_container_bot_sprite)

        self.hooking_container_left_texture = arcade.load_texture("assets/funnypfp.png")
        self.hooking_container_left_sprite = arcade.Sprite(self.hooking_container_left_texture, scale=0.05)
        self.hooking_container_left_sprite.center_x = WINDOW_WIDTH / 4
        self.hooking_container_left_sprite.center_y = WINDOW_HEIGHT / 4
        self.fishing_sprite_list.append(self.hooking_container_left_sprite)

        self.hooking_container_right_texture = arcade.load_texture("assets/funnypfp.png")
        self.hooking_container_right_sprite = arcade.Sprite(self.hooking_container_right_texture, scale=0.05)
        self.hooking_container_right_sprite.center_x = WINDOW_WIDTH / 4
        self.hooking_container_right_sprite.center_y = WINDOW_HEIGHT / 4
        self.fishing_sprite_list.append(self.hooking_container_right_sprite)

        self.physics_engine1 = arcade.PhysicsEnginePlatformer(self.hook_sprite, None,
                                                              GRAVITY, None, self.wall_block)
        self.physics_engine2 = arcade.PhysicsEnginePlatformer(self.indicator_sprite, None,
                                                              0, None, self.wall_block)

        self.collision = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        pass

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        arcade.draw_lbwh_rectangle_filled(50, 50, 50, self.progress_bar_height, (255, 0, 0))
        arcade.draw_text(f'{self.progress_bar_height}%', 50, 50)
        self.fishing_sprite_list.draw()

    def on_update(self, delta_time):
        self.indicator_ticks += 1
        self.fishing_sprite_list.update()
        self.hook_center_sprite.center_x = self.hook_sprite.center_x
        self.hook_center_sprite.center_y = self.hook_sprite.center_y
        self.physics_engine1.update()
        self.physics_engine2.update()
        self.collision = arcade.check_for_collision(self.hook_center_sprite, self.indicator_sprite)
        if self.collision is True:
            self.fishing_ticks += 1
            if self.progress_bar_height < 100:
                self.progress_bar_height += 3
            if self.fishing_ticks % 30 == 0:
                self.fishing_seconds += 1
                print(self.fishing_seconds)

        if self.progress_bar_height > 0:
            self.progress_bar_height -= 1

        self.indicator_change_direction = random.randint(0, 1)
        self.indicator_change_speed_ticks = random.randint(1, 2) * 30
        self.indicator_change_direction_ticks = random.randint(1, 2) * 30

        if self.indicator_ticks % self.indicator_change_speed_ticks == 0:
            self.indicator_sprite.change_y = random.randint(0, 5)

        if self.indicator_ticks % self.indicator_change_direction_ticks == 0:
            if self.indicator_change_direction == 1:
                self.indicator_sprite.change_y = -self.indicator_sprite.change_y

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.hook_sprite.change_y = PLAYER_MOVEMENT_SPEED


def main():
    """Main function"""
    window = FishingMiniGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
