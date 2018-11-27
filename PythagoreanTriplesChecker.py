#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def inpt(kf):
    x = ''
    while True:
        x = input(kf)
        try:
            x = int(x)
            return x
        except:
            print('can\'t interpret answer, please enter again')
            
def check(kfs):
    if kfs[0]**2 + kfs[1]**2 - kfs[2]**2 == 0:
         return True
    if kfs[0]**2 + kfs[2]**2 - kfs[1]**2 == 0:
         return True
    if kfs[1]**2 + kfs[2]**2 - kfs[0]**2 == 0:
         return True
    return False

def diditagainn():
    please = 'Please enter coefficient '
    kfs = [inpt(please + str(_ + 1) + ': ') for _ in range(3)]
    print('Is it Pythagorean: ', check(kfs))
    
def again():
    x = ''
    while True:
        x = input('Did it again? > "y" for yes < : ')
        try:
            x = str(x)
            if x == 'y' or x == 'Y':
                return True
            else:
                return False
        except:
            print('can\'t interpret answer')
    return False
    
print('<Pythagorean Triples Checker>')

while True:
    diditagainn()
    if not again():
        print('quit')
        break
        
quit()
