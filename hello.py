#!/usr/bin/env python3.8
char_1 = 'A'
char_2 = 'Z'

print( ''.join((list(map(chr, range(ord(char_1), ord(char_2)+1))))))