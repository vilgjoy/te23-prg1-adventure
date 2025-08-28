import time

def typewriter(text, delay=0.1):
  for letter in text:
    print(letter, end='', flush=True)
    time.sleep(delay)
  print()

def welcome_message():
    while True:
        answer = input("""
                        Hail brave adventurer! 
                        Welcome to the land of Pythonia where great challenges await you and even greater rewards if you still stand to claim them. 
                        Choose wisely and keep your wits about you as many dangers, puzzles and riddles stand between you and glory. 
                        Let us begin! (begin/no thanks)""")
        if answer.lower().strip() == "begin":
            return
        elif answer.lower().strip() == "no thanks":
            print("Kind of defeats the purpose of this whole thing, but hey, its your life! It's now or never, you ain't gonna win this endeavour!")
            exit()
        else:
            print("Invalid input for begin/no thanks choice. Please try again.")

def welcome_message_v2():
        answer = input ("""
                        Back so soon, adventurer?
                        The lands of Pythonia can certainly be a challenge.
                        Perhaps a certain change of choice can help you overcome your challenge?
                        (continue)""")
                            
        #if answer.lower().strip() == "try again":
        
def welcome_message_v3():
        answer = input ("""
                        Ah, well done adventurer! A nice little hoard you've gathered.
                        Yet something tells me you yearn for a much larger success.
                        Perhaps a more methodical approach will yield a greater return?
                        (continue)""")

def welcome_message_v4():
        answer = input ("""
                        Well, well, well!
                        Someone has their eyes on the prize!
                        Your ambition knows no bounds!
                        Let us hope your patience is equally as abundant as your desire...
                        (continue)
                        """)
        #return weapon_choice()

def welcome_message_v5():
        answer = input ("""
                        Congratulations! 
                        You overcame the challenge of the bone forest and obtained all possible gems!
                        With all three gems you now have as much wealth as a dragon's hoard at your disposal!
                        Will you buy your own kingdom and rule as a king?
                        Live out the rest of your days in peace and comfort?
                        Or will you take up the mantle of adventurer and venture forth into Pythonia for another challenge?
                        (continue)""")
        return one_path_choice()

def weapon_choice():
    while True:
        answer = input("""
                        As a fame-hungry adventurer you plan to journey to the outskirts of lesser known lands for fortunes beyond your wildest dreams.
                        In preparation for your journey what equipment do you bring to defend yourself?

                        1) A mace which is engraved with the words 'bone cruncher' in its handle
                        2) A staff with a bright blue crystal which radiates sunlight at your command
                        Which do you choose? 
                        (mace/staff)""").lower().strip()
        if answer.lower().strip() == "mace":
            weapon = "mace"
            print("Excellent choice! With your {} in hand you journey on to adventure.".format(weapon))
            return weapon
        elif answer.lower().strip() == "staff":
            weapon = "staff"
            print("Excellent choice! With your {} in hand you journey on to adventure.".format(weapon))
            return weapon
        else:
            print("Invalid choice, perhaps the life of an adventurer is not for you!")

def path_choice():
    while True:
        path = input("""
                        Before you stands two paths - each extremely dangerous yet equally as lucrative.
                        To your left is a dark and dense forest - its trees a pale white with leaves of blood red.
                        To your right stands a castle long known to be abandoned, with an unnatural darkness surrounding its tall, slender parapets.
                        Which path do you take? (dense forest/dark castle)""").lower().strip()
        
        if path == "dense forest".lower().strip():
            return "dense forest"
        elif path == 'dark castle'.lower().strip():
            return "dark castle"
        else:
            print("Invalid path choice. Please try again.")

def one_path_choice():
    while True:
        one_path_choice = input("""
                        Before you stands one path - at its end is a castle long known to be abandoned, with an unnatural darkness surrounding its tall, slender parapets.
                        (continue)""")
        if one_path_choice == "continue".lower().strip():
            return dark_castle()
        else:
            print("Invalid path choice. Please try again.")

def dense_forest(weapon):
    while True:
        print("""
                        You grip your {} firmly and venture carefully into the forest.
                        As you walk past the tree line you hear a faint rattling sound.
                        Checking every angle you spot no sudden movements.""".format(weapon))
            
        forest_approach = input("Do you wish to proceed slow and steady or go in {} blazing? (slow and steady/{} blazing)".format(weapon, weapon)).lower().strip()
        if forest_approach == "slow and steady".lower().strip():
            return slow_and_steady(weapon)
        elif forest_approach == "{} blazing".format(weapon).lower().strip():
            return weapon_blazing(weapon)
            
        else:    
            print("Invalid choice. Please try again.")

def dark_castle():
    print("""
                        You venture down the path leading to the Dark castle.
                        As you approach the dark, blocky structure the chill in the air begins to bite into your skin.
                        After sometime you find the castle's arched main entry towering above you.
                        However being this close something immediately seems off...

                        As you inspect the castle in greater depth, a great gust of wind blows into the castle - to your surprise the castle collapses in on itself!
                        It appears the castle was a facade - made of cardboard which lies on the ground in front of you completely flat.
                        Where the castle once stood sits a man, with a glowing cube on a table in front of him.
                        He appears to be in a deep state of equal parts concentration and frustration as his finger runs against the cube, inscribing runes within.
                        
                        "If...then elif...unexpected indent?
                        What does this bug mean? Argh, it keeps looping without going to the next step?!
                        How is this defined again?"

                        Before you can attempt to decipher his crazed mutterings, he suddenly looks up in shock as he notices you.
                        "A-ah hello! You've caught me unaware - lets just say this is under construction. Let me see if I can't sort this out."
                        His hands begin to rapidly enter runes into the cube.
                        "Typewriter and time delay is a nice touch...then it just needs to loop back...
                        Hope this wo-
            """)
    print("3...")
    time.sleep(1)  
    print("2...")
    time.sleep(1) 
    print("1...")
    time.sleep(1)
    return welcome_message() 
    #try_again_flag = True
    
#try_again_flag = False

def slow_and_steady(weapon):
    while True:
        print("""
                        You decide a slow, tactical approach through the forest is best.
                        As you absorb your surroundings you notice some of the pale white trees have words marked into them.
                        "Head...missing...please...help"
                        As you follow this trail of words you hear a soft rattling sound as you approach a clearing.
                        You quietly approach and spot a skull-less skeleton sitting atop stone, bent over with its hand curled in a fist, pressed against its neck bone.
                        It appears deep in thought.""")
        response_to_skeleton = input("(ambush the skeleton/reason with the headless skeleton)")
        if response_to_skeleton == "reason with the headless skeleton".lower().strip():
            return reason_with_skeleton_slow()
        elif response_to_skeleton == "ambush the skeleton".lower().strip():
            return ambush_the_skeleton(weapon)
        
    else:
        print("Invalid choice. Please try again.")

def reason_with_skeleton_slow():
    while True:
        print("""
                        Recalling the messages you read on the way here, you take a neutral stance and raise your hands to the skeleton in a non-threatening manner.
                        You explain you mean the skeleton no harm.
                        It jumps up out of its deep thought and cautiously approaches you.
                        Before you know it, it wraps its arms around you...and embraces you tenderly, rattling its bones slightly.
                        You let out a sigh of relief.
                        The skeleton begins to mime slowly and thoughtfully, repeatedly pointing at the empty space where a skull would usually be.
                        """)
        reason_with_skeleton_slow_choice = input("(tell the skeleton to get lost/offer to help find its head)")
        if reason_with_skeleton_slow_choice.lower().strip() == "tell the skeleton to get lost":
            return tell_skeleton_get_lost()
        if reason_with_skeleton_slow_choice.lower().strip() == "offer to help find its head":
            return offer_to_help_find_its_head()

def tell_skeleton_get_lost():
    while True:
        print("""
                        You are sick of this skeleton and tell it to promptly get out of your sight.
                        It stands there for a moment with its hands clasped together in what you can only assume is an attempt at swaying you with puppy dog eye-sockets.
                        However, as it is missing its skull it has little effect.
                """)
        tell_skeleton_get_lost_choice = input("(abandon skeleton and continue)")
        if tell_skeleton_get_lost_choice.lower().strip() == "abandon skeleton and continue":
            return abandon_skeleton_continue()


def ambush_the_skeleton(weapon):
    while True:
        print("""
                        You use the element of surprise to your advantage and bring your {} down fiercely into the shoulderblade of the skeleton. 
                        It crumples to the floor as your hit catches it unaware.
                """.format(weapon))
        ambush_the_skeleton_choice = input("(bring it with you/abandon skeleton and continue)")
        if ambush_the_skeleton_choice.lower().strip() == "bring it with you":
            return bring_with_you()
        if ambush_the_skeleton_choice.lower().strip() == "abandon skeleton and continue":
            return abandon_skeleton_continue()
        

def offer_to_help_find_its_head():
    while True:
        print("""
                        You explain you will help to find its skull.
                        The skeleton jumps up in joy and claps its hands excitedly.
                        It grabs your hand and begins striding forward.
                        You feel its sharp bones press into your hand and you smile awkwardly as you try to ignore the pain.

                        As you journey together for sometime the skeleton stops in front of a tree and begins scratching a message into a tree:
                        "In trio, the gems you seek,
                        To claim them all, a rite unique.
                        A humble stance on bended knee,
                        The secret lies in sets of three.

                        In sockets deep, a touch you'll lend,
                        Where sight once dwelt, and words descend.
                        A gentle grasp, the skull you'll hoist,
                        Complete the frame with care and poise.

                        Reunite what once was sundered,
                        And witness then the gems unencumbered."

                        You scratch your head as you try to decipher the meaning behind this, as you ask the skeleton.
                        It shrugs and continues forward.
                """)
        continue_with_skeleton = input("(continue with skeleton)")
        if continue_with_skeleton.lower().strip() == "continue with skeleton":
            after_continuing()
            break
    else:
        print("The skeleton eagerly awaits you to make a sensible move - try again")

def after_continuing():
    while True:
        print("""
                        Not long after this cryptic exchange you see a faint shimmer of light coming from the ground in the distance.
                        As you approach it you see a magnificent crown with three eye-watering gems atop a skull.
                        What do you do?""")
        after_continuing = input("""
                (grab just the crown)
                (grab skull and crown)
                (put a finger in one eysocket)
                (put a finger in two eyesockets)
                (kneel down on one knee)
                (kneel down on two knees)
        """)
        if after_continuing.lower().strip() == "grab just the crown":
            return just_the_crown_v2()
        elif after_continuing.lower().strip() == "grab skull and crown":
            return skull_and_crown_v2()
        elif after_continuing.lower().strip() == "put a finger in one eyesocket":
            return put_a_finger_in_one_eyesocket()
        elif after_continuing.lower().strip() == "put a finger in two eyesockets":
            return put_a_finger_in_two_eyesockets()
        elif after_continuing.lower().strip() == "kneel down on one knee":
            return kneel_down_on_one_knee()
        elif after_continuing.lower().strip() == "kneel down on two knees":
            return kneel_two_knees()

def put_a_finger_in_one_eyesocket():
    while True:
        print("""You place a finger in one of the skull's eyesockets.
        """)
        put_a_finger_in_one_eyesocket_choice = input("(continue)")
        if put_a_finger_in_one_eyesocket_choice.lower().strip() == "continue":
            return skull_and_crown_v2()

def put_a_finger_in_two_eyesockets():
    while True:
        print("""
                You place a finger in two of the skull's eyesockets.
        """)
        put_a_finger_in_two_eyesockets_choice = input("(continue)")
        if put_a_finger_in_two_eyesockets_choice.lower().strip() == "continue":
            return skull_and_crown_v2()

def just_the_crown_v2():
    while True:
        print("""
                        You grab the crown only, eager to get your hands on the valuable looking jewels.
                        As you go to touch the cool metallic surface of the golden crown, you instantly feel a jolt of pain circulate throughout your whole body.
                        The skulls jaw begins to flap:
                        "I see you went for the crown without bothering to put my skull back. Bold, but not very wise. However, I'm feeling generous since you brought my body back, so I'll let this slide. But don't push your luck – I won't be so bone-evolent next time!"
                        The skeletal body walks you to the edge of the forest as you remain paralysed in fear while gripping the crown.
                        The skull stares at you the entire time, its jaw flapping as it giggles.
                        As you enter the edge of the forest the skeleton body takes the skull from your grasp, waves at you goodbye and leaves you empty handed.
        """)
        just_the_crown_v2 = input("The End...? (continue)")
        if just_the_crown_v2.lower().strip() == "continue":
            return welcome_message_v2()

def kneel_two_knees():
    while True:
        print("""You drop to both knees and kneel before the skull and crown. 
        """)
        kneel_two_knees_choice = input("(skull and crown/just the crown)")
        if kneel_two_knees_choice.lower().strip() == "skull and crown":
            return skull_and_crown_v2()
        elif kneel_two_knees_choice.lower().strip() == "just the crown":
            return just_the_crown_v2()

def skull_and_crown_v2():
    while True:
        print("""
                        You pick up the skull and the crown. The skeleton claps excitedly behind you.

                        The skull's jaw begins to flap away:
                        "Well, well, look who's become a bone-a-fide hero! 
                        I was on the verge of becoming a real bonehead without my body – thank you for bringing it back! 
                        The head bone's connected to the neck bone - I'm ready!")""")
        skull_and_crown_v2_choice = input("(return skull to body/extort for gems)")
        if skull_and_crown_v2_choice.lower().strip() == "return skull to body":
            return return_skull_to_body_v2()
        elif skull_and_crown_v2_choice == "extort for gems":
            return extort_for_gems()
            
        else:
            input("The skull awaits impatiently for a valid input")

def return_skull_to_body_v2():
    while True:
        print("""
                        You place the head on the skeletal body standing by your side.
                        A satisfying click sound echoes throughout the forest as the skeleton begins stretching out his long lost body.

                        "Being whole again is a real breath of fresh air – or it would be if I still had lungs! 
                        Here are two gems for your troubles. I'm sure they'll come in handy when you're not busy playing osteopath."

                        The skeleton prys out 2 gems from his crown, blue and red.
                        It extends its hand out to you.

                        As you take the gems the skeleton takes one final bow and snaps his fingers.
                        You find yourself at the edge of the forest, with gems in hand.
                        The riches these gems will afford should make you almost as rich as a king...
                        Yet your mind wonders...what's a king without a fully gemmed crown?
                                """)
        return_skull_to_body_v2_choice = input("(try again)")
        if return_skull_to_body_v2_choice.lower().strip() == "try again":
            return welcome_message_v4()
            
def extort_for_gems():
    while True:
        print("""
                        You tell the skull to not get a-head of itself and explain you have all the leverage here and that you will return it to its body once you have the gems.
                        "You're really ribbing me here!
                        I guess its true what they say: diamonds are a ghoul's best friend!
                        Very well you may have all of my gems, simply yank them out of the crown and they are yours."
                """)
        extort_for_gems_choice = input("(pull jewels out)")
        if extort_for_gems_choice.lower().strip() == "pull jewels out":
            return just_the_crown()



def kneel_down_on_one_knee():
    while True:
        print("""
                        You drop down to one knee and kneel before the skull and crown.What next?""")
        kneel_down_on_one_knee_choice = input("""
                (put a finger in one eyesocket)
                (put a finger in two eyesockets)
                (put a finger in two eyesockets and its mouth)""")
        if kneel_down_on_one_knee_choice.lower().strip() == "put a finger in one eyesocket":
            return skull_and_crown_v2()
        elif kneel_down_on_one_knee_choice.lower().strip() == "put a finger in two eyesockets":
            return skull_and_crown_v2()
        elif kneel_down_on_one_knee_choice.lower().strip() == "put a finger in two eyesockets and its mouth":
            return put_a_finger_in_two_eyesockets_and_its_mouth()

def put_a_finger_in_two_eyesockets_and_its_mouth():
    while True:
        print("""
                        With a finger in each each eyesocket and another in its mouth, you are poised to lift the skull.
                        What do you do?
                """)
        put_a_finger_in_two_eyesockets_and_its_mouth_choice = input("""
                (return the skull to its body gently)
                (return the skull to its body aggressively)
                (throw the skull with all your might far away into the forest)""")
        if put_a_finger_in_two_eyesockets_and_its_mouth_choice.lower().strip() == "return the skull to its body gently":
            return return_skull_to_body_v3()
        elif put_a_finger_in_two_eyesockets_and_its_mouth_choice.lower().strip() == "return the skull to its body aggressively":
            return return_skull_to_body_aggresive()
        elif put_a_finger_in_two_eyesockets_and_its_mouth_choice.lower().strip() == "throw the skull with all your might far away into the forest":
            return throw_skull_into_forest()

def throw_skull_into_forest():
    while True:
        print("""
                        With the skull firmly in your grasp you summon all your strength to throw it as deep into the forest as far as you can.
                        You hear a shout emenating from the skull:
                        "By the phalanges! Your treachery knows no bounds, you calcium deficient deliquent! Hope you're ready for a boney boomerang......"
                        As you slap your hands together watching the skull fly away with satisfaction you feel the tender embrace of the skeleton hug you once more.
                        At first you recognise it as a sign of gratitude from the skeleton from freeing it from the servitude of its skull master, until you find it hard to breathe.
                        With the grip getting tighter the last thing you feel before you pass out is the ribcage slicing into your back.
                """)
        throw_skull_into_forest_choice = input("The End...(continue)")
        if throw_skull_into_forest_choice.lower().strip() == "continue":
            return welcome_message_v2()

def return_skull_to_body_v3():
    while True:
        print("""
                        While on one knee, you gently lift the skull and place it back onto the skeleton's neckbone.
                        You hear a soft click as the skull settles in place.
                        The skull begins to glow and its jaw starts to move:
                        "You have my sincerest gratitude. I was worried I'd be left in pieces, but you've given me a new lease on death.
                        Thanks for proving that not all adventurers are boneheads. You've got some real bone-marrow!
                        For this, I shall give you a skeleton key to my heart...and a few priceless gems!"
                        The skeleton places his hand on the crown and runes light up across its golden surface.
                        After a few seconds they disappear and the gems fall into the skeleton's hand.
                        He places them in your hand then hugs you.
                        You hear a click of bone against bone.
                        You find yourself outside of the forest - a green, blue and red gem in hand securing a path to your wildest dreams.
                """)
        return welcome_message_v5()


def return_skull_to_body_aggresive():
    while True:
        print(""""
                        With a firm grip of the skull you use your strength to aggressively smash the skull back into place atop the skeletons neck.
                        The newly formed skeleton takes a step back as a click followed by a crunch echoes through the forest as the skull is reattached.
                        Your fist slips with the excessive force sending chips of bone flying away from its shoulderblade.
                """)
        return_skull_to_body_aggresive_choice = input("(continue)")
        if return_skull_to_body_aggresive_choice.lower().strip() == "continue":
            return return_skull_to_body()

def return_skull_to_body():
    while True:
        print("""
                        The skeleton comes to life and picks itself up and dusts itself off.
                        It looks at its shoulderblade where you had attacked previously.
                        "You've left me with a chip on my shoulder, but I'll still reward you with one of my crown jewels"
                        The skeleton pulls out the blue gem from the crown and hands it to you.
                        It waves to you and says "Bone voyage! Maybe we'll cross bones again in another loop!"
                        Before you can try to piece together what that means the skeleton snaps his fingers and you find yourself standing outside the forest with the blue gem sparkling in your hands.
                        Success! The riches from this gem should last you for quite sometime but you can't help but wonder what your future would look like with more gems in your possession.
                """)
        return_skull_to_body_choice = input("(try again)")
        if return_skull_to_body_choice.lower().strip() == "try again":
            return welcome_message_v3()


def weapon_blazing(weapon):
    while True:
        print("""
                        Fortune favours the bold you tell yourself as you grip your {} in hand and charge head first into the forest.
                        The sound of rattling grows louder - do you look up at the trees or ground level to try and identify the source of the sound? 
                        """.format(weapon))
        view_forest = input("(look up at the trees/look around at ground level)").lower().strip()
        if view_forest.lower().strip() == "look up at the trees":
            return look_up_at_the_trees()
        elif view_forest.lower().strip() == "look around at ground level":
            return look_at_ground_level(weapon)

def look_at_ground_level(weapon):
    while True:
        print("""
                        You look towards your immediate surroundings, barely slowing down while avoiding the hazards underfoot.
                        The sound of rattling grows louder as you spot movement far ahead of you.
                        Do you call out to the source of movement or prepare for battle?
                """)
        look_at_ground_level = input("(call out/prepare to fight)").lower().strip()
        if look_at_ground_level.lower().strip() == "call out":
            return call_out(weapon)
        elif look_at_ground_level.lower().strip() == "prepare to fight":
            return prepare_to_fight(weapon)
        else:
            print("Invalid choice - please try again")

def call_out(weapon):
    while True:
        print(""""
                        Who goes there?!"
                        You shout out confidently.
                        From the source of movement you see red bushes part to reveal a head-less skeleton appear, its pearl-white bones radiating an unnatural light.
                        It pantomimes grabbing the space above its neck over and over again before charging towards you. 
                        Do you prepare to fight or attempt to reason with the charging, head-less skeleton?
                """)
        call_out_choice = input("(prepare to fight/reason with the headless skeleton)")
        if call_out_choice.lower().strip() == "prepare to fight":
            return prepare_to_fight(weapon)
        elif call_out_choice.lower().strip() == "reason with the headless skeleton":
            return reason_with_skeleton_v2()
        else:
            print("Invalid choice - hurry and try again!")

def reason_with_skeleton_v2():
    while True:
        print(""""
                        Against your better judgement, you take a neutral stance and raise your hands to the skeleton in a non-threatening manner.
                        You explain you mean the skeleton no harm.
                        It stops in its tracks and you lets out a sigh of relief - at least thats what you think it tries to do, considering it has no lungs.
                        The skeleton cautiously approaches you and begins to frantically mime, repeatedly pointing at the empty space where a skull would usually be.
                    """)
        reason_with_skeleton_v2_choice = input("(tell the skeleton to get lost/bring it along to search for its skull)")
        if reason_with_skeleton_v2_choice.lower().strip() == "tell the skeleton to get lost":
            return tell_skeleton_get_lost()
        if reason_with_skeleton_v2_choice.lower().strip() == "bring it along to search for its skull":
            return bring_along_to_search()

def bring_along_to_search():
    while True:
        print("""
                        You feel sorry for this assortment of bones and invite it to journey along with you through the forest.
                        The skeleton claps its hands together in excitement and bows to you, ready to follow.
                        Do you travel in silence or attempt to make small talk with this skull-less skeleton?
                """)
        bring_along_to_search_choice = input("(travel in silence/make small talk)")
        if bring_along_to_search_choice.lower().strip() == "travel in silence":
            return travel_in_silence()
        if bring_along_to_search_choice.lower().strip() == "make small talk":
            return make_small_talk()

def make_small_talk():
    while True:
        print("""
                        You begin to talk to the skeleton, hoping to get any information out of it.
                        Through a series of motions it mimes pointing at its head, lifting an imaginary hat off of it and then making an X with its skeletal arms.
                        It then points slightly lower than where the hat would be if it had a skull, and points aggressively at the space its skull would be, then gives you a thumbs up.

                        Before you can piece together this crpytic clue you spot something shiny...
                """)
        make_small_talk_choice = input("(approach the shiny)")
        if make_small_talk_choice.lower().strip() == "approach the shiny":
            return something_shiny_v2()
        else:
            print("The silence between the skeleton and you is deafening...best to give a valid input to proceed!")

def travel_in_silence():
    while True:
        print("""
                        You're not in the mood for a game of skeleton charades.
                        You continue through the forest in silence, the rattling of the skeleton's company as it walks behind you the only reminder it is still here.
                """)
        travel_in_silence_choice = input("(aprroach the shiny)")
        if travel_in_silence_choice.lower().strip() == "approach the shiny":
            return something_shiny_v2()

def something_shiny_v2():
    while True:
        print("""
                        As you continue to venture through the forest you begin to lose track of your surroundings as seconds turn to minutes turn to hours.
                        Just as you are ready to declare yourself lost you see a glimmer of light reflect of something in the distance.
                        As you approach it you see a magnificent crown with three eye-watering gems atop a skull.
                        Do you pick up the skull and crown or just the crown?
                """)
        something_shiny_v2_choice = input("(skull and crown/just the crown)")
        if something_shiny_v2_choice.lower().strip() == "skull and crown":
            return skull_and_crown_v2()
        if something_shiny_v2_choice.lower().strip() == "just the crown":
            return just_the_crown_v2()

def prepare_to_fight(weapon):
    while True:
        print("""You raise your {} and charge at the skeleton""".format(weapon))
        
        if weapon == "staff":
            print("""
                        You target your staff's sunlight at the skeleton's bones - it bounces off with no effect.
                        As you meet you attempt to swing the staff down into its shoulder. 
                        Your staff gets lodged into its shoulderblade. 
                        Before you can pry it out, the skeleton takes a step back, moves its neck bone to point directly at you and plunges it directly through your heart.""")
            return welcome_message_v2()
        elif weapon == "mace":
            print("""
                        You grip your mace and shield tightly as you charge towards the skeleton.
                        As you meet you swing the mace down with a surge of adrenaline-fuelled speed into the skeleton's shoulderblade.""")
            time.sleep(2) 
            print("""   
                        CRUNCH""")
            time.sleep(2)  
            print("""   
                        A loud crunch echoes through the forest as your bone-splintering blow causes the skeleton to fall to the floor, motionless.
                        Do you abandon the skeleton here and continue on or attempt to disassemble its pieces and bring it with you?
                        """)
            fight_outcome = input("(abandon skeleton and continue/bring it with you)")
            if fight_outcome.lower().strip() == "abandon skeleton and continue":
                return abandon_skeleton_continue()
            elif fight_outcome.lower().strip() == "bring it with you":
                return bring_with_you()
            

def bring_with_you():
    while True:
        print("""
                        You attempt to disassemble its pieces however some unknown force keeps it together.
                        Using rope from your inventory you tie it up and bring it with you.
                """)
        bring_with_you_choice = input("(continue)")
        if bring_with_you_choice.lower().strip() == "continue":
            return something_shiny()
        else:
            print("You're in a strange forest carrying a hostle skeleton...should probably make a valid input real soon")

def something_shiny():
    while True:
        print("""
                        As you continue to venture through the forest you begin to lose track of your surroundings as seconds turn to minutes turn to hours.
                        Just as you are ready to declare yourself lost you see a glimmer of light reflect of something in the distance.
                        As you approach it you see a magnificent crown with three eye-watering gems atop a skull.
                        Do you pick up the skull and crown or just the crown?
            """)
        something_shiny = input("(skull and crown/just the crown)")
        if something_shiny.lower().strip() == "just the crown":
            return just_the_crown()
        elif something_shiny.lower().strip() == "skull and crown":
            return skull_and_crown()

def skull_and_crown():
    while True:
        print("""
                        You grab the crown by its skull and inspect it.
                        Your reflection stares back at you from each of the gems, taking on a blue, green and red tinge from the sapphire, emerald and ruby respectively.
                        Suddenly the skull's jaw begins to move:
                        "Well that was certainly a long dirt nap!
                        You've got a real head for treasure hunting!
                        Looks like you've got quite the eye-socket for finding lost things.
                        Thank you for returning my body - its certainly a weight off my shoulders, or rather, back on them!"
                """)
        skull_and_crown_choice = input("(untie the body to return to the skull/extort for gems)")
        if skull_and_crown_choice.lower().strip() == "untie the body to return to the skull":
            return return_skull_to_body()
        elif skull_and_crown_choice.lower().strip() == "extort for gems":
            return extort_for_gems()

def just_the_crown():
    while True:
        print("""
                        The crown's gems are too tantalising to resist as you reach out to touch the crown.
                        You attempt to lift it from the skull with no success, with some sort of force keeping it stuck.
                        As you realise this you are instantly paralysed with pain as the gems embedded in the crown begin to glow.
                        The skull's jaw begins to flap as you hear the skull say:
                        "Well it's about time my luck turned around, stuck in my forest with nobody!
                        Your paralysis is quite humerus, but I'm afraid it's time for me to deal with you.
                        What a shame, you even brought my body back to me!
                        You've gone from bone-thief to bone-stiff, although I will reward you for bringing my body back to me. I'll make it quick!"
                        The head drops from the crown and uses its jaw to bite-climb its way up to its body tied to your back.
                        It breaks free from your ropes as you helplessly watch it adorn the crown and stay true to its word as it plunges its fist through your torso.
                """)
        just_the_crown = input("The End...(continue)")
        if just_the_crown.lower().strip() == "continue":
            return welcome_message_v2()


def abandon_skeleton_continue():
    while True:
        print("""
                        You have had enough of this skeleton and never want to see another bone again, so you abandon it.
                        As you continue to venture through the forest you begin to lose track of your surroundings as seconds turn to minutes turn to hours.
                        Just as you are ready to declare yourself lost you see a glimmer of light reflect of something in the distance.
                        As you approach it you see a magnificent crown with three eye-watering gems atop a skull.
                """)
        abandon_skeleton_continue = input("(pick up the crown, ignoring the skull)")
        return pick_up_crown_ignore_skull()

def pick_up_crown_ignore_skull():
    while True:
        print("""
                        The crown's gems are too tantalising to resist and you are done dealing with bones so you reach out to touch the crown.
                        You attempt to lift it from the skull with no success, with some sort of force keeping it stuck.
                        As you realise this you are instantly paralysed with pain as the gems embedded in the crown begin to glow.
                        The skull's jaw begins to flap as you hear the skull say:
                        "Well my luck sucks and I'm still stuck in my forest with nobody!
                        Your paralysis is quite humerus, but I'm afraid it's time for me to deal with you.
                        What a shame, you come here empty handed and stiff-spined, way to rub it in!
                        The head drops from the crown and uses its jaw to bite-climb its way up to your neck.
                        "My apologies for biting you, but I'm feeling a bit 'dis-jointed' after being apart from my body for so long!"

                        You feel its jaw sink into your neck as you pass out from the pain.
                """)
        pick_up_crown_ignore_skull = input("The End...? (try again)")
        if pick_up_crown_ignore_skull.lower().strip() == "try again":
            try_again_flag = True
            return welcome_message_v2()
            break
try_again_flag = False

def look_up_at_the_trees():
    while True:
        print("""
                        You swear that the sound came from up above within the trees. 
                        You slow down slightly while tilting your head back to try to see through the dark red patches of leaves overhead.
                        Your legs suddenly give way as you trip over a white root of a tree, as gravity guides your face to the earth below.
                        You taste an ash like consistency in your mouth - you raise your head as the rattling sound grows louder and blinking through the ash in your eyes you have a moment to see the moonlight reflect off a skull-less skeleton charging at you.
                        Before you can get to your feet, the skull-less skeleton launches itself into the air and brings both of its knees down into your back.
                        You hear the sounds of bones crack and a sudden surge of pain brings a terrifying realisation that those cracked bones are yours.
                        You are knocked out from the severity of the injury, your fate left to the whims of the forest.
        """)
        look_up_at_the_trees = input("The End...(continue)").lower().strip()
        if look_up_at_the_trees.lower().strip() == "continue":
            try_again_flag = True
            return welcome_message_v2()
            

#def look_at_ground_level():

#def offer to help find its head

def main():
    global try_again_flag
    first_time = True
    weapon_chosen = None
    
    while True:
        if first_time:
            welcome_message()
            first_time = False
        elif try_again_flag:
            try_again_flag = False
        else:
            if welcome_message_v2() is None:
                continue

        if not weapon_chosen:
            weapon_chosen = weapon_choice()
            
        path = path_choice()
       

        if path == "dense forest": #if player chooses dense forest under path option then...
            forest_approach = dense_forest(weapon_chosen) #give them forest approach option under dense_forest function
                        
        elif path == "dark castle":
            dark_castle()
            # Add more code for the dark castle story path here.

        if try_again_flag:
            continue

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no)").lower().strip()
        if play_again == "no":
            print("Yeah treasure isn't that cool anyway - thanks for playing!")
            break
        elif play_again == "yes":
            try_again_flag = True
            weapon_chosen = None
        else:
            print("Invalid path choice. Try again!")

if __name__ == "__main__":
    main()