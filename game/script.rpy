# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image placeholder_gator = "backgrounds/placeholder1.png"
image placeholder_xatu = "backgrounds/placeholder2.png"
image placeholder_katie = "backgrounds/placeholder3.png"
# Declare characters used by this game.
define es = Character('Burrito', color="#c8ffc8")
define bj = Character('Bird Jesus', color="#a8afc8")
define kt = Character('Katie', color="#00afc8")


# The game starts here.
label start:
    show placeholder_gator at top
    es "<<Man, this guy looks so intimidating... oh no, is he looking at me?!>>"
    show placeholder_katie at top
    kt "Kyaaaaah!!! I'm so sorry... I DRAGONBREATH when I get nervous..."
    show placeholder_xatu at top
    es "Oh... S-Senpai..."
    return
