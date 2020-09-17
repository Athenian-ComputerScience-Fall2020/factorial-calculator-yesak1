# Collaborators:  I asked my uncle for some tips as he has some python experience.
def factorialcalc(num):   #you may choose the name of the parameter
    if num==1:
        return num
    else:
        return num * factorialcalc(num-1)
        

num=int(input("enter number"))

if num < 0:
    print ("negative values cannot be factorialized")
elif num == 0:
    print ("factorial of 0 is 1")
else:
    print ("factorial of", num, "is", factorialcalc(num))



    

  
  # be sure to return the factorial
if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
   
    print(factorialcalc(int(num)))
    

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    
