# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 01:51:56 2025

@author: Crimson
"""
annual_salary = float(input("What's your annual salary "))
portion_saved = float(input("What %(in decimal) of your salary do you want to save "))
total_cost = float(input("What's the cost of your dream home "))
semi_annual_raise = float(input("What is the %(in decimal) raise do you get semi-annually "))
monthly_salary = annual_salary/12
portion_down_payment = total_cost * .25
current_savings = 0.0
r = .04
monthly_r = r/12
total_months = 0
month_counter = 0

while portion_down_payment >= current_savings:
    return_value = current_savings * monthly_r
    current_savings = monthly_salary * portion_saved + return_value + current_savings
    if month_counter == 6:
        annual_salary = annual_salary + annual_salary * semi_annual_raise
        monthly_salary = annual_salary/12
        month_counter = 0
    total_months += 1
    month_counter += 1
    
    
print("It'll take", total_months, "months to save")