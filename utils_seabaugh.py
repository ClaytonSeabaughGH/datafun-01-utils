
'''  ITERATION 2

Module: Stellar Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this second iteration, add a function that returns the byline as a string.

I'll create a function named get_byline().
It'll return my byline to whatever calls the get_byline() function. 
   
I'll update the main() function to use the new get_byline() function. 

Same conditional boilerplate at the end. 

I'll test this version before adding more code that shows:
- my ability to declare variables of different types
- my ability to use Python to calculate basic descriptive statistics. '''


#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Intersteller Analytics: Delivering Professional Insights'



#####################################
# Define the get_byline() Function
#####################################

def get_byline()-> str:
    '''Return byline for my analytics projects'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
