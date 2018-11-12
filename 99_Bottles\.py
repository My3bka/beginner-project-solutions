#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:05:03 2018

@author: loyso
"""
# https://github.com/jorgegonzalez/beginner-projects#99-bottles
'''
    Create a program that prints out every line 
to the song "99 bottles of beer on the wall."

    Do not use a list for all of the numbers, 
and do not manually type them all in. 
Use a built in function instead.

    Besides the phrase "take one down," 
you may not type in any numbers/names
of numbers directly into your song lyrics.

    Remember, when you reach 1 bottle left,
the word "bottles" becomes singular.
'''
# make some vars for clearly making list
t0 = ' bottles of beer on the wall, '
t1 = ' bottles of beer.\nTake one down and pass it around, '
t2 = ' bottles of beer on the wall.\n\n'
end = '''No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.'''
#make list with for loop
l = [str(x) + t0 + str(x) + t1 + str(x-1) + t2 for x in range(99, 0, -1)]
t = ''.join(l).replace('1 bottles', '1 bottle').replace('0', 'no more') + end
print(t)