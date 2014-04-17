label class_scene_1:
  scene bg standard with dissolve
  show rj_voiceover at left
  show rj at left
  rj "I’d better get to class. I just- oof!"
  uk "Hey, Junior. Just where do you think you're going in such a hurry? It looks to me like you’re running in the hallway."
  rj "W...what? Who said that?"
  uk "Up here, new kid."
  show right placeholder_gator at right
  lg "The name's Lazor. Lazor Gator. Has no one ever told you that running in the halls is an offense worthy of expulsion?"
  rj "S... Sorry, Lazor Gator…"
  lg "Sorry? Why’re you apologizing to me? You’re the one who’s going to get kicked out. And on your first day, too. Tch..."
  uk "Gator, do you have to do this to every new student on their first day?"
  lg "Hey! I was just getting started with this poor fella!"
  lg "Well, since that  joke’s been ruined..."
  lg "It's nice to meet you!"
  uk "Don't you have a class to get to, Gator?"
  lg "I dunno, do I?"
  uk "Mmm. Well, if your intent is to play this little game of yours, so be it. I've important matters to attend to, like directing this little Espeon here to class."
  lg "Ugh. Boring. I’m off."
  hide right placeholder_gator
  $ relationships['gator'] += 1
  uk "Now then..."
  show generic_character at right
  bj "Hello, sophomore. My name is Abba. I am the head of the student council, third year class rep, and your guide to your first class."
  if menu_flag1:
    bj "Incidentally, you are slightly tardy. A rather poor show, for your first day."
    rj "Oh, I’m sorry..."
    $ relationships['bj'] -= 1
  else:
    bj "Incidentally, I noticed that you are slightly early for your first class. I approve."
    rj "T-thanks. Good habits have to start early, after all!"
    $ relationships['bj'] += 1
  bj "Now, on to business. It seems the only Espeon currently enrolled is named..."
  bj "“...Burrito.” Is that you?"
  hide rj
  rj "What!? Mom didn't really... She couldn’t have..."
  show rj at left
  rj "W-what? No, my name is RJ!"
  bj "Hmm? But that would mean you are not enrolled in this school."
  rj "No, I am! I'm a transfer student; today is my first day."
  menu:
    "admit burrito is your nickname":
      rj "Look, this is just a big misunderstanding. See, Burrito is what they called me back home, but it's just a nickname."
      bj "Hmm. Cute. I'm not quite sure how it got on the enrollment form... Nevertheless, I'll take it down to the office and get it sorted out. You may have to endure a class of everyone calling you Burrito, but knowing Ms. Whitney… Well, Burrito is probably better than Fluffy Sunray or the like."
      hide rj
      rj "‘F… Fluffy… Sunray..?!’ What kind of nickname is ‘Fluffy Sunray’?!"
    "Deny that burrito is your nickname":
      rj "It's RJ. There's no way I've ever been called Burrito. Never."
      bj "Hmm. I'm not quite sure how it got on the enrollment form… Nevertheless, I'll take it down to the office and get it sorted out. You may have to endure a class of everyone calling you Burrito, but knowing Ms. Whitney… well, Burrito is probably better than Fluffy Sunray or the likes."
      hide rj
      rj "‘F… Fluffy… Sunray..?!’ What kind of nickname is ‘Fluffy Sunray’?!"
  show rj at left
  bj "Speaking of Ms. Whitney, I am sure you know she runs your first class. Biology, correct?"
  rj "Yep."
  bj "Do you know the way to Ms. Whitney’s room?"
  rj "Er…"
  bj "I thought not. Walk straight out of this building and go down. You’ll end up straight in front of the biology lab."
  rj "Ah. Thanks, Abba."
  bj "Not a problem. I hope to see you again soon."
  $ relationships['bj'] += 1
  hide rj
  hide generic_character
  rj "Alright, I just need to follow Abba’s directions to the letter and… hey! Is that… yeah, it is. The biology lab!"
  rj "Shoot, I’m a little late. Still, I’m sure Ms. Whitney will forgive me since it’s my first day. Alright, here goes!"
  show rj at left
  mw "Arc?"
  aj "Present."
  mw "Brian?"
  br "Here."
  mw "Burrito?"
  rj "I’m here! But my name isn’t-"
  hide rj
  rj "Woah… that Nidoking in the back of the class is really looking at me intently. And a Charmeleon… and a Zapdos. Geez, they’re really staring. At least they seem interested."
  rj "Oh geez, I’m so nervous. That Venomoth and Dragonite are really staring. At least they seem interested."
  hide rj_voiceover
  show katie:
      zoom 0.5
      xalign 1.0 yalign 0.5
  show atv:
    zoom 0.5
    xalign 0.0 yalign 0.5
  atv "Vehvehvehveh... Look, Katie. Another newbie."
  kt "Another poor soul for you to torment, you mean. Hello, new guy!"
  show atv:
      zoom 0.5
      xalign 0.0 yalign 0.5
      linear 1.0 xalign 0.5
  pause 1.0
  show rj:
      
      zoom 0.5
      xalign 0.0 yalign 0.5

  rj "Hi! I’m, uh, RJ. Who are you two?"
  atv "Hey, Katie. We should recite the A-Team motto to introduce ourselves."
  kt "What, ATV? That childish drivel? I told you I hate those comics."
  kt "Why, you…"
  kt "Uh oh. Here comes Ms. Whitney. You better get to your seat."
  rj "Oh, right. Excuse me."
  show atv:
      zoom 0.5
      xalign 0.5 yalign 0.5
      linear 1.0 xalign 1.6
  show katie:
      zoom 0.5
      xalign 1.0 yalign 0.5
      linear 1.0 xalign 1.6
  show rj:
      zoom 0.5
      xalign 0.0 yalign 0.5
      linear 1.0 zoom 1.0 yalign 1.0
  pause 1.0
  show generic_character at right
  show rj_voiceover:
      zoom 1.0
      xalign 0.0 yalign 1.0
  mw "Hello, dears, and welcome to the start of a fun new school year! But before we can get to the wonders of biology-"
  "everyone" "Groan…"
  mw "We need to take roll! Look alive, everybody. Arc?"
  aj "Present."
  mw "Brian?"
  br "Here."
  mw "Burrito?"
  rj "I’m here! But my name isn’t-"
  mw "Ahh, Burrito! You’re our new student, aren’t you? I’m sure we’re going to be VERY good friends."
  rj "Oh, uh…"
  mw "Burrito transferred here from Little Cup High school. What a cutie, huh?"
  rj "Um…"
  mw "It was a rhetorical question, sweetie. We all know you are. Does anyone have any questions for the new student before we move on with class?"
  atv "What’s your dorm number? As though I couldn’t find out myself. Vehvehvehveh…"
  ar " Hey, do you play Ultraball? What’s your favorite team?"
  fz " Are you a boy or a girl? I can’t tell with that doofy sweater of yours!"
  mw "..."
  mw ". . .Fonzie-pie, see me after class."
  fz "...!"
  mw "Is that all, everyone?"
  "pidgey" "I’d like to know-"
  mw "Great! I'm sure you are all itching to find out more about Burrito, but for now, it's time to learn!"
  rj "My name is actually-"
  mw "Learning time, Burrito. Start learning."
  hide rj
  hide generic_character
  rj "Well, I guess that could have been worse… at least it’s not Fluffy Sunray. Still, I hope Abba gets things sorted out in time."
  show rj:
       zoom 1.0
       xalign 0.0 yalign 1.0
  rj "But then again, Burrito is kind of cute... I just wish I knew what Mom was thinking when she put that as my official name."
  aj "Are you talking to yourself?"
  show generic_character at right
  aj "About… burritos? Seems rather vain, given your name."
  rj "Oh, um. Yeah. I like burritos. It’s kind of a family tradition that we make burritos with super-spicy salsa for our first meal each time we go to a new school."
  aj "Quaint. My first day rituals involve proclaiming, 'I am an Archangel of JUSTICE! BOOORAAZZZ!'"
  mw "A volunteer!"
  aj "Beg pardon?"
  mw "I was just asking who wanted to hand out the syllabus. You clearly have too much energy, so you can do it, Sparky!"
  aj "My name is Arc, not Sparky. And I refuse to serve. Do you know how many servants I have at home? I will not lower myself to the level of… of... manual labor."
  mw "Aw, that’s a shame. Your grades could really do with a bit of a boost in my class, you know. It’s not often I’m willing to hand out extra credit so easily. Plus, I’m telling you to."
  show generic_character:
      linear 1.0 xalign 1.6
  aj "I'll file a lawsuit, just wait and see…"
  mw "That’s nice, Sparky."
  hide rj
  rj "Arc handed out the biology syllabi, muttering to himself all the while. We reviewed it line by line, as Ms. Whitney didn’t seem sure we knew how to read. Other than the frequent protests from students whenever Ms. Whitney gave someone a ridiculously cute nickname, it was peaceful and class proceeded smoothly."
  $ relationships['atv'] += 1
  $ relationships['katie'] += 1
      
return
