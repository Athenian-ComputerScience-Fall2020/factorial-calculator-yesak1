# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  asked my uncle for some tips as he has some python experience.
number=input("enter number")
def factorialcalc(x):   #you may choose the name of the parameter
if number < 0:
    print("negative values cannot be factorialized")
elif number==0 :
    print("the factorial of 0 is 1")
else:
    for x in range (1, number+1):
        factorial=factorial*x
    print(f"the factorial of {number} is {factorial}")
    return number
  # be sure to return the factorial
if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    print (factorialcalc)

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    #print(factorial_calc(int(num)))
