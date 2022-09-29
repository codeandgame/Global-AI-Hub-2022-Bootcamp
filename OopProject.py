class HealthInsurance:
    def __init__(self,company_name,foundaiton_year,founder_name,company_slogan,num_of_employee,num_of_clients):
        self.company_name = company_name
        self.foundation_year = foundaiton_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.num_of_employee = num_of_employee
        self.num_of_clients = num_of_clients

    def print_report(self):
        print(f"""The company{self.company_name} was founded is {self.foundation_year}.
        The founder of the company is {self.founder_name}.
        Company slogan: {self.company_slogan}
        Number of employees: {self.num_of_employee}
        Number of clients: {self.num_of_clients}""")

    def sub_health_insurance(self,age,chronic_disase,income):
        if age >= 60 and chronic_disase == True and income < 6000:
            print("We are sorry! you are not eligible for supplemental health insurance.")
        elif age < 60 and income >= 6000 or chronic_disase == False:
            print("Congratulations you can get supplemental health insurance")

    def update_num_clients(self,new_number):
        self.num_of_clients = new_number
        print(f"Number of clients has been changed to {self.num_of_clients}!")


HI_company1 = HealthInsurance('Healty',2012,'Bob Mayer','We care for you',3500,13230)

HI_company1.sub_health_insurance(36,True,6000)
HI_company1.update_num_clients(13231)
HI_company1.print_report()
