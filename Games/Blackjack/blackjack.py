from helper import *


def black_jack():
    playing = True

    while True:
        # Print an opening statement
        print('Welcome to BlackJack!\n\
            Get as close to 21 as you can without going over!\n\
            Dealer hits until she reaches 17. Aces count as 1 or 11.\n\
            You have 100 chips per game i.e. Chips will reset after every game')

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's chips
        chips = Chips()

        # Prompt the Player for their bet
        take_bet(chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            playing = hit_or_stand(deck, player_hand, playing)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 16:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(chips)

            else:
                push()

        # Inform Player of their chips total
        print('\n Player total Chips Remaining: ', chips.total)

        # Ask to play again
        new_game = input("\nDo you want to play again? Enter 'y' or 'n': ")
        if new_game.lower() == 'y':
            playing = True
            continue
        else:
            print('Thanks for playing')
            break


if __name__ == "__main__":
    black_jack()
