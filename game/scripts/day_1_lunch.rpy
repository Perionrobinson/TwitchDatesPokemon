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
      # call day_1_lunch_table_4
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
