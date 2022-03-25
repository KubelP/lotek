from lotek import rand_int

def test_rand_int_len():
    rand_numbers = rand_int()
    assert len(rand_numbers) == 6