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
    
    "The station is rather empty... Let’s see... where did I put that map?"
    "...hm? What's this?"
    
    #play sound "ruffle_paper"
    #scene letter
    
    hide burrito
    
    'Letter' "'Hope you have a wonderful first day at school! Your mother and I are so proud of you! We know you'll do the best you can, whatever you choose to do."
    'Letter' "'Also, I spilled water all over your map, but don't worry  - I'm sure the school hasn't changed much since I was there, so I drew you a new one from memory!'"
    
    show burrito at left #frowning
    show letter_map at topright
    pause
    
    #need slow text
    burrito "... I don't even know what to say about this."
    hide burrito
    hide letter_map
    #some kind of transition?
    
    "I eventually manage to find my way to registration, where they gave me an ID and a room key. I ended up being in a room by myself, with the luggage my parents mailed ahead of me waiting on the bed. The room is small, but its cozy, and as much as I'd like to explore the school, I've got class first thing in the morning and the bed is so inviting. I don't even bother to unpack, and before I know it it the bright morning sun is shining on my face, waking me up to a new day."
    return
