label introduction:
    
    scene black
    
    show burrito at left with fade
    show burrito at left with vpunch
    
    burrito "Zzzzz…"
    
    show burrito at left with vpunch
    
    #play sound "train.mp3"
    
    burrito "...Zzzzzz..."
    show burrito at left with vpunch
    #louder train
    
    burrito "Zzzzz…"
    
    'Announcer' "Next stop: Twitch Academy. Next stop: Twitch Academy."
    
    show burrito at left with vpunch
    burrito "….Zzzzzhngh?"
    #show train_back
    
    #make burrito opaque
    hide burrito
    show train_text at top
    pause
    #play sound "ding_dong.mp3"
    hide train_text

    'Announcer' "Arriving at: Twitch Academy."
    
    #show burrito_char_pan
    show burrito
    burrito "...it's my stop!"
    
    #hide burrito_char_pan
    
    #play sound "door_opening.mp3"
    scene outside
    
    "The station is rather empty. I remember that the station actually leads into the school grounds, so my dorm should be nearby. I want to get settled in as quickly as possible."
    "Let’s see… where did I put that map?"
    " "
    "...hm? Oh, there’s a note from mom!"
    
    #play sound "ruffle_paper"
    #scene letter
    
    'Letter' "Dear Burrito,"
    
    show burrito at left #sighing
    
    burrito "She still uses that nickname…"
    
    hide burrito
    
    'Letter' "'Hope you have a wonderful first day at school! Your father and I are so proud of you! We know you'll do the best you can, whatever you choose to do."
    'Letter' "On the back of this letter is a map to help you find your way from the train station. (Your father made it, so it might be a good idea to just buy your own) Take care!"
    'Letter' "P.S. There's a surprise waiting for you in your new room. Hope it 'spices' things up!'"
    
    show burrito at left #frowning
    
    burrito "Dad made a map? This can’t be good."
    
    show letter_map at right
    
    #need slow text
    burrito "Oh. Uh… I think I go this way? Or maybe this way? Um…"
    
    hide letter_map
    #some kind of transition?
    
    #show burrito_relieved
    burrito "Finally!"
    
    "As I make my way to the dorms, I can hear different conversations going on."
    "Some talked about that popular sport Ultraball. I also heard something about a group called the 'A Team'. Could it be some special team from the school?"
    "I guess I'll have to talk to my classmates to find out more."
    
    #show burrito_yawn
    burrito "*yawn*"
    #show burrito
    
    burrito "For now, I need to get to the dorms."
    
    hide burrito
    #show burrito_dorm
    
    "I enter my dorm. Looks like my roommate is already here, but they're wrapped head to toe in blankets. I better try to not wake them up."
    "I see my luggage is already on my bed, and there's even a package on top of it."
    
    burrito "I Guess this is the surprise that mom mentioned?"
    
    'Letter' "Burrito,"
    'Letter' "Inside is a special treat; it’s one of your favorites! There should be enough in here to last you the rest of the school year. Remember to keep it cold!"
    'Letter' "Love, Mom."
    
    burrito "Is it... No way! Aha! It is! Mom's special home-made salsa!"
    
    "This is definitely going on my lunch tomorrow. And the day after. And the day after. And the day after…"
    "I slept on the train, but I'm still dead tired from the trip here. My bed looks really comfy right now…"
    
    burrito "It's REALLY...comfy…"
    
    #show burrito_close_eyes
    
    "Really... *yawn* REALLY comfy…"
    return
