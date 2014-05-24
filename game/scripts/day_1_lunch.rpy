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
      call day_1_lunch_table_2
      $ do_nothing_yet = True
    "Table 3; Lazor, Fonz, ??? (Steelix), ??? (Charmeleon)":
      # call day_1_lunch_table_3
      $ do_nothing_yet = True
    "Table 4; ??? (Flareon)":
      call day_1_lunch_table_4
      $ do_nothing_yet = True
    "Sit alone":
      call day_1_lunch_table_5
      $ do_nothing_yet = True
  return

label day_1_lunch_table_1:
  $ relationships["bj"]+=3
  $ relationships["brian"]+=3
  $ relationships["air"]+=3
  "I think I’ll sit at Abba’s table. He helped me out with my enrollment form earlier, after all."
  show burrito nervous at left
  burrito "H-hey, Abba, mind if I sit here?"
  show bj at right
  voice "assets/voices/abba/day_1_lunch/ABBA Part 3 of 9.mp3"
  bj "Hm? Oh, the new student!"
  voice sustain
  bj "I suppose we can make room for you on your first day."
  if (late_on_first_day):
    show bj annoyed
    bj "However, being tardy to class is not a good start. This is still your first day, but I hope you won’t repeat the same offense later on."
    show burrito embarrassed
    burrito "R-right, I’ll do my best to be on time."
  show bj normal
  show burrito normal
  voice "assets/voices/abba/day_1_lunch/ABBA Part 4 of 9.mp3"
  bj "The office is still dealing with your enrollment form. They probably won’t be done until the end of the day."
  voice sustain
  bj "For now, we’ll just call you by your official name."
  show burrito surprised
  burrito "Ehh? But..."
  show bj at center
  voice "assets/voices/abba/day_1_lunch/ABBA Part 5 of 9.mp3"
  bj "Anyway, let me introduce you. Everyone, this is Burrito, a new student at Twitch Academy."
  show burrito normal
  burrito "Hello everyone, nice to meet you."

  show arc normal at right
  voice "assets/voices/abba/day_1_lunch/ABBA Part 6 of 9.mp3"
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
  voice "assets/voices/abba/day_1_lunch/ABBA Part 7 of 9.mp3"
  bj "And this is Air, one of the best Ultraball players here."
  air "Thanks, bro. Just doin’ my thing."

  # Air character panel appears, when it exists
  "CHARACTER PANEL PLACEHOLDER"
  $ introduced["air"] = True

  show air happy
  air "You should come watch a game sometime. It’s really intense."
  burrito "Thanks for the invite. That sounds interesting."
  hide air

  show brian normal at right
  voice "assets/voices/abba/day_1_lunch/ABBA Part 8 of 9.mp3"
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
  show arc smile at right
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
  voice "assets/voices/abba/day_1_lunch/ABBA Part 9 of 9.mp3"
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

label day_1_lunch_table_2:
  "ATV is looking at something on his phone. Hope I'm not interrupting anything important."
  show burrito nervous at left
  burrito "Hi, umm... Do you mind if I sit here?"
  show atv laughing at right
  show atv laughing
  atv "Oh, it’s the Burrito kid, vehvehvehveh."
  atv "Did you know your new nickname is being spread out to the world as we speak?"
  show burrito blushing
  burrito "E-eh?!"
  show atv laughing
  atv "Vehvehvehvehveh! Ms. Whitney is an avid PokéBook user."
  if (introduced["atv"] == False):
    # Atv character panel appears, when it exists
    "CHARACTER PANEL PLACEHOLDER"
    $ introduced["atv"] = True
  hide atv
  show katie sighing at right
  katie "He means he’s a creep who stalks people. Don’t mind him, Burrito."
  if (introduced["katie"] == False):
    # Katie character panel appears, when it exists
    "CHARACTER PANEL PLACEHOLDER"
    $ introduced["katie"] = True
  "Oookay, I guess? He doesn’t seem mean, at least."
  "I'll just sit down and get started on my burritos."
  hide katie
  show digrat normal at right
  digrat "*sniff* *sniff*"
  show digrat normal
  digrat "Are those homemade burritos? And mm, mm. Salsa? Is that... Spicy salsa! I smell Tamato and Kelpsy! Some Cheri too!"
  show burrito surprised
  burrito "Wow, you can really smell all that? You’re on point!"
  show digrat happy
  digrat "Heheh, I do have a good sense of smell. Burrito, eh? Everyone calls me Digrat."
  hide digrat
  show katie smile at right
  katie "My name is Katie, we’re in the same class. "
  show katie annoyed
  katie "The rude creep is ATV, by the way."
  hide katie
  show atv annoyed at right
  atv "Sorry if reading information openly on PokéBook means I’m a creep. Blame the content creator, not the reader!"
  show burrito smile
  burrito "It’s all right, it’s all right. Ah, Digrat was it? If you want some salsa..."
  hide atv
  show digrat normal at right
  digrat "Ah, no, I’m weak to spicy things. My muzzle is tingling!"
  digrat "Katie might want it though. She doesn’t mind hot food."
  hide digrat
  show katie smile at right
  katie "I can handle spicy food alright..."
  show katie aside
  katie "...unlike ATV here."
  hide burrito
  show atv sneering at left
  atv "Vehvehvehveh... I don’t need to remind you of the Octopus Incident, do I?"
  show katie embarrassed
  katie "H-hey, quit it..!"
  hide katie
  hide atv
  show burrito normal at left
  "ATV looks like he had just won a battle against Katie, who just mumbles to herself and concentrates on her food. Octopus incident? What are they talking about?"
  menu:
    "Ask about the Octopus Incident":
      "Curiosity gets the best of me, and I turn towards ATV."
      show atv sneering at right
      show burrito curious
      burrito "What is the Octopus Incident?"
      atv "It was last year. Katie came over to eat lunch with Lance-sensei, and there was octopus on the menu."
      show atv laughing
      atv "The face Katie made when she saw it... Veeehvehvehvehveh!"
      hide atv
      show katie embarrassed at right
      katie "I-I don’t like t-their eyes, okay?! They look creepy! Like you!"
      "The Dragonite cast me a glare before looking down to her plate, eating quickly. I don’t think she was very amused by my inquiry. ATV, though, seemed blissfuly happy."
      hide katie
      $ relationships["katie"]-=3

    "Don’t ask":
      "I open my mouth to ask, but decide against it. Katie seemed embarrassed enough as it was, and I didn’t want to make her too uncomfortable."
      show katie small_smile at right
      "She notices that, and shoots me a tiny smile as thanks."
      hide katie
      $ relationships["katie"]+=3

  show atv normal at right
  atv "So, Burrito. Are you planning on joining a club?"
  show burrito thinking
  burrito "Hmm... I haven’t really thought about it yet; I just got here."
  show burrito normal
  burrito "Are you in a club?"
  show atv proud
  atv "As a matter of fact, you are looking at the president and senior member of Twitch Academy’s resident Science Club!"
  hide atv
  show katie aside at right
  katie "And only member."
  hide burrito
  show atv angry at left
  atv "I will not have my status trivialized!"
  hide atv
  hide katie
  show digrat normal at right
  show burrito normal at left
  digrat "It’s good to just ignore him when he gets like this, newbie."
  show burrito aside
  burrito "I see, I se--ACHOO!"
  hide digrat
  "~flapping sound~"
  "V-Venomoth powder...?!"
  "Ow, my nose..!"
  show atv angry at right
  atv "I will not be left out of conversations either!"
  show atv curious
  atv "Now, what were we talking about?"
  show burrito awkward
  burrito "Uh..."
  hide burrito
  show katie normal at left
  katie "...pest problems."
  hide katie
  show digrat normal at left
  digrat "Yeah, pest-- choo! Pest problems!"
  hide digrat
  show burrito normal at left
  show atv normal
  atv "Ah, you must mean the fungal overgrowth located in the back of Ms. Whitney’s classroom, underneath the third seat from the back in the left-most row."
  show burrito confused
  burrito "The... the what? Why would yo--"
  show atv sneering
  atv "Vehvehvehveh... My dear Burrito, when you have an intellectual thirst like mine the pursuit and acquisition of knowledge satisfies me in an unparalleled way."
  show atv proud
  atv "To put it simply..."
  "Uh-oh."
  atv "I consider it my duty to study and solve life’s mysteries."
  hide burrito
  show katie sneering at left
  katie "Sure, when you’re not busy gorging yourself on those inane comics of yours."
  show atv annoyed
  atv "I-Why... You... Take that back!"
  show katie smirk
  katie "Or what?"
  hide atv
  show digrat normal at right
  digrat "C’mon Katie, don’t tease him like this. You know how he gets."
  hide digrat
  show atv annoyed at right
  atv "I don’t get anything, Digrat!"
  hide atv
  show digrat snicker at right
  show katie snicker
  "Katie and Digrat shoot each other knowing glances, snickering lightly at ATV’s turn of phrase."
  hide digrat
  show atv annoyed at right
  atv "I am merely passionate about an art form that deserves to be respected!"
  show katie eyeroll
  katie "Please, it’s nothing more than gussied up stories made to sell toys to little Pokemon."
  hide katie
  show burrito confused at left
  burrito "Um, excuse me, but what exactly are you guys talking about?"
  show atv happy
  atv "Oh? Do you not read “The A Team,” Burrito? It’s a fantastic series!"
  "Uh oh, I think I just stepped on another trap..."
  "~bell rings~"
  "...perfect timing!"

  if (late_on_first_day):
    show burrito normal
    burrito "Ah, sorry guys, I’d love to stay and chat but I was late to class earlier this morning, and I don’t want that to happen again."
    show atv normal 
    atv "Vehvehveh... Alright. We’ll talk another time."

  else:
    hide atv
    show katie normal at right
    burrito "Well, looks like lunch is over. Maybe I’ll see you guys later?"
    show katie happy
    katie "Sure! See you around, Burrito!"
  
  return

label day_1_lunch_table_3:
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
    show flareon small_smile at right
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
            show flareon small_smile at right
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
            show flareon small_smile at right
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
            #show flareon small_smile
            flareon "..."
            hide flareon small_smile with moveoutright
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
    
label day_1_lunch_table_5:
    "There's a lone table sitting at the corner. I don't know if I should sit with others yet. I really don't know any of them, so I feel like I'd be a bit of a bother..."
    show burrito at left
    voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 02 of 16.mp3"
    burrito "But eventually, it would be nice to join in and make some friends. So, until then..."
    show burrito sad at left
    voice sustain
    burrito "I'll just sit by myself."
    hide burrito
    #play sound "sit_down.mp3"
    #play sound "paper_bag_crinkle.mp3"
    "~~ Sound of Burrito sitting down ~~"
    "~~ sound of paper bag crinkling ~~"
    "Mom sent me the family’s celebratory bean and rice burritos for today’s lunch."
    "I could already hear my stomach growling in excitement."
    "Ooh salsa... yeah that's it..."
    "These just look even more delicious with the salsa on it."
    voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 03 of 16.mp3"
    burrito "Oh my lovely burritos, keep me company for today..."
    "..."
    "Even if I can’t sit with other students right now, I really shouldn't be upset."
    "After all, how can I be anything but happy with delicious burritos for lunch?"
    voice "assets/voices/brian/day_1_lunch/Brian Part 02 of 21.mp3"
    "???" "E-excuse me?"
    show burrito confused at left
    voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 04 of 16.mp3"
    burrito "Hmm?"
    show brian at right
    voice "assets/voices/brian/day_1_lunch/Brian Part 03 of 21.mp3"
    brian "Um, hello there. My name is Brian. Would you mind if I....sit with you?"
    
    menu:
        "Let him sit":
            $ relationships["brian"]+=3
            show burrito happy at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 05 of 16.mp3"
            burrito "Of course! I mean, if you really want to."
            show brian happy at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 04 of 21.mp3"
            brian "Sure!"
            
            # Brian character panel appears, when it exists
            "CHARACTER PANEL PLACEHOLDER"
            $ introduced["brian"] = True
            
            "Brian sits across from me and I notice his lunch; it’s a salad with lots of sunflower seeds, and some sort of vegetable sandwich."
            show brian at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 05 of 21.mp3"
            brian "So, um... I heard that you've seen my brother already..."
            show burrito surprised at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 06 of 16.mp3"
            burrito "Your brother? Wait, do you mean..."
            hide burrito
            hide brian
            show bj at center
            $ renpy.pause(1.0)
            hide bj with fade
            show burrito surprised at left
            show brian at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 06 of 21.mp3"
            brian "Yes. I'm Abba’s little brother."
            show burrito smile at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 07 of 16.mp3"
            burrito "Oh, I've met Abba! He seems like a really nice guy!"
            show brian awkward at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 07 of 21.mp3"
            brian "Y-yeah, he is."
            show burrito confused at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 08 of 16.mp3"
            burrito "Huh?"
            show brian at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 08 of 21.mp3"
            brian "Oh, it's nothing."
            show brian happy at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 09 of 21.mp3"
            brian "Say, could I try some of that salsa?"
            show burrito at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 10 of 16.mp3"
            burrito "Sure. But I have to warn you, it can be a little...spicy."
            "I watched as Brian scooped some salsa into a spoon and swallow it. A few seconds passed. I saw Brian start to sweat."
            show brian nervous at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 10 of 21.mp3"
            brian "W-well....that salsa really is....something!"
            show brian sweating at right
            voice sustain
            brian "It's so...so...."
            show burrito nervous at left
            burrito "..."
            hide brian
            "He immediately went for his bottle of water and drank it all up!"
            "Maybe I should have been a bit more stern with the warning..."
            show brian panting at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 11 of 21.mp3"
            brian "That...is....spicy...."
            show burrito embarrassed at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 11 of 16.mp3"
            burrito "Well, that’s because it was made with lots of Tamato and Kelpsy berries grown to be super spicy."
            show burrito at left
            voice sustain
            burrito "Also, water isn’t the best choice when it comes to combating spiciness."
            voice "assets/voices/brian/day_1_lunch/Brian Part 12 of 21.mp3"
            brian "Then, what’s the best way to *cough* fight it?"
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 12 of 16.mp3"
            burrito "Milk and other dairy products. In fact, I happen to have a bottle of Moomoo Milk to sha--"
            hide brian
            show brian at left with moveinright
            #play sound "swipe.mp3"
            "~wind sound/swiping sound~"
            show burrito surprised at left
            "?!"
            hide brian with moveoutright
            voice "assets/voices/brian/day_1_lunch/Brian Part 13 of 21.mp3"
            brian "*gulp gulp*"
            "He just drank that one all up too!"
            show burrito laughing at left
            "I'm trying hard not to laugh, but... hahaha..."
            show brian nervous at right with moveinright
            voice "assets/voices/brian/day_1_lunch/Brian Part 14 of 21.mp3"
            brian "Haah..."
            show brian at right
            voice sustain
            brian "Aah."
            show brian smile at right
            voice sustain
            brian "Wow, that really did the trick!"
            show burrito smile at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 13 of 16.mp3"
            burrito "I know, right?"
            show brian at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 15 of 21.mp3"
            brian "And you know what? This salsa's actually pretty good!"
            show brian happy at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 16 of 21.mp3"
            brian "Think you can give me a recipe for this?"
            show burrito surprised at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 14 of 16.mp3"
            burrito "Huh? But when you ate it…"
            show brian nervous at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 17 of 21.mp3"
            brian "I-I mean, maybe a milder version of it….if it’s not too much trouble."
            show burrito happy at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 15 of 16.mp3"
            burrito "Oh! Sure thing!"
            "I may not be the salsa expert in the family, but I've helped with the cooking long enough for me to know how it's done. Maybe I can finally try my hand at making my own now!"
            "~munching sounds~"
            show brian happy at right
            "The two of us continue to eat and chat about school. Turns out, we were actually in the same Biology class earlier, he just didn't get the chance to say much. Wonder why I didn't notice him though?"
            "Still, it feels really nice to have a friend, especially on the first day."
            "~bell rings~"
            show brian at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 18 of 21.mp3"
            brian "Oh, looks like lunch is over. Thanks for letting me sit here, Burrito!"
            show burrito smile at left
            voice "assets/voices/burrito/day_1_lunch/alone/Burritoful-- Part 16 of 16.mp3"
            burrito "No problem! It was great talking with you. I hope we can have another lunch like this."
            show brian smile at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 19 of 21.mp3"
            brian "Me too! Bye!"
            burrito "Bye!"
            hide burrito
            hide brian
            "And with that, we went to our next class."
            "Though, what was with his reaction earlier when I mentioned Abba?"
            "I hope it's nothing too troublesome. Maybe I should ask him about it next time..."
            "Anyway, I need to get back to class."     
        "Decline his offer":
            burrito "I... I’m sorry, but I’d like to be alone today."
            show brian sad at right
            voice "assets/voices/brian/day_1_lunch/Brian Part 21 of 21.mp3"
            brian "Oh... I understand. Well, have a good lunch."
            hide brian
            "I watch Brian leave with a look of guilt.I really didn’t mean to be rude to him. I hope that the next time we meet, we can have lunch together."
            
    return
