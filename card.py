#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:43:49 2020

@author: stevenyuan
"""

#define the global variables
HEARTS = 0
DIAMONDS = 1
CLUBS = 2
SPADES= 3

TWO = 0
THREE = 1
FOUR = 2
FIVE = 3
SIX = 4
SEVEN = 5
EIGHT = 6
NINE = 7
TEN = 8
JACK = 9
QUEEN = 10
KING = 11
ACE = 12

def get_suit(card):
    '''
    Given an integer representation of a card, 
    return its suit as an integer between 0 and 3.

    Parameters
    ----------
    card : Int
        representation of a card

    Returns
    -------
    Int
    an integer represented the suit

    >>> get_suit(7)
    2
    >>> get_suit(10)
    1
    >>> get_suit(52)
    3
    '''
    
    suits = (card - 1) % 4
    return suits

    # if have to use the global variable
    #if(suits == HEARTS):
    #    return HEARTS
    #elif(suits == DIAMONDS):
    #    return DIAMONDS
    #elif(suits == CLUBS):
    #    return CLUBS
    #elif(suits == SPADES):
    #    return SPADES
    #
    
def get_rank(card):
    '''
    Given an integer representation of a card, 
    return its rank as an integer between 0 and 12.

    Parameters
    ----------
    card : Int
        an integer representation of a card

    Returns
    -------
    Int
    an integer as the rank

    >>> get_rank(7)
    1
    >>> get_rank(52)
    12
    >>> get_rank(18)
    4    
    '''
    
    rank = (card - 1) // 4
    return rank

    #if have to use the global variables
    #if(rank == TWO):
    #    return TWO
    #elif(rank == 1):
    #    return THREE
    #elif(rank == 2):
    #    return FOUR
    #elif(rank == 3):
    #    return FIVE
    #elif(rank == 4):
    #    return SIX
    #elif(rank == 5):
    #    return SEVEN
    #elif(rank == 6):
    #    return EIGHT
    #elif(rank == 7):
    #    return NINE
    #elif(rank == 8):
    #    return TEN
    #elif(rank == 9):
    #    return JACK
    #elif(rank == 10):
    #    return QUEEN
    #elif(rank == 11):
    #    return KING
    #elif(rank == 12):
    #    return ACE
    
def same_rank(card1, card2):
    '''
    Given two integer card representations, 
    return True if they are both of the same rank, and False otherwise.

    Parameters
    ----------
    card1 : Int
        card representations
    card2 : Int
        card representations

    Returns
    -------
    boolean
    return if the two cards have same rank

    >>> same_rank(1, 3)
    True
    >>> same_rank(1, 52)
    False
    >>> same_rank(50, 52)
    True
    '''
    
    rank1 = get_rank(card1)
    rank2 = get_rank(card2)
    return rank1 == rank2

def same_suit(card1, card2):
    '''
    Given two integer card representations, 
    return True if they are both of the same suit, and False otherwise.

    Parameters
    ----------
    card1 : Int
        card representations
    card2 : Int
        card representations

    Returns
    -------
    boolean
    return if the two cards have same suits

    >>> same_suit(7, 15)
    True
    >>> same_suit(7, 47)
    True
    >>> same_suit(7, 8)
    False
    '''
    suit1 = get_suit(card1)
    suit2 = get_suit(card2)
    return suit1 == suit2

def same_color_suit(card1, card2):
    '''
    Given two integer card representations, 
    return True if they are both of the same color of suit, and False otherwise.

    Parameters
    ----------
    card1 : Int
        card representations
    card2 : Int
        card representations

    Returns
    -------
    boolean
    return if the two cards have same color

    >>> same_color_suit(5, 6)
    True
    >>> same_color_suit(51, 52)
    True
    >>> same_color_suit(5, 7)
    False
    '''
    
    suit1 = get_suit(card1)
    suit2 = get_suit(card2)
    
    red = (suit1 == HEARTS and suit2 == HEARTS) or (suit1 == HEARTS and suit2 == DIAMONDS) or \
        (suit1 == DIAMONDS and suit2 == HEARTS) or (suit1 == DIAMONDS and suit2 == DIAMONDS)
        
    black = (suit1 == CLUBS and suit2 == CLUBS) or (suit1 == CLUBS and suit2 == SPADES) or \
        (suit1 == SPADES and suit2 == CLUBS) or (suit1 == SPADES and suit2 == SPADES)
        
    return red or black

    
if __name__ == '__main__':
    print(same_color_suit(5, 6))
    print(same_color_suit(51, 52))
    print(same_color_suit(5, 7))
    
    