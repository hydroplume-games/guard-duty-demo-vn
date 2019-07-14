# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define vp = Character("Penn", color='#2c5ba0')
define a = Character("Anderson", color='#d11d1d')

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
    
    "Quite a few dollars, to be honest."
    "I can't believe how well they pay me to sit on my ass in a tower and watch a fence."
    "That's private security for you, almost makes me glad I left the army."
    "I should really remember to thank David for setting me up with this gig. Just a few more months, and I can afford that trip to Australia I always wanted."
    "Shift's about to start, better go and replace Anderson.\nMake the crotchety bastard wait on that tower a minute after his shift ends and you'll never hear the end of it."
    "The captain is already here to supervise the shift change."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room  # Transition to scene outside the facility/tower here

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show guard idle

    "Captain" "Alright, Penn, you know the drill. Twelve hour shift. No eating, no smoking, no using your cell phone or reading. Just keep your eyes on the fence and stay awake. Ignore anything you hear from the facility itself- it doesn't concern you."

    vp "You don't have to give the same damn speech every day, Cap, I got it."

    "Captain" "If you fuck up it's my ass on the line too, so I rather not take any chances. Now get up, Anderson is getting jumpy."

    hide guard idle
    # Transition to tower scene

    "Climbing the tower, I see the captain is right. Anderson is even more restless than usual. He's smoking, of course, and I see more than one empty pack of crisps on the floor."

    call prototype_verbatim

    "END OF DEMO"

    # The game ends on return

    return

label prototype_verbatim:
    vp "You better clean this mess up, because I'm sure as hell not doing it for you again."
    a "Stuff it, Penn. I know what I'm doing. Just keep your mouth shut."
    vp "I'm not going to rat you out for a few cigarettes, Anderson."
    a "Whatever."

    "He really is a mess today. Is that a flask he's hiding under his jacket?"
    a "Just keep your eyes open. My knee's been acting up, and that means something bad is going to happen. Always does. I don't trust those eggheads inside, they're up to something."
    vp "They could be cloning Elvis for all I care. As long as they keep paying me."
    "Anderson climbs down, and I check my gear to see everything is there:"
    "my rifle,{cps=[list_cps]} {/cps}combat vest with five magazines,{cps=[list_cps]} {/cps}flashlight,{cps=[list_cps]} {/cps}canteen,{cps=[list_cps]} {/cps}radio,{cps=[list_cps]} {/cps}med-kit,{cps=[list_cps]} {/cps}night vision goggles."
    "All good. Now I just sit back and watch the fence."

    "{color=#d7dbe2}{b}Monday, 22:00{/b}{/color}"
    "God, this is boring. Every time I finish a shift I forget just how mind numbingly dull sitting up here is."
    "Mosquitoes are fucking driving me insane."
    "What the hell did Anderson do to the chair?{p=1.5}How can plastic be this uncomfortable? It wasn't this lumpy yesterday, I swear."
    "Nine more hours of this shit. God dammit."

    "{color=#d7dbe2}{b}Monday, 23:30{/b}{/color}"
    "Noises coming from the facility, sounds a bit like drums."
    "Maybe the eggheads are starting a band, and I'm here to guard their sweet grooves."
    "Heh."
    
    "{color=#d7dbe2}{b}Tuesday, 00:30{/b}{/color}"
    "The noises are getting louder."
    "Those are definitely drums, and I'm starting to hear this eerie chant too.{p=1.2}What the hell are they doing in there?"
    
    "{color=#d7dbe2}{b}Tuesday, 01:15{/b}{/color}"
    "Silence again.{p=1.8}Whatever they did, it's over now.{p=2.5}I hope."
    
    "{color=#d7dbe2}{b}Tuesday, 01:30{/b}{/color}"
    "Alarms!"
    "The entire facility is lighting up like a Christmas tree. Those spooks they keep to handle inner security are all riled up, swarming the entire perimeter with their jeeps."
    "Radio is going apeshit too, but it's all code words. They even launched a chopper."
    "Anderson was right,{cps=0.5} {/cps}they {i}were{/i} messing with something in there."
    "Whatever it is, it's none of my business. I'm outer security, just a grunt. Better just sit tight, obey my orders and stay the hell out of the way."
    "The spooks are going inside.{p=1.5}They'll fix everything, nothing for me to worry about."
    
    "{color=#d7dbe2}{b}Tuesday, 01:50{/b}{/color}"
    "They aren't coming out."
    "Everything went quiet again, but no one has come out. All the lights are out too,{cps=0.5} {/cps}{cps=*0.6}that's not supposed to happen.{/cps}"
    "It's okay, the spooks are probably just getting things under control, everything's cool."
    ""
    "Oh God, what the fuck is going on inside?! Radio is totally silent. Something is very wrong here. Maybe I should climb down, sneak away before whatever did the spooks in gets me too. Wait, what's that? Someone is coming out. Jesus, that's a relief. Wait, that doesn't look like the spooks. Better turn night vision on. What is that thing?"
    
    "{color=#d7dbe2}{b}????{/b}{/color}"
    "The stone of the watchtower is cold beneath my fingers. Was it always stone? It must have been, this tower has been here for centuries. Why am I remembering metal? The solitude must be playing tricks on my mind. Being a royal scout is no easy task, but I perform it gladly. The King will be proud."
    "What's that? A horn! Scanning the road, I see a group of footmen making their way to my tower, carrying the royal standard and forming a protective ring around a majestic figure. Why, it's the King himself, here in my humble tower! What on earth is he doing here? A man approaches the tower, wearing the uniform of the royal guard."
    "unknown" "Good scout, the realm requires your services! In the name of the King, attend!"
    
    "I hurry to do as I was commanded. In the back of my head, a little voice whispers"
    "\"Don't.\""
    "\"You have orders. Something is wrong here\""
    "but I ignore it. How can serving the wise King be wrong? He is our just ruler, our savior."

    "unknown" "Good sir knight, how may I assist your party?"
    "The knight had a grim look in his eyes."
    "unknown" "I fear we come bearing grave news. The castle has fallen to the forces of the Adversary. We barely managed to rescue the King before we were overwhelmed and forced to flee. The Prince and Queen were killed during our escape. Now, we require your help and that of your cohorts to show us a safe way through the border. We already have them here."
    "Indeed they have. Capian and Andres, my loyal friends, are among the party."
    "unknown" "Very well,"
    "I say,"
    "unknown" "We must make haste before the Adversary and his minions arrive."
    "Suddenly, the call of a dread horn. Too late!"
    "The knight hears it too."
    "unknown" "To arms, men, protect the King with your life!"
    "We form a protective ring around the King, as the wretched forces of the Adversary descend upon us. Flying beasts with glowing eyes and fiery breath, hulking, crawling behemoths with skin like steel, chitinous footmen that scream at us in their alien tongue. They are trying to capture us alive, but we won't let them, we all know what they do to captives. We fight to the death, for the King! I raise my bow and take a foot soldier through the eye, and see Andres fall, a poison barb in his neck. Capian is taken down with a raw shock of power by one of their mages. I feel a sting in my neck, and see that I am the only one left standing, save for the King himself. He fights with the force of a typhoon, felling foul beasts left and right, ripping the behemoths to shreds with his mighty sword, even cutting a flyer from the sky, but they are too many. He falls, his body pierced with dozens of metal barbs. My tears are the last thing I see as the world turns dark."
    
    "{color=#d7dbe2}{b}????{/b}{/color}"
    "RthgEtTn Dra'k! NoR MoStdyX!"
    "A figure dressed in writhing shadows, its tongue demonic. The Adversary."
    "I will never betray my King! Begone, cruel revenant."
    "SRoTn, caBn yoEu heaWr meU?"
    "Not shadows. Black fabric. Wait, I think I'm beginning to understand..."
    "Son, do you understand me? Can you tell me who you are?"
    "I am Veron Pennoren, proud scout of the-"
    "No, that isn't right-"
    "unknown" "I... I'm Vernon Penn, sir. I think."
    "The man smiles, he seems relieved."
    "I think this one is going to be okay. Leave him here for now, let him recuperate. I'll arrange for some class-Bs. Everything is going to be alright, son, Just lie down and relax. It's over."
    "Yeah, that sounds like a good idea."

    "{color=#d7dbe2}{b}Sunday, 07:00{/b}{/color}"
    "Last shift is finally over. I can't believe it's been six months already. Time to leave this dirt hole behind and finally catch that plane. I can't believe they paid me so much just to sit on my ass and stare at a fence."
