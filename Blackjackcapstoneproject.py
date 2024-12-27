import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def low_computer_score(cards_list, list_score):
    another_computer_card = random.sample(cards, 1)
    reference_computer = sum(cards_list) + another_computer_card[0]
    if (11 in another_computer_card and cards_list) and reference_computer > 21:
        another_computer_card[0] = 1
    list_score += sum(another_computer_card)
    cards_list.append(another_computer_card[0])
    return cards_list, list_score
def dealer_turn(dealer_cards, score):
    while score < 17:
        example_list = low_computer_score(dealer_cards, score)
        score = example_list[1]
    return score
#user_score=total_score, cards_user=user_cards, computer_cards=machine_cards, computer_score=machine_score
def print_final_score(user_cards_de, user_score, machine_cards, machine_score):
    if user_score == 21 and len(user_cards_de) == 2:
        print(f"Your final hand: {user_cards_de}, final score: {user_score}")
        print(f"Computer's final hand: {machine_cards}, final score: {machine_score}")
        print("You Won with a Blackjack! 😎🤑🫡")
    elif machine_score == 21 and len(machine_cards) == 2:
        print(f"Your final hand: {user_cards_de}, final score: {user_score}")
        print(f"Computer's final hand: {machine_cards}, final score: {machine_score}")
        print("Machine Won with a Blackjack! 🤐😮😔")
    elif user_score > 21 and machine_score < 21:
        print(f"Your final hand: {user_cards_de}, final score: {user_score}")
        print(f"Computer's final hand: {machine_cards}, final score: {machine_score}")
        print("You Went Over! 🤣🤣")
    elif machine_score > 21 and user_score < 21:
        print(f"Your final hand: {user_cards_de}, final score: {user_score}")
        print(f"Computer's final hand: {machine_cards}, final score: {machine_score}")
        print("Computer Went Over! You Win 😁")
    elif user_score < machine_score:
        print(f"Your final hand: {user_cards_de}, final score: {user_score}")
        print(f"Computer's final hand: {machine_cards}, final score: {machine_score}")
        print("You Lose 🤦‍♂️😒")
    elif user_score ==  machine_score:
        print(f"Your final hand: {user_cards_de}, final score: {user_score}")
        print(f"Computer's final hand: {machine_cards}, final score: {machine_score}")
        print("It's a Draw! 😮🤔")
    else:
        print(f"Your final hand: {user_cards_de}, final score: {user_score}")
        print(f"Computer's final hand: {machine_cards}, final score: {machine_score}")
        print("You Win, Congrats! 😎😉")


def looping():
    user_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)
    current_score = user_cards[0] + user_cards[1]
    computer_score = computer_cards[0] + computer_cards[1]
    # print logo import logo from art
    print("\n" * 25)
    print(logo)
    print(f"Your cards: {user_cards}, current score: {current_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    def continuing():
        continue_game = input("Type 'y' to  get another card, type 'n' to pass: ").lower()
        nonlocal current_score
        if continue_game == "y":
            another_card = random.sample(cards, 1)
            reference = current_score + another_card[0]
            if (11 in another_card and user_cards) and reference > 21:
                another_card[0] = 1
            user_cards.append(another_card[0])
            current_score = sum(user_cards)
            if current_score > 21:
                print(f"Your final hand: {user_cards}, final score: {current_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You Went Over! 🤣🤣")
                starting_game()
            elif current_score == 21:
                computer_final_score = dealer_turn(computer_cards, computer_score)
                print_final_score(user_cards, current_score, computer_cards, computer_final_score)
                starting_game()
            else:
                print(f"Your cards: {user_cards}, current score: {current_score}")
                print(print(f"Computer's first card: {computer_cards[0]}"))
                continuing()


        elif continue_game == "n":
            computer_final_score = dealer_turn(computer_cards, computer_score)
            print_final_score(user_cards, current_score, computer_cards, computer_final_score)
            starting_game()
        else:
            print("Wrong value 'IDIOT'!")
            continuing()
    continuing()
#construct a while loop
def starting_game():
    start_game = input("Do you want to play a game of blackjack, Type 'y' or 'n': ").lower()
    if start_game == "y":
        looping()
    elif start_game == "n":
        print("Good Bye, Have a nice day ☺️")
    else:
        print("Wrong Input!")

starting_game()
