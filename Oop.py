class Company():
    def __init__(self, employee_name,department, starting_year, salary):
        self.employee_name = employee_name
        self.department = department
        self.starting_year = starting_year
        self.salary = salary


employee_1 = Company("Ben","sales",2020,5000)

print(employee_1.employee_name)
print(employee_1.department)
print(employee_1.starting_year)
print(employee_1.salary)
