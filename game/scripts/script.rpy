# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image splash_image = "assets/backgrounds/start.png"
# eg. image eileen happy = "eileen_happy.png"
image rj = "assets/portraits/rj.png"
image right placeholder_gator = "assets/portraits/placeholder_generic.png"
image right placeholder_xatu = "assets/portraits/placeholder_generic.png"
image katie = "assets/portraits/katie.png"
image atv = "assets/portraits/atv.png"
image abby = "assets/portraits/abby.png"
image digrat = "assets/portraits/placeholder_digrat.jpg"
image snake = "assets/portraits/snake.png"
image placeholder_lunch = "assets/backgrounds/placeholder_lunchroom.jpg"
image letter_map = "assets/backgrounds/letter_map.png"
image outside = "assets/backgrounds/outside.jpg"
#image train_back = ""
#image rj_char_pan = ""
#image letter = ""
#image rj_dorm = ""
# Declare characters used by this game.
define rj = Character('Burrito', color="#c8ffc8")
define kt = Character('Katie', color="#00afc8")
define atv = Character('ATV', color="#550000")
define dr = Character('Digrat', color="#AA66AA")
define gy = Character('Gyra', color="4455CC")
define bj = Character('BJ', color="777777")
define aj = Character('AJ', color="777777")
define ar = Character('Air', color="0000AA")
define br = Character('Brian', color="777777")
define fz = Character('Fonz', color="777777")
define ab = Character('Abby', color="AA0000")
define lg = Character('Gator', color="777777")
define ss = Character('Solid Snake', color="777777")
define fl = Character('Flareon', color="AA0000")

label splashscreen:
    show splash_image
    $ renpy.pause()
    return

# The game starts here.
label start:
    stop music
    $ day = Day()
    
    call introduction

    while day.dayNum <= 30:
        
        #Say what day it is.
        show rj
        "It was [day.dayString]"

        "We had classes in the morning."

        scene placeholder_lunch
        if day.dayNum == 1:
          call day_1_lunch
        else:
          "Lunch went by like it always does..."
        scene
  

        show rj
        "Then we had afternoon classes, and then I went home and went to bed."      
        #Call anything that happens prior to the day starting. ie. Day planners
        
        
        # Call anything that happens after the day. ie. Day summaries

        if day.weekdayNum == 5:
            "Another week has come and gone."
        
        # Increment to the next day.
        $ day.nextDay()
        
    
    "The game has ended. Time has run out."
    
    return

