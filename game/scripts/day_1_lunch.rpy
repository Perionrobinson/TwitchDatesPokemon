label day_1_lunch:
  "I probably should have gotten here earlier, this cafeteria is pretty packed! At least I don’t have to wait in line, since I brought lunch today."
  "It’s definitely better than anything that a school cafeteria could ever prepare, anyway. Super-ultra-deluxe Cheri burritos with Mom’s special homemade salsa!"
  "Hmm."
  "There’s seats by Abba, that class rep, who is sitting with Arc and Brian from class, as well as another Pokemon I don’t really know."
  "ATV is sharing a table with Katie and a Raticate; he seemed a bit strange during class but I’m sure he and his friends are interesting! I wonder why they’re sitting together, though. Don’t they hate each other?"
  "There’s a table of a bunch of big Pokemon including Fonz and Gator, as well as a Steelix and a female Charmeleon. I mean, I guess Gator and Fonz are funny... in a way."
  "But who is that Flareon sitting alone? Most Eevee where I came from had plenty of friends, especially after they evolved."
  "Hmm, which seat should I take..."

  menu:
    "Table 1; Abba, Arc, Brian, ??? (Lapras)":
      call day_1_lunch_table_1
    "Table 2; ATV, Katie, ???(Raticate)":
      # call day_1_lunch_table_2
      $ do_nothing_yet = True
    "Table 3; Lazor, Fonz, ??? (Steelix), ??? (Charmeleon)":
      # call day_1_lunch_table_3
      $ do_nothing_yet = True
    "Table 4; ??? (Flareon)":
      call day_1_lunch_table_4
      $ do_nothing_yet = True
    "Sit alone":
      # call day_1_lunch_table_5
      $ do_nothing_yet = True
  return

label day_1_lunch_table_1:
  $ relationships["bj"]+=3
  $ relationships["brian"]+=3
  $ relationships["arc"]+=3
  $ relationships["air"]+=3
  "I think I’ll sit at Abba’s table. He helped me out with my enrollment form earlier, after all."
  show burrito nervous at left
  burrito "H-hey, Abba, mind if I sit here?"
  show bj at right
  bj "Hm? Oh, the new student!"
  bj "I suppose we can make room for you on your first day."
  if (late_on_first_day):
    show bj annoyed
    bj "However, being tardy to class is not a good start. This is still your first day, but I hope you won’t repeat the same offense later on."
    show burrito embarrassed
    burrito "R-right, I’ll do my best to be on time."
  show bj normal
  show burrito normal
  bj "The office is still dealing with your enrollment form. They probably won’t be done until the end of the day."
  bj "For now, we’ll just call you by your official name."
  show burrito surprised
  burrito "Ehh? But..."
  show bj at center
  bj "Anyway, let me introduce you. Everyone, this is Burrito, a new student at Twitch Academy."
  show burrito normal
  burrito "Hello everyone, nice to meet you."

  show arc normal at right
  bj "Arc is a close friend of mine, and vice-president of the student council. I assume you met him earlier in Ms. Whitney’s class."
  arc "Hey, I meant to ask you earlier-- Why did you want to come to Twitch Academy?"
  show burrito nervous
  "W-what? What’s with that question all of a sudden…? I know that Zapdos naturally look a bit intimidating, but when he talks like that it kinda scares me for real..."
  burrito "W-well, I was able to get a scholarship here..."
  show arc surprised
  arc "...really now? They have scholarships for this place? Wow, you learn something new every day…"
  show bj sad
  bj "Arc, not everyone is so privileged as we are. You'd do well to remember that now and again."
  show burrito normal
  show bj normal
  show arc normal
  arc "...whatever."
  "Are scholarships really that surprising? I mean, this is an academy, not just some public school, right?"
  "What’s the deal with this Arc guy, anyway? He doesn’t seem like the type of ‘mon to hang out with someone as respectable as Abba, let alone be the vice-president of the student council..."
  hide arc

  show air normal at right
  bj "And this is Air, one of the best Ultraball players here."
  air "Thanks, bro. Just doin’ my thing."

  # Air character panel appears, when it exists
  "CHARACTER PANEL PLACEHOLDER"
  $ introduced["air"] = True

  show air happy
  air "You should come watch a game sometime. It’s really intense."
  burrito "Thanks for the invite. That sounds interesting."
  hide air

  show brian at right
  bj "And last, but certainly not least, is my younger brother, Brian."

  # Brian character panel appears, when it exists
  "CHARACTER PANEL PLACEHOLDER"
  $ introduced["brian"] = True

  show burrito happy
  burrito "Ah… I didn’t realize you were related! But it’s pretty obvious now that I see you two together."
  brian "Y-yeah, we get that a lot."
  brian "So, how are you enjoying it here so far?"
  show burrito normal 
  burrito "Well, the campus is much bigger than the schools I’m used to."
  burrito "It’ll take me a while just to figure out where everything is."
  brian "I guess that’s to be expected."
  brian "Feel free to ask me if you need help with anything. I know my way around pretty well."
  burrito "Thanks, Brian!"
  brian "No problem."
  brian "Anyway, we should get started eating before lunch is over."
  show burrito happy
  burrito "Yeah, I didn’t realize it earlier, but I’m starving!"
  hide brian
  hide bj

  "~munching sound~"
  "*munch* *munch*"
  "This is delicious! Tastes just like home..."
  "~munching sound~"
  show air surprised at right
  show brian surprised at center
  "*munch* *munch*"
  hide air
  hide brian
  show bj surprised at center
  bj "…"
  hide bj
  show arc smiling at right
  arc "..."
  hide arc
  show burrito nervous 
  "Whoops- almost forgot I wasn’t alone with my burritos! Hope they don’t think I’m too weird…"
  hide arc
  hide bj
  show brian normal at right
  show burrito embarrassed at left
  brian "You really do enjoy burritos, don’t you?"
  burrito "Y-yeah..."
  hide burrito
  hide brian
  show arc normal at left
  show air normal at right
  arc "You know what I enjoy?"
  show arc happy
  arc "Berries jubilee!"
  arc "The combination of sweet berries with cold vanilla ice cream… Hey, I just got an idea."
  arc "Maybe I can convince the cafeteria to serve it!"
  air "Want to know what I enjoy?"
  air "Pure, simple water."
  air "It's so refreshing, especially after playing a game of Ultraball. Gotta keep myself quenched when I’m moving around like that!"
  air "Man, now I feel like going out to play instead of going to class."

  "*~Bell ring~*"
  show arc annoyed
  hide air
  show brian normal at right
  brian "Eh… looks like lunch is over."
  hide arc
  hide brian
  show burrito normal at left
  show bj normal at right
  bj "Well, you proved to be a pleasant lunchtime companion, Burrito. With that, I hope you will join us again sometime."
  burrito "Thanks, Abba."
  hide bj
  show arc normal at right
  arc "Meh… I don’t feel like moving yet, but whatever… See ya around."
  hide right
  show air happy at right
  air "Maybe you guys can come play some Ultraball later!"
  hide air
  "A student council president and his little brother, a very privileged Zapdos as the vice-president, and a dedicated Ultraball player."
  "It’s amazing how a variety of personalities can get along together. Maybe I’ll hang out with them some more later."
  "Oops, time to head back to class."
  hide Burrito

  return

label day_1_lunch_table_4:
    $ relationships["flareon"]+=3
    "Is it really a good idea to sit there? I might be bothering her. Maybe she wants to eat alone."
    "Then again, I figure this is as good a chance as any to meet someone. Can’t just expect new friends to run into me on the first day."
    "No time for doubts now."
    
    #play sound "footsteps.mp3"
    
    "Great! Something to break the ice, at least."
    "It doesn’t look like she has anything for lunch; just a book that she’s reading. I squint at the cover, trying to get a better look."
    "Oh! It's that \"Sparkle Zubat\" series. I've only heard others talking about the book, but it doesn't really seem like my thing."
    "Harry Oshawotter is my book of choice, though. Maybe she also reads it? Only one way to find out."
    show burrito nervous at left
    burrito "Hi there, mind if I sit here?"
    show flareon at right
    flareon "..."
    burrito "I'm... well, people have been calling me Burrito, ahaha..."
    show burrito flustered at left
    burrito "B-but don’t think you have to call me that, or that that’s my real name. It’s just some silly nickname."
    flareon "..."
    "She just keeps reading her book..."
    show burrito nervous at left
    burrito "But, um, you can call me Burrito, I guess, if you prefer... That's okay too!"
    flareon "..."
    burrito "Uh... Stay silent if it’s okay for me to sit here!"
    flareon "..."
    "..."
    "Guess I should just sit down here and get started on my lunch."
    show burrito at left
    burrito "So, um... what's your name?"
    flareon "..."
    show burrito nervous at left
    "She's still reading her book, like she's ignoring me..."
    "She hasn't even looked at me once."
    "All she's done is turn pages. Maybe I made a mistake sitting here..."
    show burrito at left
    burrito "Well, uh... What are you eating? Not your book, are you?"
    show burrito nervous at left
    burrito "Um... Though if you were, it wouldn’t be so bad. It *is* rich in fiber!"
    flareon "..."
    show burrito embarrassed at left
    "Swing and a miss there."
    "Maybe I shouldn't have brought up the book..."
    "Sigh."
    "I should get started on my lunch before class starts."
    show burrito at left
    burrito "The cafeteria is pretty packed, so I hope you don’t mind if I just stay here and eat."
    flareon "..."
    "Still nothing."
    "Ah well. At least there’s no way for me to be awkward with my food."
    flareon "...Is that salsa?"
    show burrito surprised at left
    "!"
    "She... she actually talked!"
    "Is she... looking at my salsa...?"
    burrito "Huh?"
    show burrito friendly at left
    burrito "A-ah, yeah... yes it is."
    flareon "..."
    "Of all things to get her attention, it’s my salsa? Not my witty banter?"
    "Whatever works, I guess."
    show burrito nervous at left
    burrito "Um... you can have some if you want...?"
    "I watch as she carefully samples a bit. Wait-"
    show burrito panic at left
    "W-wait, that's super spicy! I should have warned her first! This could be bad!"
    "My cousins grow their own Tamato and Kelpsy berries and have specifically bred them to be really, really hot. Only the bravest of tongues can handle its fiery taste!"
    flareon "..."
    "But the Flareon doesn’t react. I simply look on, agape with fear. Any second now she’ll be howling in pain."
    show flareon small smile at right
    flareon "...It's good."
    
    # Flareon character panel appears, when it exists
    "CHARACTER PANEL PLACEHOLDER"
    $ introduced["flareon"] = True
    
    show burrito surprised at left
    burrito "...Huh?"
    "She drank it all..."
    show burrito embarrassed at left
    "She even licked her lips once she was done... eh?!"
    show burrito nervous at left
    "I... I don't get it, shouldn't she be screaming right now?! Tearing up at least? It took me years to get used to the flavor!"
    show flareon at right
    flareon "... Did you make this?"
    
    menu:
        "No, not really.":
            $ relationships["flareon"]+=1
            show burrito nervous at left
            burrito "U-um, yes... and no. My mother and I made it. She has this whole process to it where she blends a bunch of different berries together at just the right temperature."
            show burrito happy at left
            burrito "See, the temperature is SUPER important! Otherwise it won’t bring out the flavor, right?"
            show burrito sad at left
            burrito "Or... at least, that’s what my mom tells me... Sorry, this must all be very boring for you."
            show flareon small smile at right
            flareon "..."
            "I’ll take that as a maybe."
            show burrito embarrassed at left
            burrito "I-... In truth I have no idea what happens. My mom always did all of the work, I just helped her cut the berries."
            "The spice level usually varies from person to person. My dad likes it more in the “medium” range, but my mom and I really like it spicy."
            flareon "..."
            show burrito at left
            burrito "Uh... I take it you like spicy as well?"
            flareon "..."
            "No words, but she nodded in response."
            "We're getting somewhere!"
            burrito "Shoulda pegged you as one who enjoys spicy food. You’re a Flareon, after all!"
            show flareon at right
            flareon "..."
            "Another nod."
            "It’s actually kinda cute, the way she nods her head like that. I just wish she was willing to talk more."
            show burrito happy at left
            burrito "You know, my mom sent me a giant box of salsa. You’re welcome to have some if you’d like."
            flareon "Bring it to dinner."
            show burrito nervous at left
            burrito "W-what?! U...um, alright..."
            show burrito at left
            "After that, she returned to reading her book."
            "I should finish my lunch now."
            "~munching sounds~"
            burrito "*munch munch*"
            flareon "..."
            "I could see her giving glances at me from the corner of her eye. Not sure what that means, but I think she's actually trying to communicate!"
            show burrito nervous at left
            show flareon small smile at right
            flareon "..."
            "She nodded again."
            "And nothing else."
            show burrito at left
            "What a strange girl."
            "~bell rings~"
            burrito "Oh, lunch is over. I have to get back to class now."
            show burrito happy at left
            burrito "Thanks for letting me sit here. Bye!"
            hide burrito with moveoutright
            #Need flareon to move slightly before leaving
            #show flareon small smile
            flareon "..."
            hide flareon small smile with moveoutright
            "Oh... I just realized... I never found out her name..."
            "I'm looking forward to seeing her again, though. Such a mysterious girl..."
        "Of course I did!":
            $ relationships["flareon"]-=1
            show burrito happy at left
            burrito "I made it all by myself, didn’t you know?"
            flareon "..."
            burrito "You see, I’m just a magnificent chef and so I made all these different types of food. See, with this particular blend of salsa, the berries need to be mixed together at just the right temperature."
            show burrito nervous at left
            burrito "That’s because... uh... Well, I’m, uh, sure there’s a reason for it."
            show burrito happy at left
            burrito "But it makes for some pretty darn good salsa!"
            flareon "..."
            "Somehow, it’s like the air got a bit colder..."
            show burrito at left
            burrito "Well that’s not important. What’s important is that I made this!"
            show burrito smirk at left
            burrito "And there’s more where that came from, uh, \"hot-stuff\"!"
            burrito "..."
            show burrito panic at left
            "I did not just say that. I did NOT. JUST. SAY THAT."
            show burrito nervous at left
            burrito "Y’see, cause you’re like, a Flareon? And you like spicy stuff?"
            "...no! Stop. Just stop, right now...!"
            flareon "..."
            show burrito embarrassed at left
            burrito "*cough* So, uh, eat here often?"
            flareon "It’s the cafeteria, so yes."
            show burrito nervous at left
            burrito "O-of course, of course. W-well, maybe I’ll bring some more salsa to dinner later, how about it?"
            flareon "..."
            flareon "Fine."
            show burrito at left
            "Forget about it getting colder, the air is now absolutely frigid."
            "This has been an extremely awkward conversation. I should just go ahead and finish my lunch..."
            "~munching sounds~"
            show burrito sad at left
            burrito "..."
            flareon "..."
            "It's only been a few minutes, but it feels like I've been eating forever."
            "I can't help but keep looking at her though... I really think I need to apologize somehow..."
            show burrito nervous at left
            burrito "U-um-"
            "~bell rings~"
            show burrito sad at left
            burrito "Oh, the bell..."
            "Well, I really don't think I should say anything at this point."
            "I should just fix up and get outta here."
            hide burrito with moveoutright
            #Need flareon to move slightly before leaving
            #show flareon
            flareon "..."
            hide flareon with moveoutright
            "..."
            "I just realized, I never did find out her name."
            "But... I think it's best if I just leave it like that for now..."
    return