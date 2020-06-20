from random import randint
from time import sleep, strftime
from os import getlogin
 
# ASCII ART
welcome = """

 =====================================================================

  ╦═╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔═╗╔═╗╔═╗╦═╗  ╔═╗╔═╗╦╔═╗╔═╗╔═╗╦═╗  ╔═╗╔═╗╔╦╗╔═╗
  ╠╦╝║ ║║  ╠╩╗  ╠═╝╠═╣╠═╝╠═╝║╣ ╠╦╝  ╚═╗║  ║╚═╗╚═╗║ ║╠╦╝  ║ ╦╠═╣║║║║╣ 
  ╩╚═╚═╝╚═╝╩ ╩  ╩  ╩ ╩╩  ╩  ╚═╝╩╚═  ╚═╝╚═╝╩╚═╝╚═╝╚═╝╩╚═  ╚═╝╩ ╩╩ ╩╚═╝

  Dari    : Muhammad Afif Abroory
  Website : afifabroory.github.io

 =====================================================================
"""

scissor = """  
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
"""

rock ="""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___) 
"""

paper ="""
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
""" 

# Global Variable
win = 0
draw = 0
lose = 0
playingTime = 0
getPcName = getlogin()
getTime = strftime("%c")

# User Guide
userGuide ="""  
       +------------------------------------------------+
       |  Panduan Pengguna:                             |
       |    Ketik '1' untuk memilih Scissor (Gunting).  |
       |    Ketik '2' untuk memilih Rock (Batu).        |
       |    Ketik '3' untuk memilih Paper (Kertas).     |
       |    Ketik 'Q' untuk keluar permainan.           |
       +------------------------------------------------+

"""

print(welcome)
print(userGuide)

# Asking user to play or not
startMenu = input(" $ SIAP UNTUK BERMAIN GAME [Y/T]? ").lower()
print("")

if startMenu == "y":
  while True:

    # Get Random from computer
    randomNumber = randint(1,100)

    if randomNumber <= 33:
      computer = scissor

    elif randomNumber <= 66:
      computer = rock

    elif randomNumber <= 100:
      computer = paper



    # Get user input
    player = str(input(" > Pilih ['1', '2', '3','Q']: ")).lower()

    if player == "1":
      player = scissor

    elif player == "2":
      player = rock

    elif player == "3":
      player = paper

    elif player =="q":
      print("""
 +==========INFO===========+
 | Total Seri    :{:>8} |
 | Total Menang  :{:>8} |
 | Total Kalah   :{:>8} |
 | Total Bermain :{:>8} |
 +=========================+""".format(draw,win,lose,playingTime))
      confirm = input("\n $ Yakin keluar? Tekan Y untuk keluar ENTER untuk lanjut: ").lower()
      if confirm == "y":
        with open("Log.txt", "a") as f:
          print("PC-NAME: {} - {}".format(getPcName,getTime), file=f)
          print(""" +==========INFO===========+
 | Total Seri    :{:>8} |
 | Total Menang  :{:>8} |
 | Total Kalah   :{:>8} |
 | Total Bermain :{:>8} |
 +=========================+\n""".format(draw,win,lose,playingTime), file=f)
        print("\n BYE! :)")
        sleep(1.5) 
        break
      else:
        print("")
        continue


    else:
      print("\n INPUT '{}' SALAH!".format(player.upper()))
      print(userGuide)
      continue  



    # Game Rules
    if computer == player:
      print("\n\n Player:\n {}\n           Vs. \n\n Computer:\n {}\n\n HASIL: SERI!\n\n".format(player, computer))
      playingTime += 1
      draw += 1

    elif player == scissor and computer == paper:
      print("\n\n Player:\n {}\n           Vs. \n\n Computer:\n {}\n\n HASIL: PLAYER MENANG!\n\n".format(player, computer))
      playingTime += 1
      win += 1

    elif player == rock and computer == scissor:
      print("\n\n Player:\n {}\n           Vs. \n\n Computer:\n {}\n\n HASIL: PLAYER MENANG!\n\n".format(player, computer))
      playingTime += 1
      win += 1

    elif player == paper and computer == rock:
      print("\n\n Player:\n {}\n           Vs. \n\n Computer:\n {}\n\n HASIL: PLAYER MENANG!\n\n".format(player, computer))
      playingTime += 1
      win += 1

    else:
      print("\n\n Player:\n {}\n           Vs. \n\n Computer:\n {}\n\n HASIL: PLAYER KALAH!\n\n".format(player, computer))
      playingTime += 1
      lose += 1
