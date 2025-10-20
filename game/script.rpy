# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define tj = Character("TJ")
define player = "THE PLAYER"
define liz = Character("LIZ")
define teacher = Character("teacher")
define classpres = Character("classrep")
define brian = Character("brian")
define host = Character("gameshow_host")
define lunch_lady = Character("cafeterialady")
define jeff = Character("jeff")
define bailey = Character("bailey")
# The game starts here.

label start:

    "Game Start"


#########
# DAY 1 #
#########
label day_loop_1:
    scene bg home_1
    "This is the home scene"
    scene bg neighborhood
    "This is the travel to school"
    "Red maple leaves scatter the across the sidewalk. "
    "A stream of students make their way towards the main school building."
    "Your neighbor and childhood friend T.J has spent the walk trying to convince you to join the e-sports club he plans to start this semester."
    show tj base with fade
    tj "I’m telling you [player], it will be awesome! And not only that, but think of how much we could make if we made it in the championship?"
    "player" "You're forgetting to mention yourself in that equation."
    "T.J has always been like this, always enthusiastic to start anything that excites him, but rarely following through once he starts."
    "player" "In any case, maybe I want to join another club. It's way too soon to commit."
    """T.J looks like he is about to protest when the school-bell cuts him off. Feet begin to quicken their pace, as
        the students rush to their homerooms.""" 
    """You follow suit and weave through the crowds and before long find
        your way to the homeroom class. Most of the other students are already seated and chatting amongst
        themselves."""
    scene bg classroom
    "This is the before lunch classroom"
    "Near the front is Brian and Liz who had saved a couple of desks for you."
    liz "Hey! T.J., [player] over here!"
    """Liz waves at you from across the room. It has always been surprising that Liz and Brian got along so well.
       They have completely different personalities.""" 
    "Liz always seems so energetic and lively. You can sense her presence in any room." 
    """Brian on the other hand has always been pretty quiet and goes out of his way not to draw attention to himself.
       He only really spoke when he was around his friends, or doing an activity he likes like playing games or cosplay.
       They had actually met at a cosplay event."""

    liz "Hey guys, how was the summer break?"
    menu q1:
        "It was pretty great!":
            liz "Cool what did you do?"
        "It was awful!":
            tj "Sorry to hear that."
    "Before long the homeroom teacher walked into the class."

    teacher """Alright settle down everyone. I'm sure you're all excited to talk about what an amazing
            summer you all had, but let's go over homeroom before all that."""

    teacher """First thing's first, please fill out your electives in your time tables and bring them to me
            before the end of the day. You'll notice there is a slot for clubs at the bottom."""

    "T.J. turns to you with a pleading look."

    teacher """There will be a club fair in room 2A after lunch. Everyone is expected to sign up for a club and
            return your forms with your selections to me or to Anastasiia, your class rep. Would you like to say a few
            words to the class?"""

    classpres "Uhh, not really."

    teacher """In any case please make your way to the next classes. And please beware, there is some
               construction happening on the 5th floor. 
               A student was injured and had to be taken to the infirmary."""

    "People had already began to disperse from the classroom and Brian and Liz were about to leave as well."

    tj "Argh, I'm heading to another class, but Brian, Liz, [player], don't pick clubs yet, I have a serious proposition to make."

    liz "Why don't we meet up at lunch and we can chat then? Brian and I have the same class next right?"
    brian "Yeah."
    liz "How about you [player]?"
    "Why is the first class an elective? I barely had a chance to look at the curriculum but I better pick something fast before I'm late for whatever class I go for"

    menu q2:
        "CLASS 1":
            player "Im going to class 1"
            $ classchosen = 1
        "CLASS 2":
            player "Im going to class 2"
            $ classchosen = 2 
        "CLASS 3":
            player "Im going to class 3"
            $ classchosen = 3
    brian "Sounds like we'll meet at lunch then."

    tj "Don't bail on me [player]"

    player "I make no promises!"
    "In an instant we scatter to our respective classes."

    scene bg lunch
    "This is the lunch scene"

    """Before long the bell is ringing for lunch and you make your way to the cafeteria. Quick scan of the room
       shows that T.J and the others haven't arrived yet. There doesn't seem to be many people in the room at all.
       \"No one cafeteria food on the first day huh?\" You think to yourself as you join the small line."""

    player "I suppose I can the table for the others till they get here."
    player "Though I'm not all that sure if I want to go ahead with T.J's club idea."

    """There are so many options it seems from the posters in the hallways alone, but then again, I could also
       not join any club and get so much time back at the end of the day. Maybe I should start thinking of an
       excuse to tell T.J."""

    lunch_lady "Hey honey , what will you be having?"

    player "Huh?"
    "The cafeteria lady looks at you with mild disinterest."
    lunch_lady "What will it be? today's menu is mac & cheese or mystery chicken stew."
    menu q3:
        "Mac and cheese":
            $ food = "mac and cheese"
            "The cafeteria lady slaps some mac and cheese onto the tray."
        "Chicken stew":
            $ food = "Chicken stew"
            "The cafeteria lady pours some stew onto the tray..."

    """After dumpimg a large portion on your plate she sends you off. As you settle down at a table, you see Brian
       and Liz, and soon afterwards T.J all head to the now slightly longer line, and signal your location to them.
       Right after a figure approaches your table. He has a scar on his left cheek and a menacing scowl."""

    player "Ah sorry these seats are tak..."
    "angry kid" "Give me your lunch!!"
    
    player "Huh?!?"
    "angry kid" "I said, give me your lunch, NOW!"
    "Stunned for a second, you regain your composure"

    player "Uh this is just the cafeteria food, you can get a tray up front and..."
    "angry kid" "Do I look stupid to you?"

    """He starts to make his way closer to you, and you're not sure if he's just going to steal your lunch or smack
       you in the face with it. He reaches into his pocket and is about to remove something when a voice
       interrupts him."""

    classpres "Jeff, don't give me work to do on the first day of school. Can't you at least wait a week?"

    jeff "Butt out of this. Don't think I won't come for you just becuase you're the class rep or whatever."

    """Before Anastasiia can respond T.J and the others show up, wondering what is going on. Jeff seeing the
       extra attention, decides to back off. But before he leaves, he reveals a small mug from his pocket and
       swoops a portion of my [food] before making a break for it out of the room."""

    player "What the..??"

    "Everyone looks on with shock except the class president who just looks fed up."

    classpres "That's Jeff, it's best to keep your distance from him. Anyway, I'll leave you all to what lunch you have left."

    liz "What was that about? Liz says a moment later."

    brian "Already attracting the local protein, huh [player]?"

    player "I don't know what that guy's deal is, but whatever, I wasn't too excited for [food] anyway."
    "After a short pause T.J. switches the subject."
    tj """Anyway, I was just starting to tell Brian and Liz about the plan for the games club. What do you all
          think? Could be really awesome right? Playing games after school each day?"""

    liz """I don't know... It does sound fun, but I've been thinking of joining the Drama club and trying to get
        Brian to join too. I hear the members write their own plays and make props for them and everything! We
        could have them do a gundam play and make mech suits and all kinds of stuff. That would be awesome!"""    

    tj "Awww come on. [player] back me up here, tell Liz she's about to make a big mistake."

    menu q4:
        "\'Agree\' uhh actually...":
            "uhhhh"
        "Nope":
            "noe"
    tj "What??? Not you too?! What club are you going for?"
    
    player "I don't knwo yet. Might decide after class, or not any of them."
    
    tj "So in that you'll..."
    
    brian """I don't know if you're thinking everything through T.J. As club president there's a bunch of other
          things you'll have to do. You may not even get to play much games at all."""

    tj "It can’t be that bad. You guys don't know what you're missing on."

    """Lunch was pretty uneventful after that. We went for the last class of the day and soon later were heading
       towards room 2A where the various clubs had set up stands and were handing out fliers and stickers,
       trying to win over as many students as they could."""

    menu club_choice:
        "Drama":
            "going to drama club"
        "T.J.'s club":
            "going to T.J's games club"
        "Track and field":
            "going to track and field club"
        "Basketball":
            "going to basketball club"
        "Football":
            "going to the football"
        "Cooking":
            "going to cooking club"
        "Poetry":
            "going to poetry club"
        "'Go home'":
            "I'm just going to head off."
    
    
    """They said that we have a short meetup at the end of the day for quick introductions and deciding the club
        meetup days. While there I ended up talking to a girl who said her name was Bailey and a group of other
        people."""
    $ showname = "SHOWTIME"
    bailey "Hey have you heard of the [showname] show?"
    player "The what?"
    bailey """These guys were just telling me about it. Apparently a mysterious show that hijacks the weather
           station frequency near midnight."""

    """It seems to be some kind of urban legend, though I've never heard of anything like that before, probably
       because I don't watch much TV to begin with, but also because I tend to ignore that kind of thing."""

    """The thought of a sort of pirate tv station did sound kind of interesting though. Like what kind of game
       show is it that they wouldn't broadcast it on a regular station. That might have been the reason why that
       night I decided to turn on the Tv to the weather station, and sure enough, at 11:03pm the did seem to get
       interrupted with an airing of a game show"""

    scene bg gameshow
    "This is the gameshow"

    host "Hello Hello Hello!" 
    host "I am your host and welcome to the game game show [showname]." 
    host """Thank you to all our viewers for tuning in. We have an amazing 5 part special for ya folks so please be sure to tune in! 
            Tonight we shall have fun with Trivia! There can only be one winner."""

    """The show looked kind of like a budget production, with slightly grainy footage and slightly jarring jump transitions. The host along with the contestants all wore masks that varied from masquerade ball masks, to welding helmets and ski masks. 
       There also seemed to be a small audience although the spot light made that you couldn't really see any of their faces."""

    """The rest of the set also seemed bare, with not much else besides a small podium that the host stood behind, 
       a banner with the show's name and a medium sized tv display."""

    """The show turned out to be not half bad. Between the indie production, and some of the questions that wouldn't 
       fly on prime TV, it makes sense why it isn't on a regular TV channel.  Probably some people who found a way 
       to get free air time and don't want to expose their real faces. In any case, it could be some mild 
       entertainment after a boring day of school."""

    scene bg classroom
    "This is the class after lunch"
    scene bg club
    "This is the club scene"
    scene bg neighborhood
    "This is the wlak home"
    scene bg home_2
    "This is the home scene at the end of the day"


#########
# DAY 2 #
#########
label day_loop_2:
    scene bg home_1
    "This is the home scene"
    scene bg neighborhood
    "This is the travel to school"
    scene bg classroom
    "This is the before lunch classroom"
    scene bg lunch
    "This is the lunch scene"
    scene bg classroom
    "This is the class after lunch"
    scene bg club
    "This is the club scene"
    scene bg neighborhood
    "This is the wlak home"
    scene bg home_2
    "This is the home scene at the end of the day"
    scene bg gameshow
    "This is the gameshow"    

#########
# DAY 3 #
#########
label day_loop_3:
    scene bg home_1
    "This is the home scene"
    scene bg neighborhood
    "This is the travel to school"
    scene bg classroom
    "This is the before lunch classroom"
    scene bg lunch
    "This is the lunch scene"
    scene bg classroom
    "This is the class after lunch"
    scene bg club
    "This is the club scene"
    scene bg neighborhood
    "This is the wlak home"
    scene bg home_2
    "This is the home scene at the end of the day"
    scene bg gameshow
    "This is the gameshow"

#########
# DAY 4 #
#########
label day_loop_4:
    scene bg home_1
    "This is the home scene"
    scene bg neighborhood
    "This is the travel to school"
    scene bg classroom
    "This is the before lunch classroom"
    scene bg lunch
    "This is the lunch scene"
    scene bg classroom
    "This is the class after lunch"
    scene bg club
    "This is the club scene"
    scene bg neighborhood
    "This is the wlak home"
    scene bg home_2
    "This is the home scene at the end of the day"
    scene bg gameshow
    "This is the gameshow"

#########
# DAY 5 #
#########
label day_loop_5:
    scene bg home_1
    "This is the home scene"
    scene bg neighborhood
    "This is the travel to school"
    scene bg classroom
    "This is the before lunch classroom"
    scene bg lunch
    "This is the lunch scene"
    scene bg classroom
    "This is the class after lunch"
    scene bg club
    "This is the club scene"
    scene bg neighborhood
    "This is the wlak home"
    scene bg home_2
    "This is the home scene at the end of the day"
    scene bg gameshow
    "This is the gameshow"

#########
# DAY 6 #
#########
label day_loop_6:
    scene bg home_1
    "This is the home scene"
    scene bg neighborhood
    "This is the travel to school"
    scene bg classroom
    "This is the before lunch classroom"
    scene bg lunch
    "This is the lunch scene"
    scene bg classroom
    "This is the class after lunch"
    scene bg club
    "This is the club scene"
    scene bg neighborhood
    "This is the wlak home"
    scene bg home_2
    "This is the home scene at the end of the day"
    scene bg gameshow
    "This is the gameshow"

#########
# DAY 7 #
#########
label day_loop_7:
    scene bg home_1
    "This is the home scene"
    scene bg neighborhood
    "This is the travel to school"
    scene bg classroom
    "This is the before lunch classroom"
    scene bg lunch
    "This is the lunch scene"
    scene bg classroom
    "This is the class after lunch"
    scene bg club
    "This is the club scene"
    scene bg neighborhood
    "This is the wlak home"
    scene bg home_2
    "This is the home scene at the end of the day"
    scene bg gameshow
    "This is the gameshow"

#########
# DAY 8 #
#########
label day_loop_8:
    scene bg home_1
    "This is the home scene"
    scene bg neighborhood
    "This is the travel to school"
    scene bg classroom
    "This is the before lunch classroom"
    scene bg lunch
    "This is the lunch scene"
    scene bg classroom
    "This is the class after lunch"
    scene bg club
    "This is the club scene"
    scene bg neighborhood
    "This is the wlak home"
    scene bg home_2
    "This is the home scene at the end of the day"
    scene bg gameshow
    "This is the gameshow"

#########
# DAY 9 #
#########
label day_loop_9:
    scene bg home_1
    "This is the home scene"
    scene bg neighborhood
    "This is the travel to school"
    scene bg classroom
    "This is the before lunch classroom"
    scene bg lunch
    "This is the lunch scene"
    scene bg classroom
    "This is the class after lunch"
    scene bg club
    "This is the club scene"
    scene bg neighborhood
    "This is the wlak home"
    scene bg home_2
    "This is the home scene at the end of the day"
    scene bg gameshow
    "This is the gameshow"

label choose_person_to_talk_to:
    menu:
        "Talk to":
            "Talking to ???"
        "c1":
            "Talking to C1"
        "c2":
            "Talking to c2"

    return
