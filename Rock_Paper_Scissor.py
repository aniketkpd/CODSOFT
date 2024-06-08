#  Rock-Paper-Scissors Game

from random import randint

again = True
while again:
    computer_choice = randint(1,3)
    print("\n\tComputer has chosen its choice\n\tIts your Turn...")
    print("\n\tEnter Your Choice:\n\t1 - [Rock]\n\t2 - [Paper]\n\t3 - [Scissor]")
    user_choice = int(input("\n\tChoice : "))

    if user_choice == 1:    
        if computer_choice == 1:
            print("\n\ttie! Computer also chosed Rock.")
        elif computer_choice == 2:
            print("\n\tYou loss! Computer Chosed Paper.")
        elif computer_choice == 3:
            print("\n\tYou Win! Computer Choses Scissor.")
    
    elif user_choice == 2:
        if computer_choice == 1:
            print("\n\tYou Win! Computer Choses Rock")
        elif computer_choice == 2:
            print("\n\ttie! Computer also chosed Paper.")
        elif computer_choice == 3:
            print("\n\tYou loss! Computer Chosed Scissor.")

    elif user_choice == 3:  
        if computer_choice == 1:
            print("\n\tYou loss! Computer Chosed Rock.")
        elif computer_choice == 2:
            print("\n\tYou Win! Computer Choses Paper")
        elif computer_choice == 3:
            print("\n\ttie! Computer also chosed Scissor.")
    
    user_choice_again = input("\n\tWant to play again [Y] or [N] : ")
    if user_choice_again == "Y" or user_choice_again == "y":
        again = True
    elif user_choice_again == "N" or user_choice_again == "n":
        again = False

else:
    print("\n\tThe game has ended...")