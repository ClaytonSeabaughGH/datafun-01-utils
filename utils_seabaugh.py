'''  ITERATION 4

Module: Stellar Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this fourth iteration, I introduce some basic statistics using Python.
    - min() is a built in function to find the smallest value passed in
    - max() is a built in function to find the largest value passed in
    - The statistics module offers methods to calculate mean and standard deviation.
'''

#####################################
# Import Modules at the Top
#####################################

# In Python, we can import modules to add extra tools and functions.
# Below, we're importing:
# - `statistics`: This gives us tools to calculate things like averages.
# Use CTRL F and type statistics to see where it is used in the code. 
# Did you find statistics.mean()?
# Did you find statistics.stdev()?

import statistics

#####################################
# Declare global variables
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Boolean variable to indicate if the company is looking for new clients
accepting_new_clients: bool = True

# Integer variable for the number of employees in the company
number_of_employees: int = 4

# List of strings reprseting different locations of clients
locations_of_clients: list = ["United States", "United Kingdom","France","Germany" ]

# List of floats representing amount of clinets per location
clients_per_location: list = [51, 32, 24, 13]

#####################################
# Calculate Basic Statistics 
#   Do this BEFORE we declare the byline 
#   So the values have been calculated 
#   and are ready for use in the byline.
#####################################

# Calculate basic stats using built-in functions min(), max() and statistics module functions mean() and stdev().
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

cpl_min_score: float = min(clients_per_location)  
cpl_max_score: float = max(clients_per_location)  
cpl_mean_score: float = statistics.mean(clients_per_location)  
cpl_stdev_score: float = statistics.stdev(clients_per_location)

#####################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------------
Interstellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Accepting New Clients:      {accepting_new_clients}
Number of Employees:        {number_of_employees}
Locations of Clients:       {locations_of_clients}
Clients per Location:       {clients_per_location}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
