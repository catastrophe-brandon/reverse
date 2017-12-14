
def linear_reverse(some_str):
    """ Walk backwards through the input string. """
    i = len(some_str) - 1
    result = []

    while (i >= 0):
        result.append(some_str[i])
        i = i - 1

    return ''.join(result)

def barf_reverse(some_str):
    """ REALLY ugly but appeals to the Java and C# folks that think Python is too simple. """
    for c in reversed(some_str.split()):
        print(c)
    return ''.join([somechar for somechar in reversed(some_str.split())])

def stack_based_reverse(some_str):
    """ Use a list like a stack, push all the chars in and pop them off """
    work = []
    for c in some_str:
        work.insert(0, c)

    return ''.join(work)

def pythonic_reverse(some_str):
    return some_str[::-1]


if __name__ == '__main__':
    to_reverse = 'reverse'
    print('String to reverse: {}'.format(to_reverse))
    print(stack_based_reverse(to_reverse))

    print('Pythonic reverse: {}'.format(pythonic_reverse(to_reverse)))
    print('Barf reverse: {}'.format(barf_reverse(to_reverse)))
    print('Linear reverse: {}'.format(linear_reverse(to_reverse)))
