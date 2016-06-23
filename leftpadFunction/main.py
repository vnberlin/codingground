# leftpad function
# In March 2016 a programmer got pissed off at guys at NPM (nodejs) and kik.com
# over a package naming issue that kik.com handled piss poorly and took matter
# to NPM directly, NPM sided with the big company bullying the open source guy.
# The programmer subsequently unpublished all his packages from NPM resulting
# tones of code that stopped functioning. You might think it was a large piece
# of code that achieved this, nope just 10 line of nodejs that did leftpadding
# Here is a Python version of a simple left padding function lines.

#http://www.sciencealert.com/how-a-programmer-almost-broke-the-internet-by-deleting-11-lines-of-code

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
