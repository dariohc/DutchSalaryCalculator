__author__ = 'Dario Hermida'
import main as calculate
import numpy as np
import matplotlib as plot

def testing_main(min_salary, max_salary, step):
    regular_salary = []
    ruling_salary = []
    salary = list(range(min_salary, max_salary, step))
    for input_bruto in salary:
        regular_salary.append(calculate.regular_salary(input_bruto))
        ruling_salary.append(calculate.thirty_percent_rulling(input_bruto))
        #  print('this should be your salary', calculate.regular_salary(input_bruto))
        #  print('this should be your Ruling salary', calculate.thirty_percent_rulling(input_bruto))
    return regular_salary, ruling_salary
