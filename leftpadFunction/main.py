# leftpad function
def leftpad(str_, pad, ch):
    a = list(str_)
    length = len(a)
    r = []
    pad = pad - length
    for i in range(pad):
        r.append(ch)
    r = r+a
    return ''.join(r)
    
def test():
    res1 = leftpad("", 10, 'o')
    res2 = leftpad("hello", 10, 'o')
    res3 = leftpad("kitten", 10, 'o')
    res4 = leftpad("hellokitty", 10, 'o')
    print res1
    print res2
    print res3
    print res4
    
def main():
    test()
if __name__ == '__main__':
    main()