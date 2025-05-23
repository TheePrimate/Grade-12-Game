# Main game loop goes here
from constants import *
from library import *


class GameView(arcade.View):
    """
    Main application class.
    """
    def __init__(self):
        # Call the parent class to set up the window
        super().__init__()
        self.bob_texture = arcade.load_texture("assets/funnypfp.png")
        self.bob_sprite = arcade.Sprite(self.bob_texture, scale = 0.02)
        self.bob_sprite.center_x = WINDOW_WIDTH / 2
        self.bob_sprite.center_y = WINDOW_HEIGHT / 2
        # Loop variables
        self.timer = 0
        self.day = 0
        self.money = 0
        self.label_timer_ticks = 0
        self.bobber_ticks = 0
        self.fish_ticks = 0
        self.missed_ticks = 0
        self.change_ticks = 0
        self.fish = random.randint(300, 1200)

        self.fishing_sprite_list = arcade.SpriteList()
        self.bob_sprite.center_x = WINDOW_WIDTH/2
        self.bob_sprite.center_y = WINDOW_HEIGHT/2
        self.money_quota = 100 + self.day * 10
        self.fish_is_ready = False
        self.bobber_animation = False
        self.show_quota_label = False
        self.is_fishing = False
        self.fishing_minigame_activate = False
        self.lose = False
        self.show_missed_label = False
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
        if self.show_missed_label:
            arcade.draw_text(f"You missed the fish", WINDOW_WIDTH/2-90, 350, arcade.color.GOLD)
        if self.show_quota_label:
            arcade.draw_text(f"Today's Quota: ${self.money_quota + 10}",WINDOW_WIDTH/2-180, 700, arcade.color.YELLOW,24)
        arcade.draw_text(f"Day: {self.day}", WINDOW_WIDTH/2-70, 50, arcade.color.RED, 20)
        # Code to draw other things will go here
        if self.is_fishing:
            self.bobber_animation = True
            arcade.draw_sprite(self.bob_sprite)

    def on_update(self, delta_time):

        self.timer += 1
        if self.timer % 400 == 0:
            self.trigger_mob()

        if self.show_missed_label:
            self.missed_ticks += 1
            if self.missed_ticks == 120:
                self.show_missed_label = False

        if self.show_quota_label:
            self.label_timer_ticks += 1
            if self.label_timer_ticks >= 240:
                self.show_quota_label = False
                self.label_timer_ticks = 0

        if self.bobber_animation:
            self.bobber_ticks += 1
            if self.bobber_ticks == self.fish:
                self.fish_is_ready = True
                self.fish_ticks += 1

        if self.fish_is_ready:
            self.bob_sprite.change_y = GRAVITY
            self.change_ticks += 1
            if self.change_ticks == 30:
                self.bob_sprite.change_y = -GRAVITY
                if self.change_ticks == 60:
                    self.change_ticks = 0
                    self.bob_sprite.change_y = 0
                    self.fish_ticks = False




    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.SPACE:
            print(self.timer)
            print(self.day)
            print(self.show_quota_label)
            print(self.money_quota)
            print(self.fish)
            print(self.bob_sprite.change_y )

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        pass

    def on_mouse_press(self, x, y, button, modifiers):
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
        print('The baddies are here')
        self.day += 1
        self.show_quota_label = True
        self.timer = 0



class GameStartView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("assets/funnypfp.png")

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
        self.texture = arcade.load_texture("assets/immortal jellyfish.png")

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
