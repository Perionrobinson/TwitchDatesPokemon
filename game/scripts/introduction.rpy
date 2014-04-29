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
    
    hide burrito

    show burrito_voiceover at left

    "...oh yeah, I’m… I’m in the train."
    "Guess I fell asleep on the way here. Funny how moving can really tire you out."
    "The announcer's voice reminds me of my destination."
    "Twitch Academy."
    "Twitch Academy. Twitch. Academy."
    "I keep repeating the words in my head but it doesn't make it seem any more real."
    "Ever since I was a young Eevee, everyone spoke of how incredible a school it is."
    "The high standards, the prestigious teachers - and past students who went on to illustrious careers! -, everything a star school should have."
    "And now, as an Espeon, I will be one of those students!... Hopefully."
    "Heh. 'Espeon'... Even that is new to me. For the longest time I knew I wanted to be an Espeon. It was taking me forever to evolve. So many of my old teachers suggested I just be like all the other Eevees and use a stone to evolve, but... I finally did it."
    "I’m an Espeon. The Sun Pokémon. Symbol of a new day! And a new beginning!"
    "And now I’ll have a chance to prove myself at Twitch Academy."
    "I wonder what my classmates will be like... I just hope I can make some friends."
    "Of course, I'll still need to keep my grades up."
    "But I can't focus too much on study or I won't have any friends!"
    "B-but if I slack off too much, I'll have bad grades, which could get me expelled!"
    "Oh, Arceus, I also need to work on my schedule, and make sure tha-!"

    #play sound "ding_dong.mp3"

    'Announcer' "Arriving at: Twitch Academy."
    
    #show burrito character panel

    show burrito at left
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
    
    show burrito frowning at left
    show letter_map at topright
    pause
    
    #slow text working!
    image conBurrito = Text("... I don't even know what to say about this.", slow=True)
    
    show conBurrito with Pause(3.0)
    $ renpy.pause()
    hide conBurrito
    
    hide burrito
    hide letter_map
    #some kind of transition?
    
    "I eventually manage to find my way to registration, where they gave me an ID and a room key. I ended up being in a room by myself, with the luggage my parents mailed ahead of me waiting on the bed. The room is small, but its cozy, and as much as I'd like to explore the school, I've got class first thing in the morning and the bed is so inviting. I don't even bother to unpack, and before I know it it the bright morning sun is shining on my face, waking me up to a new day."
    return
