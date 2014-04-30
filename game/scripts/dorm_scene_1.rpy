label dorm_scene_1: 
 
  uk "KWEEAH!"
  show burrito_voiceover at left
  show burrito at left
  burrito "W...what was that?!"
  hide burrito 
  burrito "There's a strange figure in front of the window, wings outstretched. It's a...a…"
  scene dorm with dissolve
  show burrito at left
  show burrito_voiceover at left
  burrito "a xatu?"
  show right placeholder_xatu at right
  xa "..."
  burrito "Oh. You must be my roommate. Wait, that’s right! I heard about you in the acceptance letter. Hello there!"
  xa "..."
  burrito "I'm RJ, nice to meet you!"


  #Pause test
  #$ renpy.pause(30.0, hard=True)
  
  #RIOT test
  uk "ヽ༼ຈل͜ຈ༽ﾉ RIOT ヽ༼ຈل͜ຈ༽ﾉ"

  xa "..."
  burrito "..."
  xa "..."
  burrito "Okay..."
  hide burrito
  burrito "I look at the clock. It dawns on me that this is the first day of the new school year." 
  show burrito at left
  show right placeholder_xatu at right
  xa "..."
  burrito "No, I have class in half an hour."
  hide burrito
  burrito "Wait, did he just speak to me?"
  show burrito at left
  show right placeholder_xatu at right
  xa "..."
  burrito "Are you like one of those ventriloquist guys? With the puppets?"
  xa "..."
  burrito "Oh, of course! You’re a psychic type, like me."
  xa "..."
  burrito "Nice to meet you then, uh... Will? Will Totem?"
  xa "..."
  hide burrito
  burrito "He’s… odd. But he seems nice. This would be a good time to leave for class, considering the time, but maybe I could squeeze in some extra chat with Will before going…"
  menu:
    "Stay and chat":
      $ late_on_first_day = True
      burrito "Well, not much harm in staying a few extra minutes. I can just rush breakfast and get to class in time, right?"
      show burrito at left
      show right placeholder_xatu at right
      burrito "So, uh, Will. What's this school like? I mean, I know it's prestigious, but is it... fun? Are there any teachers or students I should watch out for? Any advice at all, really?"
      xa "..."
      burrito "Wow, really? That's very important. I should keep that in mind while organizing my schedule. Thank goodness you told me!"
      xa "..."
      burrito "You don’t say? I didn’t even know that was possible."
      xa "..."
      burrito "Uh huh. And he wasn’t even fired? Who’s our principal?"
      xa "..."
      burrito "A computer? You’re not joking, are you?"
      xa "..."
      burrito "Wait… what?! Class starts in five minutes?!"
      xa "..."
      burrito "Eep, I got carried away! I’d better have breakfast and rush to my first class. Excuse me, Will!"
      hide burrito
      xa "..."
      $ relationships['gator'] += 3
    "Get to class":
      $ late_on_first_day = False
      burrito "Better safe than sorry. I have the whole year to chat with Will, and being late on my first day won’t do me any good."
      show burrito at left
      show right placeholder_xatu at right
      burrito "I’m sorry, I’d like to stay and chat a bit more, but I think I wanna be early for my first class. I still need to have breakfast, so I’ll be on my way now. Please excuse me, Will."
      hide burrito
      $ relationships['atv'] += 2
      $ relationships['katie'] += 2
      $ relationships['bj'] += 2
  scene bg standard with dissolve #hallway
  show burrito_voiceover at left
  burrito "My stomach's growling. I think my mother said something about sending breakfast with me…  Ah, here it is! A box of poffins buried under the mountain of salsa.They’re just for me! I sure am glad that mom made me this delicious breakfast. Mmm. Tastes like cupcake. I eat a few before changing into my uniform.
  Nice. I don’t have the standard issue uniform most new students get yet, so I’ll just have to wear my old school uniform. Still, it’s not half bad. Hehe… Time to head to class. (image fades)"
return
