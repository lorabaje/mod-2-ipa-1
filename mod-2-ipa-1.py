'''Module 2: Individual Programming Assignment 1
Useful Business Calculations
This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    5 points.
    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee
    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos
    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    net_tax = round(gross_pay - (gross_pay * tax_rate)) # what is left after tax; gross pay - tax
    net_savings = net_tax - expenses
    
    return net_savings
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    
savings(10_000, 0.05, 15_000)
-5500
def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    5 points.
    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.
    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.
    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.
    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job
    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code.
    
    total_material_cons = num_jobs * job_consumption # total material consumed
    material_waste = total_material - total_material_cons # material waste
    z = str(material_units) # declare material units as string
    material_waste_final = str(material_waste) + z # convert material_waste into string then combine with 'z'
    
    return material_waste_final
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
material_waste(100, "kg", 50, 1.5)
'25.0kg'
def interest(principal, rate, periods):
    '''Interest.
    5 points.
    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.
    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.
    Round down the final amount.
    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested
    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    
    interest = principal * (rate * periods) # interest
    final_amount = round(principal + interest) # final amount
    
    return final_amount

    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
interest(100_000, 0.01, 25)
125000
def body_mass_index(weight, height):
    '''Body Mass Index.
    5 points.
    This function calculates the body mass index (BMI) of a person
        given their weight and height.
    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)
    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].
    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    
    weight_kg = 0.453592 * weight # Weight input is lb
    
    height[0] = 0.3048 * height[0] # foot to meter
    height[1] = 0.0254 * height[1] # inches to meter 
    

    height_sum = sum(height) # sum elements in heights after converting; height in meters
    
    body_mass_index = weight_kg / (height_sum ** 2) # BMI formula
    
    print(weight)
    print(weight_kg)
    print(height[0])
    print(height[1])
    print(height_sum)
    
    return body_mass_index
    
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
body_mass_index(170, [5, 3])
170
77.11064
1.524
0.07619999999999999
1.6002
30.113814825765203
 