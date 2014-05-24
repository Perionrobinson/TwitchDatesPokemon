label class_scene_1:
  scene bg standard with dissolve
  show burrito_voiceover at left
  show burrito at left
  burrito "I’d better get to class. I just- oof!"
  voice "assets/voices/gator/day_1_hallway/Lazor Part 2 of 8.mp3"
  uk_gator "Hey, Junior. Just where do you think you're going in such a hurry? It looks to me like you’re running in the hallway."
  burrito "W...what? Who said that?"
  voice "assets/voices/gator/day_1_hallway/Lazor Part 3 of 8.mp3"
  uk_gator "Up here, new kid."
  show gator at right
  voice "assets/voices/gator/day_1_hallway/Lazor Part 4 of 8.mp3"
  gator "The name's Lazor. Lazor Gator. Has no one ever told you that running in the halls is an offense worthy of expulsion?"
  burrito "S... Sorry, Lazor Gator…"
  voice "assets/voices/gator/day_1_hallway/Lazor Part 5 of 8.mp3"
  gator "Sorry? Why’re you apologizing to me? You’re the one who’s going to get kicked out. And on your first day, too. Tch..."
  uk_bj "Gator, do you have to do this to every new student on their first day?"
  voice "assets/voices/gator/day_1_hallway/Lazor Part 6 of 8.mp3"
  gator "Hey! I was just getting started with this poor fella!"
  voice "assets/voices/gator/day_1_hallway/Lazor Part 7 of 8.mp3"
  gator "Well, since that joke’s been ruined..."
  voice "assets/voices/gator/day_1_hallway/Lazor Part 8 of 8.mp3"
  gator "It's nice to meet you!"
  uk_bj "Don't you have a class to get to, Gator?"
  gator "I dunno, do I?"
  uk_bj "Mmm. Well, if your intent is to play this little game of yours, so be it. I've important matters to attend to, like directing this little Espeon here to class."
  gator "Ugh. Boring. I’m off."
  hide gator
  $ relationships['gator'] += 1
  uk_bj "Now then..."
  show bj at right
  bj "Hello, sophomore. My name is Abba. I am the head of the student council, third year class rep, and your guide to your first class."
  if(late_on_first_day):
    bj "Incidentally, you are slightly tardy. A rather poor show, for your first day."
    burrito "Oh, I’m sorry..."
    $ relationships['bj'] -= 1
  else:
    bj "Incidentally, I noticed that you are slightly early for your first class. I approve."
    burrito "T-thanks. Good habits have to start early, after all!"
    $ relationships['bj'] += 1
  bj "Now, on to business. It seems the only Espeon currently enrolled is named..."
  bj "“...Burrito.” Is that you?"
  hide burrito
  burrito "What!? Mom didn't really... She couldn’t have..."
  show burrito at left
  burrito "W-what? No, my name is RJ!"
  bj "Hmm? But that would mean you are not enrolled in this school."
  burrito "No, I am! I'm a transfer student; today is my first day."
  menu:
    "Admit burrito is your nickname":
      burrito "Look, this is just a big misunderstanding. See, Burrito is what they called me back home, but it's just a nickname."
      bj "Hmm. Cute. I'm not quite sure how it got on the enrollment form... Nevertheless, I'll take it down to the office and get it sorted out. You may have to endure a class of everyone calling you Burrito, but knowing Ms. Whitney… Well, Burrito is probably better than Fluffy Sunray or the like."
      hide burrito
      burrito "‘F… Fluffy… Sunray..?!’ What kind of nickname is ‘Fluffy Sunray’?!"
    "Deny that burrito is your nickname":
      burrito "It's RJ. There's no way I've ever been called Burrito. Never."
      bj "Hmm. I'm not quite sure how it got on the enrollment form… Nevertheless, I'll take it down to the office and get it sorted out. You may have to endure a class of everyone calling you Burrito, but knowing Ms. Whitney… well, Burrito is probably better than Fluffy Sunray or the likes."
      hide burrito
      burrito "‘F… Fluffy… Sunray..?!’ What kind of nickname is ‘Fluffy Sunray’?!"
  show burrito at left
  bj "Speaking of Ms. Whitney, I am sure you know she runs your first class. Biology, correct?"
  burrito "Yep."
  bj "Do you know the way to Ms. Whitney’s room?"
  burrito "Er…"
  bj "I thought not. Walk straight out of this building and go down. You’ll end up straight in front of the biology lab."
  burrito "Ah. Thanks, Abba."
  bj "Not a problem. I hope to see you again soon."
  $ relationships['bj'] += 1
  hide burrito
  hide bj
  burrito "Alright, I just need to follow Abba’s directions to the letter and… hey! Is that… yeah, it is. The biology lab!"
  burrito "Shoot, I’m a little late. Still, I’m sure Ms. Whitney will forgive me since it’s my first day. Alright, here goes!"
  show burrito at left
  mw "Arc?"
  arc "Present."
  mw "Brian?"
  brian "Here."
  mw "Burrito?"
  burrito "I’m here! But my name isn’t-"
  hide burrito
  burrito "Woah… that Nidoking in the back of the class is really looking at me intently. And a Charmeleon… and a Zapdos. Geez, they’re really staring. At least they seem interested."
  burrito "Oh geez, I’m so nervous. That Venomoth and Dragonite are really staring. At least they seem interested."
  hide burrito_voiceover
  show katie:
      zoom 0.5
      xalign 1.0 yalign 0.5
  show atv:
    zoom 0.5
    xalign 0.0 yalign 0.5
  atv "Vehvehvehveh... Look, Katie. Another newbie."
  katie "Another poor soul for you to torment, you mean. Hello, new guy!"
  show atv:
      zoom 0.5
      xalign 0.0 yalign 0.5
      linear 1.0 xalign 0.5
  pause 1.0
  show burrito:
      
      zoom 0.5
      xalign 0.0 yalign 0.5

  burrito "Hi! I’m, uh, RJ. Who are you two?"
  atv "Hey, Katie. We should recite the A-Team motto to introduce ourselves."
  katie "What, ATV? That childish drivel? I told you I hate those comics."
  katie "Why, you…"
  katie "Uh oh. Here comes Ms. Whitney. You better get to your seat."
  burrito "Oh, right. Excuse me."
  show atv:
      zoom 0.5
      xalign 0.5 yalign 0.5
      linear 1.0 xalign 1.6
  show katie:
      zoom 0.5
      xalign 1.0 yalign 0.5
      linear 1.0 xalign 1.6
  show burrito:
      zoom 0.5
      xalign 0.0 yalign 0.5
      linear 1.0 zoom 1.0 yalign 1.0
  pause 1.0
  show generic_character at right
  show burrito_voiceover:
      zoom 1.0
      xalign 0.0 yalign 1.0
  mw "Hello, dears, and welcome to the start of a fun new school year! But before we can get to the wonders of biology-"
  "Everyone" "Groan…"
  mw "We need to take roll! Look alive, everybody. Arc?"
  arc "Present."
  mw "Brian?"
  brian "Here."
  mw "Burrito?"
  burrito "I’m here! But my name isn’t-"
  mw "Ahh, Burrito! You’re our new student, aren’t you? I’m sure we’re going to be VERY good friends."
  burrito "Oh, uh…"
  mw "Burrito transferred here from Little Cup High school. What a cutie, huh?"
  burrito "Um…"
  mw "It was a rhetorical question, sweetie. We all know you are. Does anyone have any questions for the new student before we move on with class?"
  atv "What’s your dorm number? As though I couldn’t find out myself. Vehvehvehveh…"
  air " Hey, do you play Ultraball? What’s your favorite team?"
  fonz " Are you a boy or a girl? I can’t tell with that doofy sweater of yours!"
  mw "..."
  mw ". . .Fonzie-pie, see me after class."
  fonz "...!"
  mw "Is that all, everyone?"
  brian "I’d like to know-"
  mw "Great! I'm sure you are all itching to find out more about Burrito, but for now, it's time to learn!"
  burrito "My name is actually-"
  mw "Learning time, Burrito. Start learning."
  hide burrito
  hide generic_character
  burrito "Well, I guess that could have been worse… at least it’s not Fluffy Sunray. Still, I hope Abba gets things sorted out in time."
  show burrito:
       zoom 1.0
       xalign 0.0 yalign 1.0
  burrito "But then again, Burrito is kind of cute... I just wish I knew what Mom was thinking when she put that as my official name."
  arc "Are you talking to yourself?"
  show arc at right
  arc "About… burritos? Seems rather vain, given your name."
  burrito "Oh, um. Yeah. I like burritos. It’s kind of a family tradition that we make burritos with super-spicy salsa for our first meal each time we go to a new school."
  arc "Quaint. My first day rituals involve proclaiming, 'I am an Archangel of JUSTICE! BOOORAAZZZ!'"
  mw "A volunteer!"
  arc "Beg pardon?"
  mw "I was just asking who wanted to hand out the syllabus. You clearly have too much energy, so you can do it, Sparky!"
  arc "My name is Arc, not Sparky. And I refuse to serve. Do you know how many servants I have at home? I will not lower myself to the level of… of... manual labor."
  mw "Aw, that’s a shame. Your grades could really do with a bit of a boost in my class, you know. It’s not often I’m willing to hand out extra credit so easily. Plus, I’m telling you to."
  show arc:
      linear 1.0 xalign 1.6
  arc "I'll file a lawsuit, just wait and see…"
  mw "That’s nice, Sparky."
  hide burrito
  burrito "Arc handed out the biology syllabi, muttering to himself all the while. We reviewed it line by line, as Ms. Whitney didn’t seem sure we knew how to read. Other than the frequent protests from students whenever Ms. Whitney gave someone a ridiculously cute nickname, it was peaceful and class proceeded smoothly."
  $ relationships['katie'] += 1
      
return
