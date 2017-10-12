

if __name__ == '__main__'
    to_reverse = 'reverse'
    work = []
    for c in to_reverse:
       work.push(c)
    
    result = []
    while len(work) > 0:
        result.add(work.pop())
        
    print(str(result))
    
