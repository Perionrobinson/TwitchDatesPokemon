# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image right placeholder_gator = "assets/portraits/placeholder_generic.png"
image right placeholder_xatu = "assets/portraits/placeholder_generic.png"
image right placeholder_katie = "assets/portraits/placeholder_generic.png"
# Declare characters used by this game.
define es = Character('Burrito', color="#c8ffc8")
define bj = Character('Bird Jesus', color="#a8afc8")
define kt = Character('Katie', color="#00afc8")


# The game starts here.
label start:
    show right placeholder_gator at right
    "<<Man, this guy looks so intimidating... oh no, is he looking at me?!>>"
    show right placeholder_katie at right
    kt "Kyaaaaah!!! I'm so sorry... I DRAGONBREATH when I get nervous..."
    show right placeholder_xatu at right
    es "Oh... S-Senpai..."
    return
