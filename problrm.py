def number(num):
    for  i in range (0, len(num)-1) :
        if num [i] ==33 and num[i+1]==33 :
            return True


    return False     
print(number([4,3,3]))


def character (text):
    result=''
    for sadat in text:
        result+=sadat*3
      
      
    print(result)
character('hello')
def Blackjack(a,b,c):
    sum=a+b+c
    if (sum<=21):
        return sum


    elif 11 in [a,b,c] and sum >=31:

        return sum -10

     
    else:
        return 'bust'


print(Blackjack(9,9,9)) 