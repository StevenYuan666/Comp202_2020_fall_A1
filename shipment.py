#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:59:20 2020

@author: stevenyuan
"""

def calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9):
    '''
    This function takes in a 10-digit ISBN as 9 one-digit integers, 
    and calculates and returns the checksum as a string.

    Parameters
    ----------
    d1 : Int
        one-digit of ISBN
    d2 : Int
        one-digit of ISBN
    d3 : Int
        one-digit of ISBN
    d4 : Int
        one-digit of ISBN
    d5 : Int
        one-digit of ISBN
    d6 : Int
        one-digit of ISBN
    d7 : Int
        one-digit of ISBN
    d8 : Int
        one-digit of ISBN
    d9 : Int
        one-digit of ISBN

    Returns
    -------
    String
    the checksum as a string to return

    >>> calculate_isbn_checksum_by_digits(8, 7, 1, 1, 0, 7, 5, 5, 9)
    7
    >>> calculate_isbn_checksum_by_digits(6, 7, 7, 3, 4, 7, 5, 9, 9)
    6
    >>> calculate_isbn_checksum_by_digits(1, 2, 3, 4, 5, 6, 7, 8, 9)
    X
    '''
    
    #calculate the sum frist
    sum_digits = d1 + 2 * d2 + 3 * d3 + 4 * d4 + 5 * d5 + 6 * d6 + 7 * d7 + 8 * d8 + 9 * d9
    remainder = sum_digits % 11
    
    #check if the remainder is 10
    if(remainder == 10):
        return 'X'
    else:
        return str(remainder)
    
def calculate_isbn_checksum(isbn):
    '''
    This function takes as input a 9-digit integer representing the 9 left-most digits of an ISBN, 
    and calculates and returns the checksum as a string.

    Parameters
    ----------
    isbn : Int
        the left-most 9 digits of ISBN

    Returns
    -------
    String
    return the checknum as a string

    >>> calculate_isbn_checksum(871107559)
    7
    >>> calculate_isbn_checksum(677347599)
    6
    >>> calculate_isbn_checksum(123456789)
    X
    '''
    
    #split the input type to digits
    d1 = isbn // 100000000
    d2 = (isbn - d1 * 100000000) // 10000000
    d3 = (isbn - d1 * 100000000 - d2 * 10000000) // 1000000
    d4 = (isbn - d1 * 100000000 - d2 * 10000000 - d3 * 1000000) // 100000
    d5 = (isbn - d1 * 100000000 - d2 * 10000000 - d3 * 1000000 - d4 * 100000) // 10000
    d6 = (isbn - d1 * 100000000 - d2 * 10000000 - d3 * 1000000 - d4 * 100000 - d5 * 10000) // 1000
    d7 = (isbn - d1 * 100000000 - d2 * 10000000 - d3 * 1000000 - d4 * 100000 - d5 * 10000 \
          - d6 * 1000) // 100
    d8 = (isbn - d1 * 100000000 - d2 * 10000000 - d3 * 1000000 - d4 * 100000 - d5 * 10000 \
          - d6 * 1000 - d7 * 100) // 10
    d9 = (isbn - d1 * 100000000 - d2 * 10000000 - d3 * 1000000 - d4 * 100000 - d5 * 10000 \
          - d6 * 1000 - d7 * 100 - d8 * 10) // 1
    
    #change the type from float to int
    d1 = int(d1)
    d2 = int(d2)
    d3 = int(d3)
    d4 = int(d4)
    d5 = int(d5)
    d6 = int(d6)
    d7 = int(d7)
    d8 = int(d8)
    d9 = int(d9)
    
    checksum = calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9)
    return checksum
    
def is_isbn(isbn, checksum):
    '''
    This function takes two arguments: a 9-digit integer representing 
    the 9 left-most digits of an ISBN, and a checksum (string), 
    and returns True if the ISBN is valid (i.e., if the given checksum matches 
    the calculated checksum) and False otherwise.

    Parameters
    ----------
    isbn : Int
        a 9-digits integer
    checksum : String
        the provided checknum

    Returns
    -------
    boolean
    check if the ISBN is valid

    >>> is_isbn(871107559, "4")
    False
    >>> is_isbn(677347599, "0")
    False
    >>> is_isbn(123456789, "X")
    True
    '''
    
    #calculated the checknum first
    calculated_checksum = calculate_isbn_checksum(isbn)
    
    #check if the calculated_checknum is same as the provided one
    return calculated_checksum == checksum

def book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
    '''
    Returns True if the book of the given integer dimensions can fit in the box of 
    the given integer dimensions, and False otherwise.

    Parameters
    ----------
    box_w : Int
        width of box
    box_d : Int
        depth of box
    box_h : Int
        height of box
    book_w : Int
        width of book
    book_d : Int
        depth of book
    book_h : Int
        heigh of book

    Returns
    -------
    boolean
    return true the book can be put in the box

    >>> book_fits_in_box(15, 2, 2, 2, 15, 2)
    True
    >>> book_fits_in_box(10, 10, 10, 2, 15, 2)
    False
    >>> book_fits_in_box(10, 10, 10, 10, 10, 10)
    True
    '''
    
    #lists the input from max to min
    if(box_w >= box_d and box_w >= box_h):
        max_box = box_w
        if(box_d >= box_h):
            medium_box = box_d
            min_box = box_h
        else:
            medium_box = box_h
            min_box = box_d
    elif(box_d >= box_w and box_d >= box_h):
        max_box = box_d
        if(box_w >= box_h):
            medium_box = box_w
            min_box = box_h
        else:
            medium_box = box_h
            min_box = box_w
    else:
        max_box = box_h
        if(box_d >= box_w):
            medium_box = box_d
            min_box = box_w
        else:
            medium_box = box_w
            min_box = box_d
    
    if(book_w >= book_d and book_w >= book_h):
        max_book = book_w
        if(book_d >= book_h):
            medium_book = book_d
            min_book = book_h
        else:
            medium_book = book_h
            min_book = book_d
    elif(book_d >= book_w and book_d >= book_h):
        max_book = book_d
        if(book_w >= book_h):
            medium_book = book_w
            min_book = book_h
        else:
            medium_book = book_h
            min_book = book_w
    else:
        max_book = book_h
        if(book_d >= book_w):
            medium_book = book_d
            min_book = book_w
        else:
            medium_book = book_w
            min_book = book_d
    
    return max_box >= max_book and medium_box >= medium_book and min_box >= min_book
    
def get_smallest_box_for_book(book_w, book_d, book_h):
    '''
    Returns a string corresponding to the small- est box size (‘small’, ‘medium’ or ‘large’) 
    in which the book of given integer dimensions can fit.
    Return empty string if there is no fit in box

    Parameters
    ----------
    book_w : Int
        width of book
    book_d : Int
        depth of book
    book_h : Int
        height of book

    Returns
    -------
    String
    the size of the most fit in box
    
    >>> get_smallest_box_for_book(12, 12, 2)
    medium
    >>> get_smallest_box_for_book(18, 10, 3)
    large
    >>> get_smallest_box_for_book(10, 10, 5)
    
    '''
    #check if the book can fit in the box from small size to big size
    if(book_fits_in_box(10, 10, 2, book_w, book_d, book_h)):
        return 'small'
    elif(book_fits_in_box(15, 15, 3, book_w, book_d, book_h)):
        return 'medium'
    elif(book_fits_in_box(20, 20, 4, book_w, book_d, book_h)):
        return 'large'
    else:
        return ''
    
def get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h):
    '''
    Returns (as an integer) the maximum number of copies of a book of given 
    integer dimensions that can fit into a box of given integer dimensions.

    Parameters
    ----------
    box_w : Int
        width of box
    box_d : Int
        depth of box
    box_h : Int
        height of box
    book_w : Int
        width of book
    book_d : Int
        depth of book
    book_h : Int
        heigh of book

    Returns
    -------
    Int
    the maximum number of copies of a book can be put in the box

    >>> get_num_books_for_box(10, 5, 5, 5, 5, 2)
    4
    >>> get_num_books_for_box(12, 3, 5, 5, 2, 2)
    4
    >>> get_num_books_for_box(3, 5, 10, 5, 5, 2)
    0
    '''
    #check if the book can be put in the box
    if(box_w >= book_w and box_h >= book_h and box_d >= box_d):
        times_of_w = box_w // book_w
        times_of_h = box_h // book_h
        times_of_d = box_d // book_d
        return times_of_w * times_of_h * times_of_d
    else:
        return 0

def main():
    '''
    The main program for the shipment

    Returns
    -------
    None.
    
    >>> main()
    Welcome to the shipment calculation system. 
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box Enter choice (1-4): 1
    Enter ISBN: 100101011
    Enter checksum: 1
    ISBN is not valid (checksum did not match)
    '''
    #display the welcome info
    print('Welcome to the shipment calculation system.')
    print('1) Check ISBN')
    print('2) Check box/book size')
    print('3) Get smallest box size for book')
    print('4) Get num equally-sized books per box')
    
    #ask the user's choice
    choice = input('Enter choice (1-4): ')
    
    if(choice == '1'):
        isbn = int(input('Enter ISBN: '))
        checksum = int(input('Enter checksum: '))
        if(is_isbn(isbn, checksum)):
            print('ISBN is valid, checksum matched.')
        else:
            print('ISBN is not valid (checksum did not match).')
    elif(choice == '2'):
        box_w = int(input('Enter the box width: '))
        box_d = int(input('Enter the box depth: '))
        box_h = int(input('Enter the box height: '))
        book_w = int(input('Enter the book width: '))
        book_d = int(input('Enter the book depth: '))
        book_h = int(input('Enter the book height: '))
        if(book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h)):
            print('Your book can be put in this box')
        else:
            print('Your book cannot be put in this box')
    elif(choice == '3'):
        book_w = int(input('Enter the book width: '))
        book_d = int(input('Enter the book depth: '))
        book_h = int(input('Enter the book height: '))
        size = get_smallest_box_for_book(book_w, book_d, book_h)
        if(size == ''):
            print('We cannot find a regular fit box for your book')
        else:
            print('The smallest box size for your book is ', size)
    elif(choice == '4'):
        box_w = int(input('Enter the box width: '))
        box_d = int(input('Enter the box depth: '))
        box_h = int(input('Enter the box height: '))
        book_w = int(input('Enter the book width: '))
        book_d = int(input('Enter the book depth: '))
        book_h = int(input('Enter the book height: '))
        num = get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h)
        if(num == 0):
            print('Your book cannot be put in this box')
        else:
            print('You can put', num, 'books in this box')
        
        
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
