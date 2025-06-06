import arcade.color

from library import *

"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""

WINDOW_TITLE = "Starting Template"


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.AMAZON
        self.fish = "mine"
        self.mineX = 500
        self.mineY = 530
        self.handX = 500
        self.handY = 340
        self.hand_vel = 5
        self.san_der = 0
        self.sanity = 459
        self.death = False
        self.san_accel = 0
        self.blackout = 0

        # Setup mine sprites
        self.mine_list = arcade.SpriteList()

        self.mine_texture = arcade.load_texture("assets/naval_mine.png")
        self.mine_sprite = arcade.Sprite(self.mine_texture, center_x=self.mineX, center_y=self.mineY)
        self.mine_list.append(self.mine_sprite)
        self.sanity_bar_texture = arcade.load_texture("assets/SanityBar.png")
        self.sanity_bar_sprite = arcade.Sprite(self.sanity_bar_texture, center_x=FISHING_MINIGAME_X,
                                               center_y=FISHING_MINIGAME_Y)
        self.mine_list.append(self.sanity_bar_sprite)
        self.hand_texture = arcade.load_texture("assets/hand.png")
        self.hand_sprite = arcade.Sprite(self.hand_texture, center_x=self.handX, center_y=self.handY)
        self.mine_list.append(self.hand_sprite)
        self.insanity_texture = arcade.load_texture("assets/insanity.png")
        self.insanity_sprite = arcade.Sprite(self.insanity_texture, center_x=WINDOW_WIDTH/2, center_y=WINDOW_HEIGHT/2
                                             , alpha=100)
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """Assign values to all variables"""
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        if self.fish == "mine":
            self.mine_list.draw(pixelated=True)
            arcade.draw_lrbt_rectangle_filled(103, 165.4, 219, 219+self.sanity,
                                              arcade.color.AIR_SUPERIORITY_BLUE)

            # Draw insanity blackout
            arcade.draw_lrbt_rectangle_filled(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, color=(0, 0, 0, self.blackout))

    def on_update(self, delta_time):
        # If the naval mine mini-game is engaged execute the following
        if self.fish == "mine":
            # Oscillate hand
            if self.hand_sprite.center_x <= 300:
                self.san_der = True
                self.hand_vel = 0
            elif self.hand_sprite.center_x >= 700:
                self.san_der = False
                self.hand_vel = 0
            if self.san_der:
                self.hand_vel += 1 + self.san_accel
            if not self.san_der:
                self.hand_vel -= 1 + self.san_accel

            self.hand_sprite.center_x += self.hand_vel

            # Sanity
            self.sanity -= 0.5
            self.san_accel += 0.005
            if self.blackout < 254:
                self.blackout += 0.3
            self.insanity_sprite.alpha = self.sanity / 4.59

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        print(x, y)
        if self.fish == "mine":
            if 300 < self.handX < 400:
                print("Bomb Disarmed")
                self.fish = "Disarmed"
            elif 400 < self.handX < 450 or 200 < self.handX < 250 or 450 < self.handX < 500:
                self.death = True
                self.sanity = 0

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and set up the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
