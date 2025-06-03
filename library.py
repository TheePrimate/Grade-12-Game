import arcade
import random
from constants import *

<<<<<<< Updated upstream
# Dollars, difficulty, sprite name
'''''
=======
# Dollars, lower-bound difficulty, higher-bound difficulty, time limit, sprite name

>>>>>>> Stashed changes
fish_data = {
    "Northern Pike": [100, DIFFICULTY_1_LOW, DIFFICULTY_1_HIGH, 20, "assets/arbitrary_asset.png"],
    "Cod": [150, DIFFICULTY_1_LOW, DIFFICULTY_2_HIGH, 20, "assets/cod.png"],
    "Rainbow Trout": [200, DIFFICULTY_1_LOW, DIFFICULTY_3_HIGH, "assets/arbitrary_asset.png"],
    "Sockeye Salmon": [250, DIFFICULTY_4_LOW, DIFFICULTY_4_HIGH, 20, "assets/sockeye.png"],
    "Snoek": [1500, DIFFICULTY_5_LOW, DIFFICULTY_5_HIGH, 20, "assets/snoek.png"],
    "Marlin": [4800, DIFFICULTY_6_LOW, DIFFICULTY_5_HIGH, "assets/marlin.png"],
    "Bluefin Tuna": [7350, DIFFICULTY_7_LOW, DIFFICULTY_5_HIGH, 20, "assets/bluefin_tuna"],
    "Dumbo Octopus": [99999, DIFFICULTY_7_LOW, DIFFICULTY_8_HIGH, 20, "assets/arbitrary_asset.png"],
    "Immortal Jellyfish": [0.3, DIFFICULTY_7_LOW, DIFFICULTY_9_HIGH, 20, "assets/arbitrary_asset.png"],
    "Ancient Mariner's Albatross": [553000, DIFFICULTY_10, DIFFICULTY_10, 20, "assets/albatross.png"],
    "Naval Bomb": [10000, DIFFICULTY_5_LOW, DIFFICULTY_5_HIGH, 20, "assets/arbitrary_asset.png"]
}
'''''