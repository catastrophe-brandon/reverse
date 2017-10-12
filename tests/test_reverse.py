from reverse import stack_based_reverse

def test_stack_based_reverse():
    assert 'otatop' == stack_based_reverse('potato')
    assert '' == stack_based_reverse('')
    assert '!otatop ' == stack_based_reverse(' potato!')

