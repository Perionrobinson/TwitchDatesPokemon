# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image left placeholder_rj = "assets/portraits/placeholder_generic.png"
image right placeholder_gator = "assets/portraits/placeholder_generic.png"
image right placeholder_xatu = "assets/portraits/placeholder_generic.png"
image right placeholder_katie = "assets/portraits/placeholder_generic.png"
image placeholder_lunch = "assets/backgrounds/placeholder_lunchroom.jpg"
# Declare characters used by this game.
define es = Character('Burrito', color="#c8ffc8")
define bj = Character('Bird Jesus', color="#a8afc8")
define kt = Character('Katie', color="#00afc8")


# The game starts here.
label start:
    
    $ day = Day()

    while day.dayNum <= 30:
        
        #Say what day it is.
        show left placeholder_rj
        "It was [day.dayString]"

        "We had classes in the morning."

        scene placeholder_lunch
        "Lunch went by like it always does..."
        scene
  

        show left placeholder_rj
        "Then we had afternoon classes, and then I went home and went to bed."      
        #Call anything that happens prior to the day starting. ie. Day planners
        
        
        # Call anything that happens after the day. ie. Day summaries

        if day.weekdayNum == 5:
            "Another week has come and gone."
        
        # Increment to the next day.
        $ day.nextDay()
        
    
    "The game has ended. Time has run out."
    
    return
