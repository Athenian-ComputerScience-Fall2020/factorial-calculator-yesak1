# Collaborators:  I asked my uncle for some tips as he has some python experience. He didn't entirely know how to do it either but he gave me some tips. So, I did some research and I used some info about recursion from https://beginnersbook.com/2018/02/python-program-to-find-factorial-of-number/ and Khan Academy.
def factorial_calc(num):   #you may choose the name of the parameter
    if num==1:
        return num
    elif num==0:
        return 1

    else:
        return num * factorial_calc(num-1)
   

        




    

  
  # be sure to return the factorial
if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    num=int(input("enter number"))

    if num < 0:
        print ("negative values cannot be factorialized")
    elif num == 0:
        print ("factorial of 0 is 1")
    else:
        print ("factorial of", num, "is", factorial_calc(num))

    print(factorial_calc(int(num)))
    

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    
