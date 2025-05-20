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
       self.beer_texture = arcade.load_texture("assets/funnypfp.png")
       self.beer_sprite = arcade.Sprite(self.beer_texture, scale = 0.05)
       self.timer = 0
       self.day = 0
       self.money = 0
       self.lose = False
       self.label_timer_ticks = 0
       self.beer_sprite.center_x = WINDOW_WIDTH/2
       self.beer_sprite.center_y = WINDOW_HEIGHT/2
       self.money_quota = 100 + self.day * 20


       self.physics_engine = arcade.PhysicsEngineSimple(
           self.beer_sprite)
       self.show_quota_label = False




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
           arcade.draw_text(
               f"Tomorrow's Quota: ${self.money_quota + 20}",
               200, 300,
               arcade.color.YELLOW,
               24
           )
       # Code to draw other things will go here
       arcade.draw_sprite(self.beer_sprite)


   def on_update(self, delta_time):
       self.physics_engine.update()
       if self.beer_sprite.center_y > 40:
           self.beer_sprite.center_y += GRAVITY
       self.timer += 1
       if self.timer % 1000 == 0:
           self.trigger_mob()


       if self.show_quota_label:
           self.label_timer_ticks += 1
           if self.label_timer_ticks >= 240:
               self.show_quota_label = False
               self.label_timer_ticks = 0


   def on_key_press(self, key, modifiers):
       """Called whenever a key is pressed."""


       if key == arcade.key.UP or key == arcade.key.W:
           self.beer_sprite.change_y = PLAYER_MOVEMENT_SPEED
       elif key == arcade.key.DOWN or key == arcade.key.S:
           self.beer_sprite.change_y = -PLAYER_MOVEMENT_SPEED
       elif key == arcade.key.LEFT or key == arcade.key.A:
           self.beer_sprite.change_x = -PLAYER_MOVEMENT_SPEED
       elif key == arcade.key.RIGHT or key == arcade.key.D:
           self.beer_sprite.change_x = PLAYER_MOVEMENT_SPEED
       elif key == arcade.key.SPACE:
           print(self.timer)
           print(self.day)
           print(self.show_quota_label)
           print(self.money_quota)


   def on_key_release(self, key, modifiers):
       """Called whenever a key is released."""


       if key == arcade.key.UP or key == arcade.key.W:
           self.beer_sprite.change_y = 0
       elif key == arcade.key.DOWN or key == arcade.key.S:
           self.beer_sprite.change_y = 0
       elif key == arcade.key.LEFT or key == arcade.key.A:
           self.beer_sprite.change_x = 0
       elif key == arcade.key.RIGHT or key == arcade.key.D:
           self.beer_sprite.change_x = 0


   def trigger_mob(self):
       print('The baddies are here')
       self.day += 1
       self.money_quota = 100 + (self.day - 1) * 20
       self.show_quota_label = True
       self.timer = 0




def main():
   """Main function"""
   window = GameView()
   window.setup()
   arcade.run()




if __name__ == "__main__":
   main()

