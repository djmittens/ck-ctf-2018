#! /usr/bin/env python
def decrement_char(ch):
    if not ch.isalpha():
        return ch
    else:
        return chr(abs(ord(ch) - 13))

with open("flag.txt") as f :
    # for k in range(100):
    content = map(decrement_char, f.read())
    print(''.join(content))