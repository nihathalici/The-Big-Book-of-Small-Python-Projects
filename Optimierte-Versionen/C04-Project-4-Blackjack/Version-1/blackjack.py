"""Blackjack, by Al Sweigart al@inventwithpython.com
The classic card game also known as 21. (This version doesn't have splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, card game"""

import random
import sys
from typing import List, Tuple, Optional

# Set up the constants:
HEARTS = chr(9829)      # '♥'
DIAMONDS = chr(9830)    # '♦'
SPADES = chr(9824)      # '♠'
CLUBS = chr(9827)       # '♣'
BACKSIDE = 'backside'

# Card type alias for better readability
Card = Tuple[str, str]
Deck = List[Card]


def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.''')

    money = 5000
    
    while True:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        print(f'Money: {money}')
        bet = get_bet(money)
        
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        
        print(f'Bet: {bet}')
        
        # Handle player's turn
        player_busted = False
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()
            
            player_value = get_hand_value(player_hand)
            if player_value > 21:
                player_busted = True
                break
            
            move = get_move(player_hand, money - bet)
            
            if move == 'D':
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f'Bet increased to {bet}.')
                print(f'Bet: {bet}')
            
            if move in ('H', 'D'):
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}.')
                player_hand.append(new_card)
                
                if get_hand_value(player_hand) > 21:
                    player_busted = True
                    # Continue to break out of loop after displaying
                    continue
            
            if move in ('S', 'D'):
                break
        
        # Handle dealer's turn (only if player didn't bust)
        if not player_busted:
            while get_hand_value(dealer_hand) < 17:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)
                
                if get_hand_value(dealer_hand) > 21:
                    break
                
                input('Press Enter to continue...')
                print('\n\n')
        
        # Show final hands and determine winner
        display_hands(player_hand, dealer_hand, True)
        
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        
        if dealer_value > 21:
            print(f'Dealer busts! You win ${bet}!')
            money += bet
        elif player_value > 21 or player_value < dealer_value:
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print(f'You won ${bet}!')
            money += bet
        else:
            print("It's a tie, the bet is returned to you.")
        
        input('Press Enter to continue...')
        print('\n\n')


def get_bet(max_bet: int) -> int:
    """Ask the player how much they want to bet for this round."""
    while True:
        print(f'How much do you bet? (1-{max_bet}, or QUIT)')
        bet_input = input('> ').upper().strip()
        
        if bet_input == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        
        if not bet_input.isdecimal():
            continue
        
        bet = int(bet_input)
        if 1 <= bet <= max_bet:
            return bet


def get_deck() -> Deck:
    """Return a list of (rank, suit) tuples for all 52 cards."""
    suits = (HEARTS, DIAMONDS, SPADES, CLUBS)
    ranks = [str(r) for r in range(2, 11)] + ['J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def display_hands(player_hand: Deck, dealer_hand: Deck, show_dealer_hand: bool) -> None:
    """Show the player's and dealer's cards. Hide the dealer's first card if show_dealer_hand is False."""
    print()
    if show_dealer_hand:
        print(f'DEALER: {get_hand_value(dealer_hand)}')
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        display_cards([BACKSIDE] + dealer_hand[1:])
    
    print(f'PLAYER: {get_hand_value(player_hand)}')
    display_cards(player_hand)


def get_hand_value(cards: Deck) -> int:
    """Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1."""
    value = 0
    ace_count = 0
    
    for rank, _ in cards:
        if rank == 'A':
            ace_count += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    
    # Add aces: start with 1 each, then upgrade to 11 if possible
    value += ace_count
    for _ in range(ace_count):
        if value + 10 <= 21:
            value += 10
    
    return value


def display_cards(cards: Deck) -> None:
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', '']
    
    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += f'|{rank:<2} | '
            rows[2] += f'| {suit} |'
            rows[3] += f'|_{rank:>2}| '
    
    print('\n'.join(rows))


def get_move(player_hand: Deck, money: int) -> str:
    """Asks the player for their move, and returns 'H' for hit, 'S' for stand, and 'D' for double down."""
    valid_moves = {
        'H': '(H)it',
        'S': '(S)tand'
    }
    
    # Player can double down on their first move (exactly two cards)
    if len(player_hand) == 2 and money > 0:
        valid_moves['D'] = '(D)ouble down'
    
    while True:
        move_prompt = ', '.join(valid_moves.values()) + '> '
        move = input(move_prompt).upper()
        
        if move in valid_moves:
            return move


if __name__ == '__main__':
    main()
