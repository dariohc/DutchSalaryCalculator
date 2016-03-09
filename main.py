__author__ = 'Dario Hermida'
salaries = [33000, 50000, 72000, 76000]
# bruto_salary = 72000
neto_salary = 0
calculate = True


def regular_salary(bruto_salary):
    first_step, second_step, third_step = [0, 0, 0]
    first_step = 33000 * (1 - 0.33)
    if bruto_salary > 66000:
        second_step = (66000 - 33000) * (1 - 0.42)
        third_step = (bruto_salary - 66000) * (1 - 0.52)
    else:
        second_step = (bruto_salary - 33000) * (1 - 0.42)
    return (first_step + second_step + third_step)/12


def thirty_percent_rulling(bruto_salary):

    first_step, second_step, third_step = [0, 0, 0]
    without_tax = bruto_salary * 0.3
    bruto_salary *= 0.7
    if bruto_salary > 33000:
        first_step = 33000 * (1 - 0.33)
        if bruto_salary > 66000:
            second_step = (66000 - 33000) * (1 - 0.42)
            third_step = (bruto_salary - 66000) * (1 - 0.52)
        else:
            second_step = (bruto_salary - 33000) * (1 - 0.42)
    else:
        first_step = bruto_salary * (1 - 0.33)
        if bruto_salary > 66000:
            second_step = (66000 - 33000) * (1 - 0.42)
            third_step = (bruto_salary - 66000) * (1 - 0.52)
        else:
            second_step = (bruto_salary - 33000) * (1 - 0.42)
    return (first_step + second_step + third_step + without_tax)/12




