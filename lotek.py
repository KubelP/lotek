'''
This module contain of exceptions: LengthError and OutOfRange
and classes:
- RandomNumDrawMachin - creator lists of random numbers
- MyNumbers - picked numbers by user
- MatchingMachine - compares picked numbers by user as MyNumbers object
  with generated numbers as result of RandomNumDrawMachin  
'''

import random
from time_decorator import time_measure


class LengthError(Exception):

    """
    Exeption for length of list validator
    """
    pass


class OutOfRange(Exception):

    """
    Exception for picked numbers validator
    """
    pass


class RandomNumDrawMachin:

    '''
    Returns set of random numers'
    Takes intiger for set leangth,
    start of range and end of range.
    '''

    def numbers_generator(self, set_len: int, began_range: int, end_range: int) -> set:
        random_numbers = set() # set eliminates issue with duplicates 

        while len(random_numbers) < set_len:
            i = random.randint(began_range, end_range)
            random_numbers.add(i)
        return random_numbers

class MyNumbers:

    """
    Initiating picked by user numbers.
    """

    def __init__(self, my_numbers: list or tuple) -> None:

        if isinstance(my_numbers[0], (list, tuple)): #for case when numbers list
                                                     # is provided as *args
            self.my_numbers = tuple(my_numbers[0])
        else:
            self.my_numbers = my_numbers


    def __len__(self) -> int:
        return len(self.my_numbers)


    def __str__(self) -> str:
        return f'{self.my_numbers}'


class MatchingMachine:

    """
    This class is main mechanic of project.
    Takes arguments:
    set_len: is quantity of numbers drawn during lottery
    began_range, end_range: range of lottery numbers - in Lotto is 1 to 49
    lottery_price: virtual price of one draw
    lotter_in_week: how many draws are in one week
    """

    def __init__(self, set_len, began_range,
                 end_range,  lottery_price, lottery_in_week) -> None:

        self.set_len = abs(set_len)
        self.began_range = abs(began_range)
        self.end_range = abs(end_range)
        self.drawn_numbers = RandomNumDrawMachin()
        self.lottery_price = lottery_price
        self.lottery_in_week = lottery_in_week
        self.counter = 0 # draws counter


    def len_check(self, my_numbers):

        if self.set_len != len(my_numbers):

            """
            Validator for checking if length of list of drawn numbers
            is equal to length of list of numbers picked by user.
            """

            raise LengthError(f'You choose {len(my_numbers)} numbers, '
                  f'but you participate in {self.set_len} numbers drawing.')


    def duplicate_check(self, my_numbers):

        """
        Validator for checking if there is no duplicates
        in list of numbers picked by user.
        """

        if len(set(my_numbers)) != len(my_numbers):
            raise LengthError('You have duplicates in your picked numbers, '
                  'given number can only be picked once.')


    def out_of_range_check(self, my_numbers):

        """
        Validator for checking if numbers picked by user
        are in range of numbers used in lottery.
        """

        for number in my_numbers:
            if number >= self.end_range or number <= 0:
                raise OutOfRange(f'You picked {number} which is out of range. '
                      f'You have to picked numbers in range {self.began_range}'
                      f' to {self.end_range-1}')


    def set_of_numbers(self, input_numbers):

        """
        Function takes as argument numbers picked (list or tuple)
        by user, validate and return set.
        """

        my_numbers = MyNumbers(input_numbers)
        numbers = my_numbers.my_numbers
        my_numbers_to_set = set(numbers)
        self.len_check(my_numbers)
        self.duplicate_check(numbers)
        self.out_of_range_check(numbers)
        return my_numbers_to_set

    @time_measure
    def matching(self, *input_numbers: int or tuple or list):

        """
        Function takes as argument numbers picked
        by user. It can be int, list or tuple.
        Returns in wich drawn user won lottery.
        Returns COUNTER: int.
        """

        my_numbers_to_set = self.set_of_numbers(input_numbers)
        print(f'My picked numbers are: {my_numbers_to_set}')
        print('Waiting for win...')

        drawn_numbers = self.drawn_numbers.numbers_generator(self.set_len,
                                                            self.began_range,
                                                            self.end_range)
        while my_numbers_to_set !=  drawn_numbers:
            self.drawn_numbers = RandomNumDrawMachin()  # clear generated set
            drawn_numbers = self.drawn_numbers.numbers_generator(self.set_len,
                                                                 self.began_range,
                                                                 self.end_range) # new draw

            self.counter +=1
        return self.counter

    def __str__(self):
        message = (f'You win on {self.counter} draw '
                  f'which cost you {self.lottery_price*self.counter}, '
                  f'and would take {int((self.counter/self.lottery_in_week)*54)} years')
        return message
      