# Perform inner join on Employee and Department tables. Get the max salary and return only the rows that
# have max salary.

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', how='inner')
    max_salary = df.groupby('departmentId')['salary'].transform('max')
    df = df[df['salary'] == max_salary]
    return (df[['name_y', 'name_x', 'salary']]
            .rename(columns= {'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'}))