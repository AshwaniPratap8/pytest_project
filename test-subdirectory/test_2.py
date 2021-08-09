
def capital_case(x):
    return x.capitalize()

def test_new():
    assert capital_case('semaphore') == 'Semaphore'
	
def test_new2():
    assert capital_case('phore') == 'Phore'