"""
Main module - in this file Lottery is an instance of MatchingMachine
You can change arguments for MatchingMachine:
set_len: quantity of numbers drawn during lottery
began_range, end_range: range of lottery numbers - in Lotto is 1 to 49
---end range shloud be your rang +1. For instance for 49 should be putted 50---
lottery_price: virtual price of one draw
lotter_in_week: how many draws are in one week
"""

from lotek import MatchingMachine

if __name__ == '__main__':
    Lottery = MatchingMachine(set_len = 6,
                             began_range = 1,
                             end_range = 50,
                             lottery_price = 3,
                             lottery_in_week = 3
                            )
    _input_values = []
    for number in range(Lottery.set_len):
        _input_values.append(int(input('Pick your number: ')))

    Lottery.matching(_input_values)
    print(Lottery)
