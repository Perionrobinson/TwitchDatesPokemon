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
image digrat = "assets/portraits/placeholder_generic.png"
image placeholder_lunch = "assets/backgrounds/placeholder_lunchroom.jpg"
# Declare characters used by this game.
define rj = Character('Burrito', color="#c8ffc8")
define bj = Character('Bird Jesus', color="#a8afc8")
define kt = Character('Katie', color="#00afc8")
define atv = Character('ATV', color="#550000")
define dr = Character('Digrat', color="#AA66AA")
define gy = Character('Gyra', color="4455CC")
define bj = Character('ABBA', color="777777")
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

    while day.dayNum <= 30:
        
        #Say what day it is.
        show rj
        "It was [day.dayString]"

        "We had classes in the morning."

        scene placeholder_lunch
        if day.dayNum == 1:
          call lunch_choice_1
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

label lunch_choice_1:
  "Then we all headed to lunch..."
  show rj at left
  rj "Wow, thats noisy. And so many people!"
  rj "Where am I supposed to sit?"
  gy "Hey, kid! Stop gawking and move along, you're holding up the line!"
  rj "Sorry!"
  rj "Aw shoot, where am I going to go!?"
  menu:
    "Table 1 - ABBA, AJ, Brian, Air":
      show rj at left
      ar "I’m just saying that you should get some fresh air sometimes!"
      aj "And I’m just saying if you looked at a book instead of a basketball, you wouldn’t need my notes every day."
      bj "Need to, no, but you’re easy to copy because you pretty much write them for us."
      aj "Well, I don’t need them."
      aj "Yeah, yeah, AJ the legendary, bound to be valedictorian while the rest of us actually enjoy life!"
      rj "Um...I’m sorry, is it okay if I sit here?"
      aj "And you are?"
      bj "The new transfer student. Burrito, right? Brian mentioned you."
      br "….."
      bj "We like to meet new people, even if they’re teeny tiny little ones like you."
      ar "And you are tiny, just like little bro Brian, huh?"
      br "….."
      aj "It’s never too early to start making it big, though."
      bj "When AJ’s right, he’s really right. That’s a good philosophy to have...so sure, Burrito, you can come sit with us."

      "The rest of lunch is pretty good. For the popular crowd, they’re all really nice, even if AJ is always serious and B.J. talks more than anyone else put together...Brian still never really said anything at all, though."
    "Table 2 - Gator, Abby, Fonz, Solid Snake":
      fz "And thats when she says-"
      ss "That she admires my Rock Hard Determination!"
      fz "She was certainly admiring some hard rocks, haha!"
      ss "Harha! ... Wait a minute, you're talking about my rock hard body that all the ladies love, right?"
      fz "Of course, of course! Hey, Abby, why no laugh? That was comedy gold, right there!"
      show abby at right
      ab "I swear you two get dumber by the day. Now, if you want to here something actually funny, let me tell you about-"
      hide abby
      lg "Hold up, Abs, guys. Looks like we got company. Can we help you, little guy?"
      rj "Well... uh... heh... I was, uh... wondering... if I could sit here?"
      fz "I dunno, kid, you look a bit scrawny. Nice color, though."
      ab "Aww, I think he's cute. We've got enough muscle bound oafs already anyway."
      lg "Have a seat, kid. kiddo. Now, Abby, where were you... "
      show abby at right
      ab "Right, right, so I'm in science class, and one of those creepy little oddish has somehow managed to get himself trapped in the vent chamber..."
      hide abby
      "Lunch was actually pretty good. I think I picked the right table. Those guys are pretty funny, and even though I didn't say much and they didn't say much to me, I got the feeling they'd be glad to have me sit with them again tomorrow."
    "Table 3 - ATV, Katie, Digrat":
      show atv at right
      atv "I got you THAT time!"
      hide atv
      show katie at right
      kt "One time out of, like, four!"
      hide katie
      show atv at right
      atv "One time’s all that I need to slay you, hah hah!"
      hide atv
      show katie at right
      kt "You are not half the superhero you THINK you are."
      hide katie
      show atv at right
      atv "That’s because I’m not a superhero, I’m a knight."
      hide atv
      show digrat at right
      dr "If you’re a knight...does that mean you fight for JUSTICE?"
      hide digrat
      show atv at right
      atv "And FREEDOM."
      rj "Does that include the freedom to...sit with you guys?"
      atv "Why yes, mysterious stranger, it does!"
      hide atv
      show digrat at right
      dr "I don’t think Burrito’s mysterious, he introduced himself in front of the whole class this morning.."
      hide digrat
      show katie at right
      kt "But that doesn’t tell us anything except that he just moved here! What about his hopes, his dreams, his secret past?!"
      rj "Um…"
      hide katie
      "The rest of lunch with them was really fun, even if it was pretty weird. They were really friendly, even if Digrat stole my utensils to make battlements for his castle, Katie kept asking me weird questions about my past and ATV never stopped being a knight, looking for more dragons to slay. "

    "Table 4 - Flareon":
      fl "…."
      rj "H...hi. Um, may I sit here?"
      fl "Why?"
      rj "I...need a place to sit? Because it’s...lunch, you know? And I like to eat my lunch sitting down, it makes food digest better than eating standing up…! Hah...hahahah…"
      rj "I am really bad at this around her."
      fl "Fine, go ahead and sit here."
      rj "Oh! Okay! Thanks!"
      rj "Wow, I didn’t think she’d say yes! Maybe I’m not as bad as I thought!"
      rj "She just...got up and moved to another empty table. Nevermind, I’m worse than I thought."
      br "It’s okay, she does that to everyone."
      rj "I’m starting to understand why she was sitting alone, I think. Anyway..."
      rj "Hi! It’s...Brian, right?"
      br "That’s me...just Brian. Do you mind if I sit with you?"
      rj "Not at all. I promise I won’t even get up and move tables!"
      "Brian and I had lunch together, just the two of us at that table. He talks a lot more when he’s not around his brother. It was really nice to have somebody to talk to!"

    "Sit Alone":
      "On second thought, it’s probably a better idea just to sit by myself on the first day. I don’t know enough about anyone yet…"
      br "Um, hello...it’s your first day, right?"
      rj "Hi! It’s...Brian, right?"
      br "That’s me...just Brian. Do you mind if I sit with you?"
      
      menu:
        "Go ahead":
          rj "Not at all. I promise I won’t even get up and move tables!"
          "Brian and I had lunch together, just the two of us at that table. He talks a lot more when he’s not around his brother. It was really nice to have somebody to talk to!"
        "I'd prefer to be alone":
          rj "Um, no thanks. I need some quiet to study."
          br "Okay. Sorry."
          "I couldn’t tell him how nervous I was to try and make friends with the little brother of the most popular person in school, not on my first day."
          "My first lunch at my new school was totally quiet after that and I was forced to ACTUALLY study. As lunches go, I hope tomorrow’s is better."
  return
