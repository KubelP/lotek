import pytest
from lotek import MatchingMachine, LengthError, OutOfRange


def test_len():

    """
    Testing if length of list/tuple of picked numbers
    is equal to length of list/tuple of drawn numbers.
    """

    with pytest.raises(LengthError) as message:
        tested_list = [1, 2, 3, 4, 5, 6] #to short list of picked numbers
        test = MatchingMachine(5, 1, 50, 3, 3)
        test.len_check(tested_list)
        assert message == LengthError


def test_duplicate():

    """
    Testing if there is no duplicates in picked numbers.
    """

    with pytest.raises(LengthError) as message:
        tested_list = [1, 2, 2, 4, 5, 6] #list of picked numbers with duplicates
        test = MatchingMachine(6, 1, 50, 3, 3)
        test.duplicate_check(tested_list)
        assert message == LengthError


def test_out_of_range():

    """
    Testing if picked numbers are in range of drwan numbers.
    """

    with pytest.raises(OutOfRange) as message:
        test = MatchingMachine(3, 1, 11, 1, 3)
        tested_list = [1, 2, 11]
        test.out_of_range_check(tested_list)
        assert message == OutOfRange


def test_matching():

    """
    Testing if MatchingMachin find match and break loop.
    """

    test = MatchingMachine(3, 1, 11, 1, 3)
    tested_list = [1, 2, 10]
    assert test.matching(tested_list) != 0 #if returned value of COUNTER is
                                           #greater then 0 that means the loop
                                           #is breaking with finite non-zero value - matching works
