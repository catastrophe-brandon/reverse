

if __name__ == '__main__':
    to_reverse = 'reverse'
    work = []
    for c in to_reverse:
       work.insert(0, c)

    result = []
    while len(work) > 0:
        result.insert(0, work.pop())

    print(str(result))

