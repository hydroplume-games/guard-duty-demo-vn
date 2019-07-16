# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define vp = Character("Penn", color='#2c5ba0')
define n = Character("Natsuki", color='#2c5ba0')
define vm = Character("Pennoren", color='#2c5ba0')
define nm = Character("Sumor", color='#2c5ba0')
define w = Character("White", color='#d11d1d')
define a = Character("Anderson", color='#d11d1d')
define c = Character("Captain", color='#d11d1d')
define k = Character("Knight", color='#d11d1d')
define t = Character("Agent", color='#d11d1d')
define wm = Character("Whitman", color='#d11d1d')
define am = Character("Andres", color='#d11d1d')
define cm = Character("Capian", color='#d11d1d')
define ad = Character("???", color='#d11d1d')

# Images (backgrounds) to be used in this script
image black = "#000"

# Other useful variables
default list_cps = "0.1"  # This is how long to pause between listed items; set to "*1" for default cps
default pause = "0.1"

# The game starts here.

label start:
    scene black  # Start with a black background

    # Light silvery color, or #caccce
    "{color=#d7dbe2}{b}Monday, 19:00{/b}{/color}"

    "{cps=18}Another day, another dollar.{/cps}"
    show natsuki idle
    n "Quite a few dollars, to be honest."
    vp "I still can't believe how well they pay us to sit our asses in a tower to watch a fence."
    n "That's private security for you, almost makes me glad that we left the army."
    vp "We should remember to thank White for setting us up with this gig."
    vp "Just a few more months, then I can finally afford that trip to Australia..."
    vp "What about you Nats?"
    # hide natsuki idle ## Unnecessary
    show natsuki pout
    n "Didn’t I tell you to not call me by that name…"
    menu:
        "Apologize.":
            vp "Sorry. I’m used to calling you by that name."
            n "It’s okay Penn. At least you’ve apologized to me. Unlike those other jerks we work with."

        "Tease her.":
            vp "What’s wrong about it? It’s a good little nickname. Short and straightforward, just like you."
            n "Well fuck you too Penn. I may be shorter than you, but I can still kick your ass!"
    # hide natsuki pout ## Unnecessary
    show natsuki idle
    n "Anyway, I don’t actually know what I would be doing once we’re-"
    hide natsuki
    show whitman idle
    w "Hey Penn! Natsuki! Your shift's about to start! You’d better go and take Anderson’s place."
    w "Make the crotchety bastard wait on that tower a minute after his shift ends and you’ll never hear the end of it."
    w "The captain is also already there to supervise the shift change."
    show whitman idle at right
    show natsuki pout at left
    vp "We’ll be there in a second."
    hide whitman idle
    show natsuki pout at center
    vp "Well… you were saying?"
    n "Let’s go to the Captain first. We can talk about this when we’re in the tower."
    hide natsuki idle

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room  # Transition to scene outside the facility/tower here

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show captain idle
    c "Alright, you two know the drill. Twelve-hour shift."
    c "No eating, no smoking, no using your cell phone or reading."
    c "Just stay awake and keep your eyes on the fence."
    c "Ignore anything you hear from the facility itself- it’s none of your business."
    vp "You don't have to give us the same damn speech everyday Cap, we’ve got this."
    c "If you fuck up it's my ass on the line too, so I rather not take any chances."
    c "Now get up there, Anderson is getting jumpy."
    hide captain idle

    # Transition to tower scene

    "Climbing the tower, I see that the captain is right. Anderson is even more restless than usual."
    show anderson idle
    "He's smoking, of course, and I see more than one empty pack of crisps on the floor."
    show natsuki idle
    n "You’d better clean this mess up, because I'm sure as hell not doing it for you again."
    a "Stuff it, Natsuki. I know what I'm doing."
    vp "We’re not going to rat you out for a few cigarettes either, Anderson."
    a "Whatever. It’s not like shorty over here had ever smoked one in her life."
    hide anderson idle

    vp "He really is a mess today. Is that a flask he's hiding under his jacket?"
    n "It sure is. I’ll get payback on him one of these days."
    vp "Heh. I’d sure like to see that happen."
    hide natsuki idle

    show anderson idle
    a "Just keep both your eyes open. My knee had been acting up, and that means something fishy is going to happen."
    a "I just don't trust those eggheads inside, they're always up to something."
    vp "They could be cloning Elvis for all I care. Well, as long as they keep paying us."
    a "Yeah. Good luck with your shift Penn. Take care of shorty over here."
    hide anderson idle

    show natsuki idle
    n "Has he always such an asshole?"
    vp "Well, that’s Anderson for you. Let’s check our gear to see if everything is here..."
    "My rifle,{cps=[list_cps]} {/cps}combat vest with five magazines,{cps=[list_cps]} {/cps}flashlight,{cps=[list_cps]} {/cps}canteen,{cps=[list_cps]} {/cps}radio,{cps=[list_cps]} {/cps}med-kit,{cps=[list_cps]} {/cps}night vision goggles."
    vp "All good."
    n "I’m all set too."
    vp "Now all we have to do is just sit back and watch the fence…"
    vp "Oh wait… I’ve almost forgotten."
    n "What?"
    vp "What was it that you were going to do once we’re out of here?"
    n "I told you that… I don’t know what I’ll be doing."
    vp "No places to visit? No trips? Nothing?"
    n "I don’t know."
    vp "How about you come with me to Australia? It could be really fun for you."
    n "Yeah. As if hanging out with you outside of work isn’t already a pain in the ass."
    vp "I’ll think about it, Penn."
    hide natsuki idle

    "{color=#d7dbe2}{b}Monday, 22:00{/b}{/color}"
    vp "God, this is boring. Every time I finish a shift I forget just how mind numbingly dull sitting up here is."
    show natsuki idle
    n "Well, what were you expecting? It’s why I brought something to read..."
    vp "Didn’t Captain say not to bring anything with us to keep us distracted?"
    n "I don’t really care all that much. It’s boring up here anyway. Might as well sneak in some things to pass the time. Anderson had done so too."
    vp "Well I guess you’re right. If you don’t get caught that is."
    vp "What is it that you’re reading anyway?"
    n "It’s “none of your business” is what it is."
    vp "It’s my business when you’ve brought it up."
    n "Fine… Just don’t laugh at me if I show you what I’m reading."
    "Natsuki passes over to me a worn out copy of some sort of… manga."
    "The cover is barely legible, but the title reads “Parfait Girls”."
    n "Are you going to laugh at me?"
    vp "No."
    vp "I’m just shocked that you would read something like this…"
    vp "Then again… maybe you have been into these types of things."
    n "No I don’t! I just… Really like the writing and visuals in this..."
    vp "Haha. Well Captain would get a laugh out when he sees this!"
    n "No! Please don’t tell anyone about this!"
    vp "I’m joking. Your secret is safe with me. Besides, I wouldn’t be that much of an asshole to you."
    n "Thanks Penn…"
    vp "Where did you even get this anyway?"
    n "I… just found it among my old belongings. I don’t actually remember where I got it…"
    vp "Oh, so you have amnesia now?"
    n "Shut it Penn. Hand me back my manga."
    vp "Alright. Alright. Just make sure to hide it from the others. If you don’t want to end up being teased about this."
    "I hand Natsuki back her manga, and return my gaze upon the fence…"
    hide natsuki idle

    "{color=#d7dbe2}{b}Monday, 23:30{/b}{/color}"
    show natsuki idle
    n "These mosquitoes are driving me fucking insane."
    vp "Don’t they for everyone?"
    n "And what the hell did Anderson do to the chair?{p=1.5}How can plastic be this uncomfortable?"
    n  "It wasn't this lumpy yesterday, I swear."
    vp "Are you just going to nit-pick at everything, Natsuki? Come on."
    n "Nine more hours of this shit..."
    vp "And nine more hours of having to hear you complain. Great."
    n "Wait… do you hear that?"
    vp "Hear what?"
    n "There are noises coming from the facility. It sounds a bit like drums."
    vp "Yeah. Maybe those nerds are starting a band, and we’re here to guard their sweet grooves. Heh."

    n "No… The noises are getting louder. Those are definitely drums, and I'm starting to hear this eerie chant too."
    vp "Yeah… I’m starting to hear it too."
    n "What the hell do you think they are doing in there?"
    vp "I don’t know. It’s not our business anyway."
    n "Well… Whatever they did, it's over now."
    vp "Yeah. The gig’s over, I guess…"
    "I hope."
    hide natsuki idle

    "{color=#d7dbe2}{b}Tuesday, 01:30{/b}{/color}"
    vp "Alarms!? The entire facility is lighting up like a Christmas tree."
    show natsuki idle
    n "What the hell is going on now?"
    vp "Those guys they keep to handle inner security are all riled up, swarming the entire perimeter with their jeeps…"
    n "We’d better go down to find out what’s going on!"
    vp "No… Our orders were to stay here. Let them handle it."
    n "Fine… If you say so."

    n "The radio’s also gone apeshit too, but it's all code words that I don’t understand."
    vp "Probably to keep the likes of us focused on our job."
    n "Look, they’ve even launched a chopper. Anderson was right,{cps=0.5} {/cps}they {i}were{/i} messing with something in there..."
    vp "And I thought that you didn’t trust that jerk."
    vp "Whatever it is, it's really none of our business. We’re just outer security; simple grunts."
    n "What? We’re just going to sit on our asses like this?"
    vp "Yeah. Just sit tight, obey our orders, and stay the hell out of the way."
    n "Or, I don’t know, we can do something about it?"
    vp "Look. The spooks are going inside.{p=1.5}They'll fix everything, nothing for us to worry about."
    n "Okay... I guess we’ll let them handle it."
    hide natsuki idle

    "{color=#d7dbe2}{b}Tuesday, 01:50{/b}{/color}"
    vp "They aren't coming out."
    show natsuki idle
    n "Yeah… Everything went quiet again, but no one has come out."
    vp "All the lights are out too, {cps=0.5} {/cps}{cps=*0.6}that's definitely not supposed to happen.{/cps}"
    n "Remember that this was your idea."
    vp "It's okay, the spooks are probably just getting things under control, everything's cool…"
    n "Penn… the radio’s dead. Something’s very wrong here."
    vp "Fine… Maybe we should climb down and sneak away before whatever’s in there gets to us too?"
    n "Finally, good to see you come to your senses. Let’s get out of here before-"
    hide natsuki idle

    vp "Wait, what's that? Someone’s coming out."
    n "Jesus, that's a relief."
    vp "Wait. Those aren’t the spooks."

    vp "Better turn night vision on…"
    n "I already have mine on…"
    vp "What the fuck is tha-?!"

    "{color=#d7dbe2}{b}????{/b}{/color}"
    "The stone of the watchtower is cold beneath my fingers."
    "Was it always stone? It must have been, this tower has been here for centuries."
    "But why am I remembering metal?"
    show natsukim idle
    nm "Are you alright Pennoren?"
    vm "Yes, I am Sumor."
    vm "The solitude must be playing tricks on my mind…"
    vm "Being a royal scout is no easy task, but I perform it gladly."
    nm "The King will be proud of us."

    vm "What's that? A horn!"
    nm "Look, over yonder!"
    hide natsukim idle

    "Scanning the road, I see a group of footmen making their way to our tower, carrying the royal standard, and forming a protective ring around a majestic figure."
    nm "Why, it's the King himself, here at our humble tower!"
    vm "What on earth is he doing here?"
    "A man approaches the tower, wearing the uniform of the royal guard."

    k "Good scouts, the realm requires your services!"
    k "In the name of the King, attend!"

    show natsukim idle
    nm "We must make haste and hurry to do as we are commanded."
    "\"Don't.\""
    "\"You have orders. Something is wrong here\""
    nm "Why has’t you stopped? The king is here!"
    vm "I’m coming."
    hide natsukim idle
    "How can serving the wise King be wrong?"
    "He is our just ruler, our savior."

    nm "Good sir knight, how may we assist your party?"
    show knight idle
    "The knight had a grim look in his eyes."
    k "I fear we come bearing grave news."
    k "The castle has fallen to the forces of the Adversary. We barely managed to rescue the King before we were overwhelmed and forced to flee."
    k "The Prince and Queen were killed during our escape."
    k "Now, we require your help and that of your cohorts to show us a safe way through the border."
    k "We already have them here."


    "Indeed they have."
    "Caspian, Whitman, and Andres, my loyal friends, are among the party."
    "Very well."
    "We must make haste before the Adversary and his minions arrive."

    "Suddenly, the call of a dread horn."
    "Too late! The knight hears it too."
    k "To arms, men, protect the King with your life!"
    hide knight idle
    "We form a protective ring around the King, as the wretched forces of the Adversary descend upon us."

    "Flying beasts with glowing eyes and fiery breath, hulking, crawling behemoths with skin like steel, chitinous footmen that scream at us in their alien tongue."
    "They are trying to capture us alive, but we won't let them, we all know what they do to captives."
    vm "We fight to the death, for the King!"
    show natsukim idle
    nm "For the King!"
    hide natsukim idle
    show whitmanm idle
    wm "For the King!"
    hide whitmanm idle
    show andersonm idle
    am "For the King!"
    hide andersonm idle
    show captainm idle
    cm "For the King!"
    hide captainm idle

    "I raise my bow and take a foot soldier through the eye."
    "Whitman is engulfed by the flames by one of the behemoths."
    "Andres falls, a poison barb in his neck…"
    "I ready my next arrow..."
    "Caspian is taken down with a raw shock of power by one of their mages..."
    "I feel a sting in my neck, and see that Sumor and I are the only ones left standing, save for the King himself."
    "He fights with the force of a typhoon, falling foul beasts left and right, and ripping the behemoths to shreds with his mighty sword..."
    "Even cutting a flyer from the sky, but they are too many..."
    "He falls, his body pierced with dozens of metal barbs."

    "My tears are the last thing I see as the world turns dark…"

    "{color=#d7dbe2}{b}????{/b}{/color}"
    show shadow idle
    ad "RthgEtTn Dra'k! NoR MoStdyX!"
    "A figure dressed in writhing shadows, its tongue demonic."
    "The Adversary."
    "I will never betray my King! Begone, cruel revenant."

    ad "SRoTn, caBn yoEu heaWr meU?"
    "Not shadows..."
    "Black fabric."
    "Wait, I think I'm beginning to understand…"
    hide shadow idle

    show agent idle
    t "Son, do you understand me?"
    t "Can you tell me who you are?"
    vm "I am Veron Pennoren, proud scout of the…"
    "No, that isn't right…"
    vp "I… I'm Vernon Penn, sir. I think."
    "The man smiles, he seems relieved."

    t "I think this one is going to be okay."
    t "Leave him here, for now, let him recuperate along with the girl."
    t "I'll arrange for some class-Bs."
    t "Everything is going to be alright, son, Just lie down and relax."
    t "It's over."
    hide agent idle
    vp "Yeah… that sounds like a good idea..."

    "{color=#d7dbe2}{b}Sunday, 07:00{/b}{/color}"
    vp "Last shift is finally over."
    show natsuki idle
    n "Well, wasn’t it certainly eventful?"
    vp "I can't believe it's been six months already."
    n "A little more than that, I think?"
    vp "It’s about time to leave this dirt hole behind and finally catch that plane to Australia. You coming?"
    n "Maybe... Let’s get down and pack our things."
    hide natsuki idle
    vp "I really just can't believe they paid us so much for us to sit on our asses and watch a fence."

    "Natsuki and I head down the ladder..."
    "Only to be greeted by a familiar face."

    show agent idle
    t "You two get packing. You both are being reassigned to another Site."
    show natsuki idle
    n "What do you mean reassigned? I thought we were done!?"
    hide natsuki idle
    vp "Wait… Don’t I remember you from somewhere?"
    t "No you don’t. Get packing before 08:00 sharp."
    t "We have uses for the likes of you two."
    hide agent idle

    "END OF DEMO"

    # The game ends on return

    return
