from pyglet.event import EVENT_HANDLE_STATE

from library import *

''''
current_fish = choice(FISH_LIST, 10, p=[0.25, 0.25, 0.1, 0.1, 0.05, 0.05, ])

print(current_fish)
print(fish_data[current_fish][0])
print(fish_data[current_fish][1])
print(fish_data[current_fish][2])
print(fish_data[current_fish][3])
'''''


class FishingMiniGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.fishing_ticks = 0
        self.fishing_seconds = 0
        self.indicator_ticks = 0
        self.indicator_seconds = 0
        self.indicator_change_speed = 0
        self.indicator_change_direction = 0
        self.indicator_change_speed_ticks = 0
        self.indicator_change_direction_ticks = 0
        self.mouse_hold = False
        self.fishing_minigame_activate = True

        self.fishing_sprite_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.wall_block = arcade.SpriteList()
        self.progress_bar_height = 0

        self.background_texture = arcade.load_texture('assets/background.png')
        self.background_sprite = arcade.Sprite(self.background_texture)
        self.background_sprite.center_x = WINDOW_WIDTH / 2
        self.background_sprite.center_y = WINDOW_HEIGHT / 2
        self.background_list.append(self.background_sprite)

        self.background_bar_texture = arcade.load_texture("assets/blue.png")
        self.background_bar_sprite = arcade.Sprite(self.background_bar_texture)
        self.background_bar_sprite.center_x = FISHING_MINIGAME_X
        self.background_bar_sprite.center_y = FISHING_MINIGAME_Y
        self.fishing_sprite_list.append(self.background_bar_sprite)

        self.hooking_container_left_texture = arcade.load_texture("assets/left.png")
        self.hooking_container_left_sprite = arcade.Sprite(self.hooking_container_left_texture)
        self.hooking_container_left_sprite.center_x = FISHING_MINIGAME_X
        self.hooking_container_left_sprite.center_y = FISHING_MINIGAME_Y
        self.fishing_sprite_list.append(self.hooking_container_left_sprite)

        self.hooking_container_right_texture = arcade.load_texture("assets/right.png")
        self.hooking_container_right_sprite = arcade.Sprite(self.hooking_container_right_texture)
        self.hooking_container_right_sprite.center_x = FISHING_MINIGAME_X
        self.hooking_container_right_sprite.center_y = FISHING_MINIGAME_Y
        self.fishing_sprite_list.append(self.hooking_container_right_sprite)

        self.hooking_container_bot_texture = arcade.load_texture("assets/bot.png")
        self.hooking_container_bot_sprite = arcade.Sprite(self.hooking_container_bot_texture)
        self.hooking_container_bot_sprite.center_x = FISHING_MINIGAME_X
        self.hooking_container_bot_sprite.center_y = FISHING_MINIGAME_Y
        self.fishing_sprite_list.append(self.hooking_container_bot_sprite)
        self.wall_block.append(self.hooking_container_bot_sprite)

        self.hooking_container_top_texture = arcade.load_texture("assets/top.png")
        self.hooking_container_top_sprite = arcade.Sprite(self.hooking_container_top_texture)
        self.hooking_container_top_sprite.center_x = FISHING_MINIGAME_X
        self.hooking_container_top_sprite.center_y = FISHING_MINIGAME_Y
        self.fishing_sprite_list.append(self.hooking_container_top_sprite)
        self.wall_block.append(self.hooking_container_top_sprite)

        self.indicator_texture = arcade.load_texture("assets/bar.png")
        self.indicator_sprite = arcade.Sprite(self.indicator_texture)
        self.indicator_sprite.center_x = FISHING_MINIGAME_X
        self.indicator_sprite.center_y = FISHING_MINIGAME_Y
        self.fishing_sprite_list.append(self.indicator_sprite)

        self.hook_texture = arcade.load_texture("assets/hook.png")
        self.hook_sprite = arcade.Sprite(self.hook_texture)
        self.hook_sprite.center_x = FISHING_MINIGAME_X
        self.hook_sprite.center_y = FISHING_MINIGAME_Y
        self.fishing_sprite_list.append(self.hook_sprite)
              
        self.progress_bar_texture = arcade.load_texture("assets/progress_bar.png")
        self.progress_bar_sprite = arcade.Sprite(self.progress_bar_texture)
        self.progress_bar_sprite.center_x = FISHING_MINIGAME_X
        self.progress_bar_sprite.center_y = FISHING_MINIGAME_Y
        self.fishing_sprite_list.append(self.progress_bar_sprite)

        self.progress_bar_bar_texture = arcade.load_texture("assets/progress_bar_bar.png")
        self.progress_bar_bar_sprite = arcade.Sprite(self.progress_bar_bar_texture)
        self.progress_bar_bar_sprite.center_x = FISHING_MINIGAME_X
        self.progress_bar_bar_sprite.center_y = FISHING_MINIGAME_Y
        self.fishing_sprite_list.append(self.progress_bar_bar_sprite)

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

        self.background_list.draw()
        if self.fishing_minigame_activate is True:
            self.fishing_sprite_list.draw(pixelated=True)
            arcade.draw_lbwh_rectangle_filled(300, 300, 50, self.progress_bar_height, (255, 0, 0))
            arcade.draw_text(f'{self.progress_bar_height}%', 300, 300)

    def on_update(self, delta_time):
        if self.fishing_minigame_activate is True:
            self.indicator_ticks += 1
            self.fishing_sprite_list.update()
            self.physics_engine1.update()
            self.physics_engine2.update()

            self.collision = arcade.check_for_collision(self.hook_sprite, self.indicator_sprite)
            print(self.progress_bar_bar_sprite.height)

            if self.collision:
                self.fishing_ticks += 1
                if self.progress_bar_bar_sprite.height < 1200:
                    print(self.progress_bar_height)
                    self.progress_bar_height += 1
                    self.progress_bar_bar_sprite.bottom = 224
                    self.progress_bar_bar_sprite.height += 1
                if self.progress_bar_bar_sprite.height >= 1200:
                    self.fishing_minigame_activate = False
                    print("Mini Game Successful")
                if self.fishing_ticks % TICK_RATE == 0:
                    self.fishing_seconds += 1
                    print(self.fishing_seconds)
            else:
                if self.progress_bar_bar_sprite.height > 0:
                    self.progress_bar_bar_sprite.bottom = 224
                    self.progress_bar_bar_sprite.height -= 1

            if self.indicator_ticks % TICK_RATE == 0:
                self.indicator_seconds += 1
                print(self.indicator_seconds)
                if self.indicator_seconds == 20:
                    self.fishing_minigame_activate = False
                    print("Mini Game Failed")

            self.indicator_change_direction = random.randint(0, 1)
            self.indicator_change_speed_ticks = random.randint(1, 2) * TICK_RATE
            self.indicator_change_direction_ticks = random.randint(1, 2) * TICK_RATE

            if self.indicator_ticks % self.indicator_change_speed_ticks == 0:
                self.indicator_sprite.change_y = random.randint(0, 5)

            if self.indicator_ticks % self.indicator_change_direction_ticks == 0:
                if self.indicator_change_direction == 1:
                    self.indicator_sprite.change_y = -self.indicator_sprite.change_y

            if self.mouse_hold:
                self.hook_sprite.change_y = HOOK_MOVEMENT_SPEED
            else:
                self.hook_sprite.change_y = -HOOK_MOVEMENT_SPEED

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_hold = True
            print(x, y)

    def on_mouse_release(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_hold = False


def main():
    """Main function"""
    window = FishingMiniGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
