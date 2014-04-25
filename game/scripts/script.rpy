# You can place the script of your game in this file.

# Backgrounds
image splash_image = "assets/backgrounds/start.png"
image bg black = Solid((0, 0, 0, 255))
image bg standard = Solid("#808080")
image placeholder_lunch = "assets/backgrounds/placeholder_lunchroom.jpg"
image outside = "assets/backgrounds/outside.jpg"

# Characters
image burrito = "assets/portraits/burrito.png"
image burrito_voiceover = im.Alpha("assets/portraits/burrito.png", 0.5)
image burrito normal = "assets/portraits/burrito.png"
image burrito confused = "assets/portraits/burrito.png"
image burrito smile = "assets/portraits/burrito.png"
image burrito sad = "assets/portraits/burrito.png"
image burrito friendly = "assets/portraits/burrito.png"
image burrito exasperated = "assets/portraits/burrito.png"
image burrito nervous = "assets/portraits/burrito.png"
image burrito flustered = "assets/portraits/burrito.png"
image burrito embarrassed = "assets/portraits/burrito.png"
image burrito happy = "assets/portraits/burrito.png"
image burrito surprised = "assets/portraits/burrito.png"
image burrito panic = "assets/portraits/burrito.png"
image burrito smirk = "assets/portraits/burrito.png"
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
image arc = "assets/portraits/placeholder_generic.png"
image arc normal = "assets/portraits/placeholder_generic.png"
image arc happy = "assets/portraits/placeholder_generic.png"
image arc annoyed = "assets/portraits/placeholder_generic.png"
image arc surprised = "assets/portraits/placeholder_generic.png"
image arc smiling = "assets/portraits/placeholder_generic.png"
image bj = "assets/portraits/placeholder_generic.png"
image bj normal = "assets/portraits/placeholder_generic.png"
image bj annoyed = "assets/portraits/placeholder_generic.png"
image bj sad = "assets/portraits/placeholder_generic.png"
image bj surprised = "assets/portraits/placeholder_generic.png"
image air normal = "assets/portraits/placeholder_generic.png"
image air surprised = "assets/portraits/placeholder_generic.png"
image air happy = "assets/portraits/placeholder_generic.png"
image brian = "assets/portraits/placeholder_generic.png"
image brian normal = "assets/portraits/placeholder_generic.png"
image brian surprised = "assets/portraits/placeholder_generic.png"
image flareon = "assets/portraits/placeholder_generic.png"
image flareon small smile = "assets/portraits/placeholder_generic.png"

#special text and images
image letter_map = "assets/backgrounds/letter_map.png"
image train_text = Text("...oh yeah, I’m on the train. Guess I fell asleep on the way here.\nFunny how much moving can tire you out.\nThe announcer's voice... ah. My next stop: Twitch Academy.\nI keep repeating those two words in my head, but it still doesn't feel real. Ever since I was small I'd heard about how incredible this school was. High standards, prestigious teachers, and plenty of students who went on to illustrious careers!\nEverything a star school should have.\nI was a lucky enough Espeon that now I was going to be one of those students!\n'Espeon'...\nEven that is new to me. I wanted to be an Espeon for the longest time, but it was taking me forever to evolve. My old teachers asked, why couldn't I just be like all the other Eevees and use a stone to evolve? But... I just couldn't. Instead, I committed myself to what I wanted, and now here I am - an Espeon. The Sun Pokémon. Symbol of new days and new beginnings!\nNow I’ll have to prove myself at Twitch Academy. I wonder what my classmates will be like... I hope I can make some friends!")   
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
define arc = Character('AJ', color="777777")
define uk = Character('???',color="#FFFFFF")
define xa = Character('Will',color="#84EFE5")
define mw = Character('Ms. Whitney', color= "#FFAA99")
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
    $ relationships = { 'atv': 0,
                        'katie': 0,
                        'gator': 0,
                        'snake': 0,
                        'brian': 0,
                        'bj': 0,
                        'flareon': 0,
                        'arc': 0,
                        'air': 0
                      }
    $ introduced = {    'atv': False,
                        'katie': False,
                        'gator': False,
                        'snake': False,
                        'brian': False,
                        'bj': False,
                        'flareon': False,
                        'arc': False,
                        'air': False
                      }
                      

    stop music
    $ day = Day()
    
    call introduction

    while day.dayNum <= 30:
        
        #Say what day it is.
        "It was [day.dayString]"

        "We had classes in the morning."
        if day.dayNum == 1:
           call dorm_scene_1
           call class_scene_1
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

