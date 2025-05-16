# Main game loop goes here

import arcade

# Constants
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_TITLE = "PLACEHOLDER"
PLAYER_MOVEMENT_SPEED = 30
GRAVITY = -1


class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, fullscreen=True)
        self.main_movement_texture = arcade.load_texture("assets/KaydenGameBarBeerAnimation.gif")
        self.main_movement_sprite = arcade.Sprite(self.main_movement_texture)
        self.main_movement_sprite.center_x = WINDOW_WIDTH/2
        self.main_movement_sprite.center_y = WINDOW_HEIGHT/2

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.main_movement_sprite)
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

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

        # Code to draw other things will go here
        arcade.draw_sprite(self.main_movement_sprite)

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.main_movement_sprite.change_y = GRAVITY

    def on_key_hold(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.main_movement_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.main_movement_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.main_movement_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.main_movement_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.main_movement_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.main_movement_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.main_movement_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.main_movement_sprite.change_x = 0


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()