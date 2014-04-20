# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image splash_image = "assets/backgrounds/start.png"
# eg. image eileen happy = "eileen_happy.png"
image burrito = "assets/portraits/burrito.png"
image burrito normal = "assets/portraits/burrito.png"
image burrito confused = "assets/portraits/burrito.png"
image burrito smile = "assets/portraits/burrito.png"
image burrito exasperated = "assets/portraits/burrito.png"
image right placeholder_gator = "assets/portraits/placeholder_generic.png"
image right placeholder_xatu = "assets/portraits/placeholder_generic.png"
image katie = "assets/portraits/katie.png"
image katie normal = "assets/portraits/katie.png"
image katie angry = "assets/portraits/katie.png"
image katie exasperated = "assets/portraits/katie.png"
image katie sad = "assets/portraits/katie.png"
image katie smile = "assets/portraits/katie.png"
image katie annoyed = "assets/portraits/katie.png"
image katie confused = "assets/portraits/katie.png"
image atv = "assets/portraits/atv.png"
image atv normal = "assets/portraits/atv.png"
image atv smile = "assets/portraits/katie.png"
image atv sad = "assets/portraits/atv.png"
image atv excited = "assets/portraits/atv.png"
image atv angry = "assets/portraits/atv.png"
image atv annoyed = "assets/portraits/atv.png"
image abby = "assets/portraits/abby.png"
image digrat = "assets/portraits/digrat_placeholder.jpg"
image digrat normal = "assets/portraits/digrat_placeholder.jpg"
image digrat smile = "assets/portraits/digrat_placeholder.jpg"
image digrat excited = "assets/portraits/digrat_placeholder.jpg"
image digrat sad = "assets/portraits/digrat_placeholder.jpg"
image digrat nervous = "assets/portraits/digrat_placeholder.jpg"
image snake = "assets/portraits/snake.png"
image placeholder_lunch = "assets/backgrounds/placeholder_lunchroom.jpg"
image letter_map = "assets/backgrounds/letter_map.png"
image outside = "assets/backgrounds/outside.jpg"
#special text
image train_text = Text("...oh yeah, I’m on the train. Guess I fell asleep on the way here.\nFunny how much moving can tire you out.\nThe announcer's voice... ah. My next stop: Twitch Academy.\nI keep repeating those two words in my head, but it still doesn't feel real. Ever since I was small I'd heard about how incredible this chsool was. High standards, prestigious teachers, and plenty of students who went on to illustrious careers!\nEverything a star school should have.\nI was a lucky enough Espeon that now I was going to be one of those students!\n'Espeon'...\nEven that is new to me. I wanted to be an Espeon for the longest time, but it was taking me forever to evolve. My old teachers asked, why couldn't I just be like all the other Eevees and use a stone to evolve? But... I just couldn't. Instead, I committed myself to what I wanted, and now here I am - an Espeon. The Sun Pokémon. Symbol of new days and new beginnings!\nNow I’ll have to prove myself at Twitch Academy. I wonder what my classmates will be like... I hope I can make some friends!")   
#image train_back = ""
#image burrito_char_pan = ""
#image letter = ""
#image burrito_dorm = ""
# Declare characters used by this game.
define burrito = Character('Burrito', color="#c8ffc8")
define katie = Character('Katie', color="#00afc8")
define atv = Character('ATV', color="#550000")
define digrat = Character('Digrat', color="#AA66AA")
define gyra = Character('Gyra', color="4455CC")
define bj = Character('BJ', color="777777")
define aj = Character('AJ', color="777777")
define air = Character('Air', color="0000AA")
define brian = Character('Brian', color="777777")
define fonz = Character('Fonz', color="777777")
define abby = Character('Abby', color="AA0000")
define gator = Character('Gator', color="777777")
define snake = Character('Solid Snake', color="777777")
define flareon = Character('Flareon', color="AA0000")

#relationship_tracking
label splashscreen:
    show splash_image
    $ renpy.pause()
    return

# The game starts here.
label start:
    $ relationships = {'atv': 0,
                   'katie': 0,
                   'gator': 0,
                   'snake': 0,
                   'brian': 0,
                   'bj': 0,
                   'flareon': 0
                  }

    stop music
    $ day = Day()
    
    call introduction

    while day.dayNum <= 30:
        
        #Say what day it is.
        show burrito
        "It was [day.dayString]"

        "We had classes in the morning."

        scene placeholder_lunch
        if day.dayNum == 1:
          call day_1_lunch
        else:
          "Lunch went by like it always does..."
        scene
  

        show burrito
        "Then we had afternoon classes, and I had to decide what I was going to do after school."
        if day.dayNum == 1:
          call day_1_after_school_choice
        elif day.dayNum == 2:
          call day_2_after_school_choice
        else:
          "I decided to just go home today, spend some time relaxing, then go to bed."      

        if day.weekdayNum == 5:
            "Another week has come and gone."
        
        # Increment to the next day.
        $ day.nextDay()
        
    
    "The game has ended. Time has run out."
    
    return

