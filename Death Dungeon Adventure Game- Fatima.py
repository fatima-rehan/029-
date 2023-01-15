
#Name: Fatima Rehan
#Student#: 342605409
#Date: 12/01/2022
#File: AdventureGame.py
#Purpose: Creates a text-based adventure game, called "Death Dungeon" 

import time #import time, to allow time sleep, between iterations
guards_uniform = 0 #variable for guards uniform object

print("Welcome to Death Dungeon!")
name = input("What is your name?: ") #name variable for user to be part of the game
print("\nHello", name,", you are guilty of a murder you did not commit, and are to be beheaded tomorrow at noon...")
print("Your objective is to escape the dungeon, before your timely death. Be aware of guards and traps\n") #\n for formatting, to move text to the next line

print("Are you ready to escape the Death Dungeon?: ") #Outputs text to user
question = "invalid"
while question != "yes" or question != "no": #while loop to allow user to input an appropriate answer to start the game
    question = input("Type \"yes\" or \"no\": ") #yes/no statement to start the game
    if question == "yes" or question == "no":
        break

if question == "yes":
     print("\nYou are currently in a locked cell. The cell's previous habitant has made holes in the cells to the East, West, and South\n")

elif question == "no":
    print("You've been beheaded!..Try again.\nENDING 1/13") #13 endings, to show user how many they have gone through
    quit()

direction = ["East", "West", "South"] #first direction variables (compass)
print("From the East cell, you can hear squeaking noises...and smell cheese?..\n")
time.sleep(3) 
print("From the West cell, you can only hear dead silence...and smell a rotting scent?..\n")
time.sleep(3) 
print("From the South cell, you can hear sizzling...wait...it's radiating extreme heat!..\n")
time.sleep(3) 
print("Which cell would you like to enter? (East, West, South):") 

userInput = input() #Multiple choice input statements
if userInput == "East":
    print("You have entered the East cell, to be greeted with flesh eating monstrous rats!")
    print("            (\,;,/)              ") #first ascii character 
    print("             (o o)\//,           ") #Art by ikas (https://ascii.co.uk/art/rat)
    print("              \ /     \,         ")
    print("              `+'(  (   \    )   ")
    print("                 //  \   |_./    ")
    print("               '~' '~----'       ")
    time.sleep(3) 
    print("You put up a tough fight, but the rats killed you..Try again.\nENDING 2/13")
    quit()
     
elif userInput == "South":
    print("You have entered the South cell, only to have fallen into a pool of hot LAVA!")
    print("           (  .      )                       ") #Art by Joan G. Stark (jgs) 
    print("        )           (              )         ") #(https://ascii.co.uk/art/fire)
    print("              .  '   .   '  .  '  .          ")
    print("     (    , )       (.   )  (   ',    )      ")
    print("      .' ) ( . )    ,  ( ,     )   ( .       ")
    print("   ). , ( .   (  ) ( , ')  .' (  ,    )      ")
    print("  (_,) . ), ) _) _,')  (, ) '. )  ,. (' )    ")
    print(" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ")
    time.sleep(3)
    print("You have painfully died, drowning in the pool of lava..Try again.\nENDING 3/13")
    quit()

elif userInput == "West":
    print("You have entered the West cell, there, you see the corpse of what seems to be a dungeon guard.")
    question = input("Would you like to steal the guards' uniform off his corpse? (yes/no): ") #object will be guards uniform that will be used after
    if question == "yes":
        guards_uniform += 1
        print("You are now dressed as a dungeon guard..I hope this wards off suspicion.\n")
    elif question == "no": 
        print("You are still dressed as a dungeon prisoner.\n")
        guards_uniform += 2
    
    print("It seems that the previous habitant of this cell has dug a tunnel out.")
    question = input("Will you crawl through this tunnel? (yes/no): ")
    if question == "yes":
        print("It took a while, but you have crawled through the narrow tunnel..at the end of the tunnel you see a staircase, which you climb.")
    if question == "no":
        print("You decided to stay in this cell, you have been beheaded with an extra blunt axe..Try again.\nENDING 4/13")
        quit()

print("You have reached the top of the staircase, to be met with a crossroad.\n") 
direction = ["North", "East"]
userInput = input("Which direction would you like to go? (East,North): ") #This crossroad will result in one shorter, and one longer ending

if userInput == "East":
        print("You have decided to enter the East hall..you continue on the way until your path is obstructed.")
        time.sleep(3)
        print("You seem to be blocked by a enormous pool of rapid moving water.\nYou also see a swinging, unsecured wooden bridge.")
        question = input("Would you like to swim through the water, or cross the wooden bridge? (swim/cross): ")
        if question == "swim":
            print("You have entered the water, to be attacked by vicious piranha!")
            print("          ,---,         ") #Art by pb (https://ascii.co.uk/art/piranha)
            print("  _    _,-'    `--,     ")
            print(" ( `-,'            `\   ")
            print("  \           ,    o \  ")
            print("  /   ,       ;       \ ")
            print(" (_,-' \       `, _  ""/")
            print("        `-,___ =='__,-' ")
            print("              ````      \n")
            print("The piranha killed you, leaving no evidence..Try again.\nENDING 5/13")
            quit()
        elif question == "cross":
            print("You have carefully crossed the wooden bridge, despite it's hectic swinging.")
            time.sleep(3) 

        print("You have now entered a dungeon corner room...to the side of the room you see a soft luscious bed.") 
        print("     ()___                      ") #Art by Joan G. Stark (jgs) 
        print("    ()//__/)_________________() ") #(https://ascii.co.uk/art/bed)
        print("    ||(___)//#/_/#/_/#/_/#()/|| ")
        print("    ||----|#| |#|_|#|_|#|_|| || ")
        print("    ||____|_|#|_|#|_|#|_|#||/|| ")
        print("    ||    |#|_|#|_|#|_|#|_||    \n")
        question = input("You are very tired..will you sleep in this bed? (yes/no): ")
        if question == "yes":
            print("You overslept!!!\nThe guards found you sleeping, and impaled you in bed..Try again.\nENDING 6/13")
            quit()
        if question == "no":
            print("Although you were tired, you pushed through and continued on your way to the main hall of the dungeon.")
        time.sleep(3)
        print("You see two doors in the main hall, one of these doors is the exit.")
        direction = ["East", "West"]

        print("Which door will you enter? (East/West): ")
        userInput = input()
        if userInput == "West":
            print("You have entered the inner doorway of the dungeon..there you see a guard!!")
            time.sleep(3)
        if guards_uniform == 1 : #if you have the guards uniform variable from earlier (TRUE), you can pass
            print("The guard saw your uniform, and let you through the gate")
            time.sleep(3)
            print("       * *                     ") #Art by Joan G. Stark (jgs)
            print("            *    *  *          ") #(https://www.asciiart.eu/plants/other)
            print("       *  *    *     *  *      ")
            print("      *     *    *  *    *     ")
            print("  * *   *    *    *    *   *   ")
            print("  *     *  *    * * .#  *   *  ")
            print("  *   *     * #.  .# *   *     ")
            print("   *     #.  #: #  * *    *     ")
            print("  *   * *  #. ##*       *      ")
            print("    *        ###               ")
            print("              ##               ")
            print("               ##.             ")
            print("               .##:            ")
            print("              :###             ")   
            print("             ,####.            ")
            print(" /\/\/\/\/\/.######.\/\/\/\/\  ")   
            print("You have now escaped the dungeon, run as fast as you can, as far as you can", name,"!!!") #This ending, wins the game
            print("ENDING 7/13")
            quit()

        elif guards_uniform == 2: #if you don't have the guards uniform (FALSE) the game ends
            print("The guard saw you and choked you to death..Try again.\nENDING 8/13")
            quit()

        elif userInput == "East":
            print("You crawled through another tunnel at the foot of the door, you have been transported to your original cell.")
            print("You made it in time for your death..you've been aggressively beheaded..Try again.\nENDING 9/13")
            quit()

if userInput == "North": #Going North results in a longer storyline, but ultimately the same ending
    print("You have decided to enter the North hall...You continue on you way until you see a room to your right.")

    question = input("This room has red spots at its entrance, would you like to enter? (yes/no): ")
    if question == "yes":                                                                                                                 
        print("You have entered the execution room!")
        print(".___________________.   ") #Art by lgbeard (0jo)
        print("|`._______________,'|   ") #https://www.asciiart.eu/weapons/guillotines
        print("| |               | |   ")
        print("| |_______________| |   ")
        print("| ||             || |   ")
        print("| ||_   _        || |   ")
        print("| || ""--._._    || |   ")
        print("| ||       `-.   || |   ")
        print("| ||          `. || |   ")
        print("| ||            \|| |   ")
        print("| ||             || |   ")
        print("| ||             || |   ")
        print("| ||             || |   ")
        print("| ||             || |   ")
        print("| ||             || |   ")
        print("| ||             || |   ")
        print("| ||             || |   ")
        print("| ||_____________|| |   ")
        print("| |/     ,--.    \| |   ")
        print("| |-(_)-(    )-(_)| |   ")
        print("| |      `--'     | |   ")
        print("|===================|   ")
        print("|                   |   ")
        print("You must have been eager to die, you've been beheaded!..Try Again\nENDING 10/13")
        quit()

    elif question == "no":
        print("You continued North, until you entered another room.\nIt is the beautiful princess' chambers..and you see her sleeping!")
        time.sleep(3)
    question = input("Would you like to wake her up for help, or leave the room?(wake/leave): ")
    if question == "wake":
        print("You have awoken the beautiful princess, who immediately screamed and pulled out a knife.\n")
        print("                     (,);        ...     ") #Art by  @-;----- Valkyrie 
        print("                    ((  ^_.     (()))    ") #(http://loveascii.com/princess.html)
        print("                     ' / /_\    {' ())   ")
        print("                       L( '}     )_ (()  ")
        print("                         ) (_    (   (_) ")
        print("                      (_  / }{)===='_/   ")
        print("                       | `/\/\     |   \ ")
        print("                      L___/ |     |    | ")
        print("                       |  . \     |    | ")
        print("                       |_/ \_\    |    | ")
        print("                       ( ____ )   |    | ")
        print("                        | | | |   |    | ")
        print("                    ( --' | \ |_  '~~~~' ")
        print("                    /_/---) (___)  _/Y   ")
        print("She has stabbed you in the heart..Try again.\nENDING 11/13")
        quit()

    elif question == "leave": 
        print("You have left the beautiful princess' room, and went East on your way")
    time.sleep(3)
    print("You continued down the East hall, until you see yet another room on your right")
    question = input("You hear muffled voices from the room, wil you enter? (yes/no): ")
    if question == "yes":
        print("You have entered the Guards quarters, to see the dungeon guards staring at you!")
        print("      |\                |\                |\                |\        ") #Art by Joan G. Stark (jgs)
        print("   || .---.          || .---.          || .---.          || .---.     ") #(https://www.asciiart.eu/weapons/soldiers)
        print("   ||( '.' )         ||( '.' )         ||( '.' )         ||( '.' )    ")
        print("   || \_-_/_         || \_-_/_         || \_-_/_         || \_-_/_    ")
        print("   :-)`'V'//-.       :-)`'V'//-.       :-)`'V'//-.       :-)`'V'//-.  ")
        print("  / ,   |// , `\    / ,   |// , `\    / ,   |// , `\    / ,   |// , ` ")
        print(" / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |")
        print("/_/||__//   || |  /_/||__//   || |  /_/||__//   || |  /_/||__//   || |")
        print("\ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |")
        print(" \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |")
        print(" /\|_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |")
        print("`--|*******||_|   `--|*******_|   `--|`^*******_|   `--|`^*******|")
        print("   |   |   ||/       |   |   ||/       |   |   ||/       |   |   ||/ ")
        print("   |   |   |         |   |   |         |   |   |         |   |   |   ")
        print("   |   |   |         |   |   |         |   |   |         |   |   |   ")
        print("   |   |   |         |   |   |         |   |   |         |   |   |   ")
        print("   L___l___J         L___l___J         L___l___J         L___l___J   ")
        print("    |_ | _|           |_ | _|           |_ | _|           |_ | _|    ")
        print("   (___|___)         (___|___)         (___|___)         (___|___)   ")
        print("    ^^^ ^^^            ^^ ^^^           ^^^ ^^^           ^^^ ^^^    ")
        print("They took turns stabbing you..Try again\ENDING 12/13")
        quit()
    if question == "no":
     print("You ignored you curiosity, and continued down the hall, until you entered the dungeon corner room.")
     time.sleep(3)
     print("There you see a large feast!")
     print("  ;)( ;                ") #Art by Hayley Jane Wakenshaw
     print(" :----:     o8Oo./     ") #(https://www.asciiart.eu/food-and-drinks/coffee-and-tea)
     print("C|====| ._o8o8o8Oo_.   ")
     print(" |    |  \========/    ")
     print(" `----'   `------'     ")
    question = input("You are very hungry, will you eat it? (yes/no): ")
    if question == "yes":
        print("You have decided to eat the large feast, which put you in a deep slumber.")
        print("The guards found you asleep, and killed you!..Try again\nENDING 13/13) #This is the final possible ending, the rest are repeated")
    
    if question == "no":
        print("Although you were hungry you ignored the feast, and continued to the main hall of the dungeon.")
        time.sleep(3)
        print("You see two doors in the main hall, one of these doors is the exit")
    direction = ["East", "West"]

    print("Which door will you enter? (East/West): ")

    userInput = input()
    if userInput == "West":
     print("You have entered the inner doorway of the dungeon..there you see a guard!!")
    time.sleep(3)
    if guards_uniform == 1 :
        print("The guard saw your uniform, and let you through the gate.")
        time.sleep(3)
        print("       * *                     ") #Art by Joan G. Stark (jgs)
        print("            *    *  *          ") #(https://www.asciiart.eu/plants/other)
        print("       *  *    *     *  *      ")
        print("      *     *    *  *    *     ")
        print("  * *   *    *    *    *   *   ")
        print("  *     *  *    * * .#  *   *  ")
        print("  *   *     * #.  .# *   *     ")
        print("   *     #.  #: #  * *    *     ")
        print("  *   * *  #. ##*       *      ")
        print("    *        ###               ")
        print("              ##               ")
        print("               ##.             ")
        print("               .##:            ")
        print("              :###             ")   
        print("             ,####.            ")
        print(" /\/\/\/\/\/.######.\/\/\/\/\  ") 
        print("You have now escaped the dungeon, run as fast as you can, as far as you can", name,"!!!")
        print("ENDING 7/13")
        quit()

    elif guards_uniform == 2:
        print("The guard saw you and choked you to death..Try again.\nENDING 8/13")
        quit()

    elif userInput == "East":
        print("You crawled through another tunnel at the foot of the door, you have been transported to your original cell.")
        print("You made it in time for your death..you've been aggressively beheaded..Try again.\nENDING 9/13")
        quit()