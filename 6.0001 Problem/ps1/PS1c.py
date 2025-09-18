# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 01:51:56 2025

@author: Crimson
"""
#Starting Variables
annual_salary = float(input("Enter Starting Salary: "))
beg_annual_salary = annual_salary
monthly_salary = annual_salary/12
total_cost = 1000000.00
portion_down_payment = total_cost * .25
semi_annual_raise = .07
r = .04
current_savings = 0.0
month_counter = 0

for month in range(1,37):
    if month_counter >= 6:
        annual_salary = annual_salary * semi_annual_raise + annual_salary
        monthly_salary = annual_salary/12
        month_counter = 0
        
    current_savings = current_savings + monthly_salary * 1 + current_savings * r/12
        
    month_counter += 1
    
if current_savings < portion_down_payment:
    print("You cannot save enough in 3 years!")
    
else:
    l = 0 # % saved min
    h = 10000 # % saved max
    bi_steps = 0
    
    while True:
        guess = (l+h)/2
        current_savings = 0
        annual_salary = beg_annual_salary
        monthly_salary = annual_salary/12
        month_counter = 0
        bi_steps += 1
        
        for month in range(1,37):
            #monthly_salary * guess/10000 is amount saved per month
            
            if month_counter >= 6:
                    annual_salary = annual_salary * semi_annual_raise + annual_salary
                    monthly_salary = annual_salary/12
                    month_counter = 0
                    
            current_savings = current_savings + monthly_salary * guess/10000 + current_savings * r/12
            
            month_counter += 1
            fg = current_savings 
            
        if fg - portion_down_payment > 100:
            h = guess
                
        elif fg < portion_down_payment:
            l = guess
            
        else:
            print("Best saving rate:", guess)
            print("Steps in bisection search:", bi_steps)
            break



