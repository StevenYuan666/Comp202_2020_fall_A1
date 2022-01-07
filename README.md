# VendingMachine-BookShipment-Cards
## Vending Machine - Smoothie Ordering
With the rise in remote learning, many classrooms in campuses across the country are currently vacant. To capitalize on this situation, a nearby school called MacGill University is converting some classrooms into temporary food delivery service facilities. One such company called Smooth Smoothies Ltd (SSL) has moved into the computer science building of said university. Smoothies are prepared in the building, and delivered to clients who order through an online system.

Contracted by Smooth Smoothies Ltd to develop an ordering system for their smoothies using Python. Users will enter their order (smoothie type, size and topping) through the Python shell, and receive the total amount payable with appropriate tax amounts listed.

Ordering will proceed as follows:

1. The customer will be welcomed to Smooth Smoothies smoothie system for ordering smoothies.

2. The customer will be asked which smoothie they would like. There will be four options from which to choose. Each option will include the name and base price of the smoothie.

3. The customer will be asked which size of smoothie they would like. There will be four options from which to choose. Each option will include the size and any additional cost (the default size will be medium and will have no additional cost).

4. The customer will be asked which topping they would like. There will be four options from which to choose. The user will only be able to choose one topping, and all toppings will be $1. The user may decide to select ‘no topping’ (which will be one of the four options).

5. The customer will be provided a receipt showing the subtotal, GST, QST, and total amount payable.


## Shipping Books
Before books are placed into a box for shipment, their ISBNs are scanned for record purposes. ISBN stands for International Standard Book Number and consists of a series of digits that uniquely identifies a book. Today, books have 13-digit ISBN numbers, but we will consider the older 10-digit numbers for simplicity. The important thing to know about an ISBN number is that its right-most (10th) digit is known as a ‘checksum.’ This checksum can be calculated by performing a computation on the other 9 digits. Each time an ISBN is scanned, this calculation is performed, and the result of the calculation is checked against the actual 10th digit. (If they do not match, then it is assumed that the ISBN is damaged in some way.)

The checksum for a 10-digit ISBN number is calculated as follows: (x1 +2∗x2 +3∗x3 +...+9∗x9)%11

where each xi is digit i of the ISBN (from left to right – x1 is the left-most digit). The result of this calculation is the checksum, unless equal to 10, in which the checksum is instead a capital ‘X’.

## Cards
A deck of playing cards consists of 52 cards, each being a combination of a suit and rank. There are four possible suits (hearts, diamonds, clubs and spades) and thirteen possible ranks (the numbers from two to ten, and Jack, Queen, King and Ace). We will write a handful of Python functions that deal with playing cards represented as integers from 1 to 52.

Each integer from 1 to 52 will represent a different card of the deck in the following manner. We can take the numbers 1, 2, 3 and 4 to be Two’s of each suit; the numbers 5, 6, 7, 8 as Three’s of each suit, and so on, culminating in the numbers 49, 50, 51, 52 as Ace’s of each suit. We will give the suits the order of Hearts, Diamonds, Clubs, and Spades; that is, the numbers 1, 2, 3, 4 will correspond to the Two of Hearts, Two of Diamonds, Two of Clubs and Two of Spades, respectively.

Thus, given any integer representation of a card (from 1 to 52), we can retrieve its rank and suit. For example, given the card 49, we can determine that it is suit 1 (Hearts) and rank 12 (Ace). There will be a number given to each suit (between 0 and 3) and rank (between 0 and 12).
