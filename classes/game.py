from ninja import Ninja
from pirate import Pirate

# Character Creation
ninja_jack = Ninja("Ninja Jack")
Pirate_black = Pirate("black beard")
Pirate_blue = Pirate("blue beard")

# Enter Arena
ninja_jack.enter_arena()
Pirate_black.enter_arena()
Pirate_blue.enter_arena()

# Turn 1
ninja_jack.special_attack(Pirate_black)
Pirate_black.show_health()

# Turn 2
ninja_jack.attack(Pirate_blue)
Pirate_blue.show_health()

# Turn 3
Pirate_black.respawn()
Pirate_black.show_health()
Pirate_blue.regain_health()
Pirate_blue.show_health()

# Turn 5
Pirate_blue.attack(ninja_jack).cannon_attack(ninja_jack)
ninja_jack.show_health()

