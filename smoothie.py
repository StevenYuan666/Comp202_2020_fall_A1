#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:38:56 2020

@author: stevenyuan
"""



# define the global variables
SMOOTHIE1_NAME = 'Pineapple Banana'
SMOOTHIE2_NAME = 'Almond Basil'
SMOOTHIE3_NAME = 'Purple Surprise'
SMOOTHIE4_NAME = 'Onion Toffee'

SMOOTHIE1_COST = 4.99
SMOOTHIE2_COST = 6.99
SMOOTHIE3_COST = 0.99
SMOOTHIE4_COST = 9.99

SIZE1_NAME = 'small'
SIZE2_NAME = 'medium'
SIZE3_NAME = 'large'
SIZE4_NAME = 'galactic'

SIZE1_COST = -2.0
SIZE2_COST = 0.0
SIZE3_COST = 2.0
SIZE4_COST = 100.0

TOPPING1_NAME = 'no topping'
TOPPING2_NAME = 'cinnamon'
TOPPING3_NAME = 'chocolate shavings'
TOPPING4_NAME = 'shredded coconut'

TOPPING1_COST = 0.0
TOPPING2_COST = 1.0
TOPPING3_COST = 1.0
TOPPING4_COST = 1.0

def pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4):
    '''
    pose the question first, and then list the options and corresponding costs line by line

    Parameters
    ----------
    question : String
        the question posed to user
    option1 : String
        the first option
    cost1 : Float
        the cost of the first option
    option2 : String
        the second option
    cost2 : Float
        the cost of the second option
    option3 : String
        the third option
    cost3 : Float
        the cost of the third option
    option4 : String
        the fourth option
    cost4 : Float
        the cost of the fourth option

    Returns
    -------
    String
    return the choice the user
    
    >>> question = 'Which smoothie would you like?'
    >>> pose_question_with_costs(question, SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, SMOOTHIE2_COST \
                                 ,SMOOTHIE3_NAME, SMOOTHIE3_COST, SMOOTHIE4_NAME, SMOOTHIE4_COST)
    Which smoothie would you like?
    1)	$4.99	Pineapple Banana
    2)	$6.99	Almond Basil
    3)	$0.99	Purple Surprise
    4)	$9.99	Onion Toffee
    Your choice (1-4): 1
    You have selected Pineapple Banana.
    >>> pose_question_with_costs(question, SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, SMOOTHIE2_COST \
                                 ,SMOOTHIE3_NAME, SMOOTHIE3_COST, SMOOTHIE4_NAME, SMOOTHIE4_COST)
    Which smoothie would you like?
    1)	$4.99	Pineapple Banana
    2)	$6.99	Almond Basil
    3)	$0.99	Purple Surprise
    4)	$9.99	Onion Toffee
    Your choice (1-4): 3
    You have selected Purple Surprise.    
    >>> pose_question_with_costs(question, SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, SMOOTHIE2_COST \
                                 ,SMOOTHIE3_NAME, SMOOTHIE3_COST, SMOOTHIE4_NAME, SMOOTHIE4_COST)
    Which smoothie would you like?
    1)	$4.99	Pineapple Banana
    2)	$6.99	Almond Basil
    3)	$0.99	Purple Surprise
    4)	$9.99	Onion Toffee
    Your choice (1-4): 0
    '''

    #display the question first
    print(question)
    
    #display the options and corresponding costs line by line
    print('1)' + '\t' + '$' + str(cost1) + '\t' + option1)
    print('2)' + '\t' + '$' + str(cost2) + '\t' + option2)
    print('3)' + '\t' + '$' + str(cost3) + '\t' + option3)
    print('4)' + '\t' + '$' + str(cost4) + '\t' + option4)
    
    #ask the user's choice and change its type to int
    choice = input('Your choice (1-4): ')
    
    if(choice == '1'):
        print('You have selected ' + option1 + '.')
        return option1
    elif(choice == '2'):
        print('You have selected ' + option2 + '.')
        return option2
    elif(choice == '3'):
        print('You have selected ' + option3 + '.')
        return option3
    elif(choice == '4'):
        print('You have selected ' + option4 + '.')
        return option4
    else:
        return ''
    
def calculate_subtotal(smoothie_type, smoothie_size, topping):
    '''
    Given the type of smoothie, size of smoothie and the topping, calculate the total price

    Parameters
    ----------
    smoothie_type : String
        type of the smoothie
    smoothie_size : String
        size fo the smoothie
    topping : String
        topping the user want to add

    Returns
    -------
    Float
    the price of the inputs

    >>> calculate_subtotal('Pineapple Banana', 'large', 'no topping')
    6.99
    >>> calculate_subtotal('Onion Toffee', 'medium', 'cinnamon')
    10.99
    >>> calculate_subtotal('Purple Surprise', 'galactic', 'no topping')
    100.99
    '''
    #match the smoothie type with our four type smoothies
    if(smoothie_type == SMOOTHIE1_NAME):
        smoothie = SMOOTHIE1_COST
    elif(smoothie_type == SMOOTHIE2_NAME):
        smoothie = SMOOTHIE2_COST
    elif(smoothie_type == SMOOTHIE3_NAME):
        smoothie = SMOOTHIE3_COST
    elif(smoothie_type == SMOOTHIE4_NAME):
        smoothie = SMOOTHIE4_COST
    
    #match the size with our four built-in size
    if(smoothie_size == SIZE1_NAME):
        size = SIZE1_COST
    elif(smoothie_size == SIZE2_NAME):
        size = SIZE2_COST
    elif(smoothie_size == SIZE3_NAME):
        size = SIZE3_COST
    elif(smoothie_size == SIZE4_NAME):
        size = SIZE4_COST
    
    #check if the user want to no topping
    if(topping == TOPPING1_NAME):
        top = TOPPING1_COST
    else:
        top = TOPPING2_COST
        
    subtotal = smoothie + size + top
    
    return subtotal

def print_receipt(subtotal, smoothie_type, smoothie_size, topping):
    '''
    takes four inputs and print out the receipt

    Parameters
    ----------
    subtotal : Float
        the total price without the tax
    smoothie_type : String
        type of the smoothie
    smoothie_size : String
        size fo the smoothie
    topping : String
        topping the user want to add

    Returns
    -------
    Float
    the final price with tax

    >>> print_receipt(6.99, 'Pineapple Banana', 'large', 'no topping')
    
    >>> print_receipt(10.99, 'Onion Toffee', 'medium', 'cinnamon')
    
    >>> print_receipt(100.99, 'Purple Surprise', 'galactic', 'no topping')
    
    '''
    #check if there is no topping
    if(topping == TOPPING1_NAME):
        print('You ordered a ' + smoothie_size + ' ' + smoothie_type + ' smoothie with ' + '[topping]')
    else:
        print('You ordered a ' + smoothie_size + ' ' + smoothie_type + ' smoothie with ' + topping)
    
    #calculate the tax
    gst = round(subtotal * 0.09975, 2)
    qst = round(subtotal * 0.05, 2)
    total = round(subtotal + gst + qst, 2)
    
    print('Smoothie cost: ', '$' + str(subtotal))
    print('GST: \t', '$' + str(gst))
    print('QST: \t', '$' + str(qst))
    print('Total: \t', '$' + str(total))
    
    return total
    
def order():
    '''
    welcome the user, and call other functions step by step

    Returns
    -------
    None.

    '''
    
    #display the welcome info
    print('Welcome to Smooth Smoothies Smoothie Ordering System')
    print('Have you tried our new Onion Toffee smoothie?')
    
    question1 = 'Which smoothie would you like?'
    smoothie = pose_question_with_costs(question1, SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, \
                                      SMOOTHIE2_COST, SMOOTHIE3_NAME, SMOOTHIE3_COST, \
                                          SMOOTHIE4_NAME, SMOOTHIE4_COST)
    if(smoothie == ''):
        print('Sorry, this is not a valid option')
        return None
    
    #inform the user we only offer the new product if they do not choose Onion Toffee smoothie
    if(smoothie != SMOOTHIE4_NAME):
       print('Unfortunately, we are out of ' + smoothie)
       print('You will be served Onion Toffee smoothie.')
       smoothie = SMOOTHIE4_NAME
    
    question2 = 'Which size would you like?'
    size = pose_question_with_costs(question2, SIZE1_NAME, SIZE1_COST, SIZE2_NAME, SIZE2_COST, \
                                    SIZE3_NAME, SIZE3_COST, SIZE4_NAME, SIZE4_COST)
    
    question3 = 'Which topping would you like?'
    topping = pose_question_with_costs(question3, TOPPING1_NAME, TOPPING1_COST, TOPPING2_NAME, \
                                       TOPPING2_COST, TOPPING3_NAME, TOPPING3_COST, TOPPING4_NAME, \
                                           TOPPING4_COST)
    
    subtotal = calculate_subtotal(smoothie, size, topping)
    print_receipt(subtotal, smoothie, size, topping)
    
    
        
    
    
    
if __name__ == '__main__':
    order()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    