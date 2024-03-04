
import time
import sys

# Initial variables
bravery_points = 5
falls = 0
pick_up_question_answered = False
walk_in_darknes = False
reached_doors = False

backpack = [
    "Flashlight", 
    "Pillow", 
    "Snack"
    ]
door_keyes = {
    1:"\nMaybe it's better this way\n", 
    2:"\nWe'd hurt each other with the things we'd want to say\n",
    3:"\nTonight the music seems so loud\n", 
    4:"\nI wish that we could lose this crowd\n"
    }
all_keys_done = False
all_keys = ["1", "2", "3", "4"]
done_keys = []
# The welcome senquence



print(
    """
Be brave and the prize will be yours!
            
===================

Answer questions with Y for Yes, and N for No.. Altough sometimes you will need to be more creative.    
      
===================
      
Your adventure begins now! 
"""
)

# Here the narrative begins
time.sleep(2)
print(
    "You find yourself in a very dark place. It is so dark that you can't see even tip of your nose. You don't know where are you.. You don't know why you are here.. \n"
)
time.sleep(2)


print("You hear loud snorgin somewhere in the room.. \n")
time.sleep(2)


print("Zzzzzzzz...zzzzzz..\n")
time.sleep(2)


print("Zzzzz...zzz..\n")
time.sleep(2)



while True:
    question_step = input("Do you want to take a step forward? (Y/N): ").upper()
    if question_step == "Y":
        time.sleep(2)
        bravery_points += 1
        print("Clang!!!! \n")
        time.sleep(2)
        print("You trip on something, causing a loud bang!!!..\n")
        time.sleep(2)
        print("..the sound echoes, for what it feels like, ages.. You realise that the room is huge..\n")
        time.sleep(2)
        print("You noticed that the snoring has spotted..\n")
        time.sleep(2)
        print("You hear a loud grumble.. GghhhhHHHHmmmmRrrrrrrrrmmmmm...\n")
        time.sleep(2)
        print("You hear deep voice calling from the depths of darkness..\n")
        
        question_who = input("'Who is distrubing my sleep?' ")
        time.sleep(1)
        print(f"\n'Who is that \"{question_who}\"?!..'\n")
        time.sleep(2)
        print("'..actually, I don't care..'\n")
        time.sleep(2)
        print(
            "Large dragon head appears just in front of you.. Small flames coming from its nose lighten it up..\n"
        )
        time.sleep(3)
        print(
            "'You look like a small human.. I like humans.. You taste excellent when deep fried..'\n"
        )
        time.sleep(1)
        print(
            "Trmebling from fear you look around for escape.. but all that you can see is a large sword..\n"
        )
        question_sword = input("Do you pick up the sword? (Y/N) ").upper()
        if question_sword == "Y":
            time.sleep(2)
            bravery_points += 1
            print("\n'You think that you can fight me?! With this tiny sword?! Brave little human!'\n")
            time.sleep(1)
            print("'I'm not going to eat you! I just wanted to scare you.. You people taste terrible since the XX. century!\n")
            time.sleep(1)
            player_name = input("'Whats is your name, little one?' ")
            time.sleep(1)
            print(f"\n\'Well.. {player_name.title()}.. I will be happy if you will see yourself out.\'\n")
            time.sleep(1)
            print("'I want to go back to sleep, these early hours at my dragonschool are killing me..'\n")
            time.sleep(1)
            print("'..I would love to come back to the simple times when ravaging villages was a way to support a life of a dragon just like me..'\n")
            time.sleep(1)
            print("'Wait a minute! I AM A DRGAON!! I CAN TRAVEL IN TIME!!\n")
            time.sleep(1)
            print("Before you even understood what happened you hear loud: ZIP ZAP ZOOP BIT BOOP!!!\n")
            time.sleep(1)
            print("The whole room lightens up for a splitsecond and the large dragon vanishes in front of your eyes.\n")
            time.sleep(1)
            print("In the flash of light you see small doors in the far end of the room.\n")
            time.sleep(3)
            print("You are confused, you are stanading there alone in the darkness, having no idea what has just happened.\n")
            time.sleep(2)
            print("You slowly realise that you have to do something, this situation won't resolve itself.\n")
            time.sleep(2)
            print("You feel backpack straps on your shoulders.\n")
            time.sleep(2)
            print("You remember the doors in the far corner.\n")
            while True:
                question_first_action = input("\nWhat do you do? 'Search bag'? 'Walk' forward in hopes of reaching the doors? 'Cry' from desperation? ").capitalize()
                if question_first_action == "Search bag":
                    time.sleep(2)
                    bravery_points += 1
                    print(f"\nIn your backpack you see: {backpack}\n")
                    while True:
                        question_item = input("Which of item do you choose? ").capitalize()
                        time.sleep(1)
                        if question_item == "Flashlight":
                            bravery_points += 2
                            time.sleep(2)
                            print("\nYou turn on the light. You can finally see something!\n")
                            time.sleep(2)
                            print("With the flashlight on you can finally navigate through the darkness of the dragon's lair.\n")
                            time.sleep(2)
                            while True:
                                action_light_on = input("What do you do? 'Look around' or 'walk' towards the doors you seen earlier? ").capitalize()
                                if action_light_on == "Look around":
                                    time.sleep(2)
                                    print("\nYou see the vastness and emptiness of the dragon's lair. There are few copper coins lying around.. and large boxes everywhere.. This dragon must have spent all his gold.. You wonder what on..\n")
                                if action_light_on == "Walk":
                                    time.sleep(2)
                                    print("\nYou avoid large box of KFC, the size of laundry machine.\n")
                                    time.sleep(2)
                                    print("..and another one..\n")
                                    time.sleep(2)
                                    print("aaaandd one more..\n")
                                    time.sleep(2)
                                    print("...yet another one...\n")
                                    time.sleep(2)
                                    print("It becomes clear where all the gold went.\n")
                                    time.sleep(2)
                                    print("Further down the way towards the doors you see on the floor a vinyl album, it's 'Make It Big' by George Michael.\n")
                                    while True:
                                        if pick_up_question_answered == True:
                                                time.sleep(2)
                                                while True:
                                                        if all_keys_done == False:
                                                            pressed_key = input("\nWhich of the keys do you press? (1/2/3/4)\n")
                                                            if pressed_key == "1":
                                                                time.sleep(1)
                                                                print(door_keyes[1])
                                                                done_keys.append("1")             
                                                            elif pressed_key == "2":
                                                                time.sleep(1)
                                                                print(door_keyes[2])
                                                                done_keys.append("2")
                                                            elif pressed_key == "3":
                                                                time.sleep(1)
                                                                print(door_keyes[3])
                                                                done_keys.append("3")
                                                            elif pressed_key == "4":
                                                                time.sleep(1)
                                                                print(door_keyes[4])
                                                                done_keys.append("4")
                                                            else:
                                                                time.sleep(1)
                                                                print("There are only keys 1/2/3/4")
                                                            for key in all_keys:
                                                                if all(key in done_keys for key in all_keys):
                                                                    all_keys_done = True
                                                        if all_keys_done == True:
                                                            time.sleep(2)
                                                            print("You are surprised by what just happened..\n")
                                                            time.sleep(1)
                                                            print("You realise you need to presse the buttons in the correct order..\n")
                                                            time.sleep(1)
                                                            while True:
                                                                door_answer = input("Input correct key order to unlock the doors.\n")
                                                                if door_answer == "3412":
                                                                    time.sleep(1)
                                                                    print("Carless Whipsers by George Michael starts to play loudly.\n")
                                                                    time.sleep(2)
                                                                    print("..what the hell..\n")
                                                                    time.sleep(1)
                                                                    print("Doors swing open. Outside light blinds you. you feel the breez of fresh air\n")
                                                                    time.sleep(3)
                                                                    print("THE END of demo ver.! Congratulations, adventurer!\n")
                                                                else:
                                                                    print("\nINCORRECT\n")
                                        pick_up_question = input("Do you pick up the album? (Y/N) ").capitalize() 
                                        if pick_up_question == "Y":
                                            time.sleep(1)
                                            print("\nYou pick up the album..\n")
                                            time.sleep(1)
                                            print("To your surprise under the album there is a large golden coin!\n")
                                            backpack.append(["Album", "Golden coin"])
                                            time.sleep(1)
                                            print("You hide the album and the golden coin in your backpack and continue walking.\n")
                                            time.sleep(1)
                                            print("Finally you've reached the doors.\n")
                                            time.sleep(1)
                                            print("You are disspoainted to see that these aren't regular doors. There is no door handle.\n")
                                            time.sleep(1)
                                            print("..but there are four piano keys..")
                                            time.sleep(1)
                                            pick_up_question_answered = True
                                        if pick_up_question == "N":
                                            print("You continue walkling towards the doors.\n")
                                            time.sleep(1)
                                            print("Finally you've reached the doors.\n")
                                            time.sleep(1)
                                            print("You are disspoainted to see that thse aren't regular doors. There is no door handle.\n")
                                            time.sleep(1)
                                            print("..but there are four piano keys..\n")
                                            time.sleep(1)
                                            print("..the keys are numbered from 1 to 4..\n")
                                            time.sleep(1)
                                            print("You realize that is some type of lock that can be deactived by the correct password.\n")
                                            time.sleep(1)
                                            pick_up_question_answered = True
                                        else:
                                            print("Answer with yes or no.")
                        elif question_item == "Snack" and "Snack" not in backpack:
                            time.sleep(2)
                            print("\nYou have already ate your snack.")
                        elif question_item == "Snack":
                            bravery_points += 1
                            time.sleep(2)
                            print("\nYou eat a tasty snack! It makes you feel better about upcoming challenges.\n")
                            backpack.remove("Snack")
                        elif question_item == "Pillow":
                            bravery_points -= 1
                            if bravery_points < 1:
                                time.sleep(1)
                                print("\nYou died")
                                sys.exit()
                            else:
                                time.sleep(2)
                                print("\nThis is no time to sleep!\n")
                                question_item
                        else:
                            time.sleep(2)
                            print(f"\nAnswer with any of {backpack}")
                elif question_first_action == "Walk":
                    walk_in_darknes = True
                    bravery_points += 1
                    time.sleep(2)
                    print("\nYou trip on something and fall to the ground.\n")
                    falls += 1
                    if falls > 4:
                        print("You died")
                        sys.exit()
                elif question_first_action == "Cry":
                    bravery_points -= 2
                    if bravery_points < 1:
                        time.sleep(1)
                        print("You died")
                        sys.exit()
                    else:
                        time.sleep(2)
                        print("\nThis no time for crying. Remember to be brave!\n") 
                else:
                    time.sleep(2)
                    print("Answer with 'Search bag' / 'Walk' / 'Cry'.")
        elif question_sword == "N":
                    bravery_points -= 1
                    if bravery_points < 1:
                        time.sleep(1)
                        print("You died")
                        sys.exit
                    else:
                        time.sleep(1)
                        print("You hesitated, your bravery decreased.\n")
                        question_sword
        else:
            time.sleep(1)
            print("Answer with yes or no.")
    elif question_step == "N":
        bravery_points -= 1
        if bravery_points < 1:
            time.sleep(1)
            print("You died")
            sys.exit()
        else:
            time.sleep(1)
            print("You hesitated, your bravery decreased.")
            question_step
    else:
        time.sleep(1)
        print("Answer with yes or no.")     
        question_step




        










