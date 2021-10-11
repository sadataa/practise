def even(num):
  
  return (num%2==0)

print((even(5)))  
   


def check_even_list(num):
    evennumber =[]
    for number in num:
        if (number%2==0):
            evennumber.append(number)
           
        else:

            pass
      
    return  evennumber  
    
print(check_even_list([1,2,3,4,5]))
def even (a,b):
    if ((a%2==0) and (b%2==0)) :

      
      return min(a,b)

 
    else:
      return max(a,b)  
        
         

print((even(10,20)))
