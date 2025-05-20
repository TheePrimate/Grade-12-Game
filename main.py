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
       self.beer_texture = arcade.load_texture("assets/funnypfp.png")
       self.beer_sprite = arcade.Sprite(self.beer_texture, scale = 0.05)
       self.timer = 0
       self.day = 0
       self.money = 0
       self.lose = False
       self.label_timer_ticks = 0
       self.beer_sprite.center_x = WINDOW_WIDTH/2
       self.beer_sprite.center_y = WINDOW_HEIGHT/2
       self.money_quota = 100 + self.day * 10
       self.physics_engine = arcade.PhysicsEngineSimple(
           self.beer_sprite)
       self.show_quota_label = False
       self.fishing_minigame_activate = False

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
       if self.show_quota_label:
           arcade.draw_text(f"Today's Quota: ${self.money_quota + 10}",WINDOW_WIDTH/2, 300, arcade.color.YELLOW,24,align="center")
       arcade.draw_text(f"Day: {self.day}", WINDOW_WIDTH/2, 50, arcade.color.RED, 20, align='center')
       # Code to draw other things will go here



   def on_update(self, delta_time):
       self.physics_engine.update()
       if self.beer_sprite.center_y > 40:
           self.beer_sprite.center_y -= GRAVITY
       self.timer += 1
       if self.timer % 400 == 0:
           self.trigger_mob()

       if self.show_quota_label:
           self.label_timer_ticks += 1
           if self.label_timer_ticks >= 240:
               self.show_quota_label = False
               self.label_timer_ticks = 0


   def on_key_press(self, key, modifiers):
       """Called whenever a key is pressed."""
       if key == arcade.key.SPACE:
           print(self.timer)
           print(self.day)
           print(self.show_quota_label)
           print(self.money_quota)

   def on_key_release(self, key, modifiers):
       """Called whenever a key is released."""
       pass

   def on_mouse_press(self, x, y, button, modifiers):
       self.fishing_minigame_activate = True

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
