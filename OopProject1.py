class Logistics:
    def __init__(self,company_name,foundation_year,founder_name,company_slogan,inventory_space):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.inventory_space = inventory_space

    def print_report(self):
        print(f"""
        TThe company name is {self.company_name} and was founded in {self.foundation_year}.
        The founder of the company is {self.founder_name}.
        Company slogan: {self.company_slogan}
        Inventory space of the company: {self.inventory_space}""")

    def update_inventory_space(self,new_storge_space):
        self.inventory_space = new_storge_space / 2
        print(f"Inventory space has been changed to {self.inventory_space}")

logistic_company1 = Logistics('LogCom',1990,'Laura McCartey', 'There is no place we cannot reach',5000)

logistic_company1.update_inventory_space(4500)
logistic_company1.print_report()

class Trading:
    def __init__(self,company_name,foundation_year,founder_name,company_slogan,sales,expenses,revenue):
        self.company_name=company_name
        self.foundation_year = foundation_year
        self.founder_name=founder_name
        self.company_name = company_name
        self.company_slogan=company_slogan
        self.sales=sales
        self.expenses=expenses
        self.revenue=revenue

    def print_report(self):
        print(f"""
        The company name is {self.company_name} and was founded in {self.foundation_year}.
        The founder of the company is {self.founder_name}
        Company slogan: {self.company_slogan}
        Total sales: {self.sales}
        Total expenses: {self.expenses}
        Total revenue: {self.revenue}""")

    def update_sales_and_expenses(self,new_sales,new_expenses):
        self.sales+=new_sales
        self.expenses+=new_expenses
        print("Sales and expenses are update")

    def calculate_revenue(self):
        self.revenue=self.sales-self.expenses
        print(f"The revenue of the company is: {self.revenue}")

trading_company1 = Trading('TraCom',2005, 'Chong Wu','We revolutionize trading',3850,1720,1838)

trading_company1.update_sales_and_expenses(100,50)
trading_company1.calculate_revenue()
trading_company1.print_report()