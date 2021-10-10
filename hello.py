import random

from __future__ import division
 
def sadat(x):
    low =1 
    high =x
    feedback=''
    while(feedback!='c'):
        if low!=high:

           guess=random.randint(low ,high)
        else:
            guess=low

        feedback=input(f'is  {guess} t oo high (H)to low (L)or correct(C)').lower()
        if (feedback=='h'):
            high=guess-1
        elif(feedback=="l"):
            low=guess=guess+1
    
    print(f'we got you {guess}')


def fahim():
 
 
 print(5/2)
 print(5//2)

  
fahim()
