# Medical_Insurance_Cost_Analysis-UPDATED

# Overview:
This project is a beginner Python program created as part of Codecademy's Data and Programming Foundations for AI course. The goal is to use a simple medical insurance cost formula to calculate estimated yearly insurance costs based on different factors.

The project uses a reusable Python function to calculate the estimated insurance cost for different people.

# The Factors Used
The calculation uses:

- Age
- Sex
- BMI
- Number of children
- Smoking status
- What the Project Does

The program defines a calculate_insurance_cost() function that takes a person's details as inputs and calculates their estimated insurance cost.

The function then prints the estimated cost for that person and returns the calculated value.

The program is used to calculate insurance costs for:

- Maria
- Omar
- Joan

For example:
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)

The same function can then be reused with different values:
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

joan_insurance_cost = calculate_insurance_cost("Joan", 18, 1, 24.9, 0, 0)

# Skills Practised
This project helped me practise the following Python concepts:

- Defining functions
- Function parameters
- Calling functions
- Returning values with return
- Variables
- Arithmetic operations
- String conversion with str()
- Printing formatted output
- Comments and code organisation
- Reusing code with functions


# Insurance Cost Formula
The function uses a formula similar to:
estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

The calculated value is then returned:
return(estimated_cost)

# Technologies:
Python 3

# Learning Context:
This is one of my first Python projects while developing my programming and data analysis skills through Codecademy's Data and Programming Foundations for AI course.

This version builds on my earlier work by introducing functions, allowing the same calculation to be reused for different people rather than repeating the same code.
