
def stack_based_reverse(some_str):
    work = []
    for c in some_str:
        work.insert(0, c)

    return ''.join(work)


if __name__ == '__main__':
    to_reverse = 'reverse'
    print('String to reverse: {}'.format(to_reverse))
    print(stack_based_reverse(to_reverse))

