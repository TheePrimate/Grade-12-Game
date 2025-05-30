# Main game loop goes here

# from constants import *
from library import *


class GameView(arcade.View):
    """
    Main application class.
    """
    def __init__(self):
        # Call the parent class to set up the window
        super().__init__()
        # Loads the texture to become sprites of the bob, and the background
        self.bob_texture = arcade.load_texture("assets/arbitrary_asset.png")
        self.background_texture = arcade.load_texture("assets/Hamlet.png")
        self.background_sprite = arcade.Sprite(self.background_texture, scale = 1)
        self.bob_sprite = arcade.Sprite(self.bob_texture, scale = 2)
        # Loop variables
        # The time in a day
        self.timer = 0
        # Which day it is
        self.day = 0
        # How much money we have
        self.money = 0
        # All the mini timers that are needed to keep track of certain variables
        # This timer counts how long a label should last on the screen for
        self.label_timer_ticks = 0
        # This timer counts how long it should take before the bobber starts to move
        self.bobber_ticks = 0
        # This timer gives us how long we have after the bobber bobs and we have to fish
        self.fish_ticks = 0
        # This timer counts how long we should keep the missed fish label for
        self.missed_ticks = 0
        # This timer is for the bobbing animation to happen
        self.change_ticks = 0
        # This shows how many seconds are needed before a fish pops up
        self.fish = random.randint(300, 1200)
        # Sets the position of the background image
        self.background_sprite.center_x = WINDOW_WIDTH / 2
        self.background_sprite.center_y = WINDOW_HEIGHT / 2
        # Sets the position of the bobber sprite
        self.bob_sprite.center_x = 1100
        self.bob_sprite.center_y = 100
        # The money quota for the first day
        self.money_quota = 100
        # Lets us know when the bobber sprite should start bobbing
        self.fish_is_ready = False
        # Lets us know when the bobber gets thrown into the water
        self.bobber_animation = False
        # Lets us show the days quota for only a certain amount of time
        self.show_quota_label = False
        # Lets us know when the person starts fishing, as soon as the mouse is clicked
        self.is_fishing = False
        # Once you successfully click when the bobber moves, the minigame shall activate
        self.fishing_minigame_activate = False
        # Lets us know once we lose the game, not enough money to meet the daily quota
        self.lose = False
        # Variable that lets us show a missed fish label for a few seconds
        self.show_missed_label = False
        # Lets us know when the main loop is going on and not any minigames
        self.main_loop = True
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
        # Draw the background
        arcade.draw_sprite(self.background_sprite)
        # Draws the missed fish text once we miss a fish
        if self.show_missed_label:
            arcade.draw_text(f"You missed the fish", WINDOW_WIDTH/2-90, 350, arcade.color.GOLD)
        # Draws the quota every new day
        if self.show_quota_label:
            arcade.draw_text(f"Today's Quota: ${self.money_quota}",WINDOW_WIDTH/2-180, 700, arcade.color.YELLOW,24)
        # Shows what day it is at the bottom of the screen
        arcade.draw_text(f"Day: {self.day}", WINDOW_WIDTH/2-70, 50, arcade.color.GREEN, 30)
        # Once the fishing starts, draw the bobber and start counting the time before the bobber should start moving
        if self.is_fishing:
            self.bobber_animation = True
            arcade.draw_sprite(self.bob_sprite)



    def on_update(self, delta_time):
        # Tick timer, every tick add one there are 60 ticks in a second
        self.timer += 1
        # Every 5 minutes or 18000 ticks trigger a new day with the trigger mob function
        if self.timer % 400 == 0:
            self.trigger_mob()
        # If you miss a fish, this will allow a label to be drawn for only 2 seconds
        if self.show_missed_label:
            self.missed_ticks += 1
            if self.missed_ticks == 120:
                self.show_missed_label = False
        # Shows a quota at the start of a new day for 4 seconds
        if self.show_quota_label:
            self.label_timer_ticks += 1
            if self.label_timer_ticks >= 240:
                self.show_quota_label = False
                self.label_timer_ticks = 0
        # Counts how many ticks the bobber has been in the water for, if it matches self.fish,
        # Start the bobbing animation as a fish is on the line and start a counter for
        # how many seconds you have to catch the fish
        if self.bobber_animation:
            self.bobber_ticks += 1
            if self.bobber_ticks == self.fish:
                self.fish_is_ready = True
                self.fish_ticks += 1
                self.bobber_animation = False
                self.bobber_ticks = 0
        # Once the fish is on the line, start a timer so the bobber can move, after 3 seconds
        if self.fish_is_ready:
            self.bob_sprite.center_y = 50
            self.change_ticks += 1
            if self.change_ticks == 45:
                self.bob_sprite.center_y = 150
                if self.change_ticks == 90:
                    self.bob_sprite.center_y = 100
                    if self.change_ticks == 180:
                        self.change_ticks = 0
                        self.fish_ticks = 0
                        self.is_fishing = False
                        self.fish_is_ready = False




    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.SPACE:
            print(self.timer)
            print(self.fish)
            print(self.is_fishing)
            print(self.bobber_ticks)

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        if self.main_loop:
            self.main_loop = False
            self.is_fishing = True
        if self.fish_is_ready:
            if self.fish_ticks < 180:
                self.fishing_minigame_activate = True
                self.bobber_animation = False
                self.fish_is_ready = False
            else:
                self.show_missed_label = True
                self.bobber_animation = False
                self.fish_is_ready = False



    def trigger_mob(self):
        # Every new day the quota goes up by 10$ and the counter increases while the timer resets
        print('The baddies are here')
        self.money_quota += 10
        self.day += 1
        self.show_quota_label = True
        self.timer = 0



class GameStartView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("assets/arbitrary_asset.png")

    def setup(self):
        pass

    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture, rect=arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        arcade.draw_text("Start Screen", 100, 300, arcade.color.WHITE, 30)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> bool | None:
        game_view = GameView()
        self.window.show_view(game_view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            game_view = RulesView()
            self.window.show_view(game_view)


class RulesView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("assets/arbitrary_asset.png")

    def setup(self):
        pass

    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture, rect=arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        arcade.draw_text("Rules Screen", 100, 300, arcade.color.WHITE, 30)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> bool | None:
        game_view = GameView()
        self.window.show_view(game_view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            game_view = GameStartView()
            self.window.show_view(game_view)

def main():
   """Main function"""
   window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
   start_view = GameStartView()
   window.show_view(start_view)
   start_view.setup()
   arcade.run()

if __name__ == "__main__":
   main()
