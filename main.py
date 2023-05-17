print('''
*******************************************************************************
                                   ___
                                   T T
                                   ===
                                   |.|
                                  .'.`.
                                .'.' `.`.
                  %%          .'.' ___ `.`.
                 %%%%       .'.'  |_|_|  `.`.
                %%%%%%    .'.'    |_|_|    `.`.
                %%%%%__.--`'| []  |_|_|  [] |`'---.
__              %%%%|------||               |||||||
 /\     =========%%%|    _&||      ___      ||===='
/  \   ///////////H/| j |  ||     |_|_|     ||    |
||||  ////////////H%|   |- ||     |_|_|     ||____|
|||| /////////////H/|   |  ||     |_|_|     ||  TT|       .   &
|||| @@@@@@@@@@@@@H@|======||               ||====|  "==='   (f
|\//|\/|/\//\||//|\|||/\//|//\||\//||//|\||\||\/|/\//\||////|//\/||
                                        
*******************************************************************************
''')
print("Welcome to 'The Cabin'")
print("In this game, you and your friends are put in a life or death scenario in which you have to make the best decisions to save your and your friends' life. BE AWARE! YOUR DECISIONS HAVE CONSEQUENCES! can you save everyone from the cabin or will you be the only survivor? or will nobody survive? you are about to find out.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print('''
*******************************************************************************
''')
#Write your code below this line 👇

print ("Your friend Lili texted the group chat inviting everyone for a 'trip to paradise'. She says she won 5 tickets to a cute cabin out in the west.")
down_to_go = input("Are you down to go?\n")
if down_to_go.lower() == "yes":
  print('''

       ''')
  print("On the drive to the place, you guys hit a deer. Tom says that you should leave it and drive on but Shelly suggest you guys move it out of the road so another car won't crash into it.")
  deer_crash= input("who do you agree with?\n")
  if deer_crash.lower() == "shelly":
    print('''

       ''')
    get_gas= input("Lili says that you guys should get more gas just in case you run out later. Do you agree?\n")
    if get_gas.lower() == "yes":
      print('''

       ''')
      tell_friends= input("You guys get to the cabin safely and meet the owners that are living across you. You notice he seems a bit odd and suspect he's up to something. Will you tell your friends?\n")
      if tell_friends.lower() == "yes":
        print('''

       ''')
        print("The owner is the killer and you let your friends know about your suspecion. That night, you see him entering tom's room to kill tom while he's sleeping.")
        help_tom= input("what will you do? a) wake up everyone and save Tom. b) go save Tom by yourself c) pretend you don't see it.\n")
        if help_tom.lower() == "a":
          print('''
          
          ''')
          print("You guys are saved Tom and are now trying to run away from the killer.")
          which_way= input("Which way do you guys run to? left or right?\n")
          if which_way.lower() == "right":
            print("You guys took the wrong turn and fell into a ditch causing everyone to die.")
          else:
            print('''
            
            ''')
            print("you guys took the correct turn and reached your car.")
            who_drives= input("Who do you let drive the car? Shelly, Tom, Lili, Matt or yourself?\n")
            if who_drives.lower() == "shelly" and deer_crash.lower() == "shelly":
              print("Since you listened to shelly before and moved the deer, you guys safely escape the cabin. CONGRATS, YOU WON THE GAME!")
            elif who_drives.lower() == "tom":
              print("You didn't listen to tom and moved the deer but tom is a bad driver and he crashed, killing everyone. GAME OVER!")
            elif who_drives.lower() == "lili":
              print("lili was able to drive you and all your friends to safety. CONGRATS, YOU WON THE GAME!")
            elif who_drives.lower() == "matt":
              print("matt is a bad driver and he crashed it, killing everyone. GAME OVER!")
            else:
              print("You drove all you friends to safety and was able to escape the cabin. CONGRATS, YOU WON THE GAME!")
                    
              
              
              
        elif help_tom.lower() =="b":
          print("You couldn't save Tom by yourself. You and Tom both were killed. GAME OVER!")
        else:
          print("After Tom was killed, all your friends were also killed off one by one. Only you escaped the cabin.")
        
        
      else:
        print("You didn't let you friends know in time and the he killed them all. Only you were able to escape.")
        
    else:
      print("You guys didn't have enough gas to escape the cabin. The killer found you all and killed every one of you. GAME OVER!")
  else:
    print("You guys didn't move the deer and when you were trying to escape the cabin, crashed into it and the car exploded. Everyone in the car died. GAME OVER!")
    
else:
  print("Your friends are angry because you never join them anymore. They called you boring. GAME OVER!")





