import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
while True:
    computer=random.randint(0, 2)
    you=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
    print(you)
    if you==0:
        print("   _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n")
    elif you==1:
        print("    _______\n"
        "---'   ____)____\n"
        "          ______)\n"
        "          _______)\n"
        "         _______)\n"
        "---.__________)\n")
    elif you==2:
            print("    _______\n"
            "---'   ____)____\n"
            "          ______)\n"
            "       __________)\n"
            "      (____)\n"
            "---.__(___)\n")
    else:
        print("INVALID Choice.")
        continue
    print(f"Computer choose: ")

    if computer==0:
        print("   _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n")
    elif computer==1:
        print("    _______\n"
        "---'   ____)____\n"
        "          ______)\n"
        "          _______)\n"
        "         _______)\n"
        "---.__________)\n")
    elif computer==2:
        print("    _______\n"
        "---'   ____)____\n"
        "          ______)\n"
        "       __________)\n"
        "      (____)\n"
        "---.__(___)\n")

    if(computer==you):
        print("Draw.\nPress any button to play and win!\nPress q to quit!")
        press=input()
        if(press=='q'):break
    elif computer==0:
        if you==1:
            print("You Win!")
            break
        elif you==2:
            print("You loose!")
            break
    elif computer==1:
        if you==0:
            print("You loose!")
            break
        elif you==2:
            print("You Win!")
            break
    elif computer==2:
        if you==0:
            print("You win!")
            break
        elif you==1:
            print("You loose!")
            break