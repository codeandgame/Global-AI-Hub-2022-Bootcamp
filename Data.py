file= open('employee_revenue.txt','r')
data = file.read()
print(data)

lines= data.splitlines()

print("-------------------------------------")

string = lines[0]

string =string.strip(" ")
print(string)
print("-------------------------------------")

string = string.lower()
print(string)
print("-------------------------------------")

string=string.capitalize()
print(string)
print("-------------------------------------")

split_string = string.split("")
print(split_string)
print("------------------------212-------------")

name= split_string[0]
print(name)
print("-------------------------------------")

call_number = split_string[2]
print(call_number)
print("-------------------------------------")

for i in split_string:
    if "$" in i:
        average_deal_size = i.split("$")[0]

print(average_deal_size)
print("-------------------------------------")

dollars_index = split_string.index("dollars")
print(dollars_index)
print("-------------------------------------")

revenue_index = dollars_index-1
print(revenue_index)
print("-------------------------------------")

revenue=split_string[revenue_index]
print(revenue)
print("-------------------------------------")

print("Name:" ,name)
print("Number of calls:",call_number)
print("Average deal size:",average_deal_size)
print("Revenue:", revenue)
print("-------------------------------------")

print("Name type:",type(name))
print("Number of calls type:", type(call_number))
print("Average deal size type:", type(average_deal_size))
print("Revenue type:", type(revenue))
print("-------------------------------------")

average_deal_size = int(average_deal_size)
call_number = int(call_number)
revenue = int(revenue)
print("-------------------------------------")
print("Name type:",type(name))
print("Number of calls type:", type(call_number))
print("Average deal size type:", type(average_deal_size))
print("Revenue type:", type(revenue))

print("-------------------------------------")

names= []
call_numbers=[]
average_deal_sizes=[]
revenues=[]

for employee in lines:
    employee = employee.strip(" ")
    employee = employee.lower()
    employee = employee.capitalize()
    split_employee = employee.split(" ")
    name = split_employee[0]
    call_number = split_employee[2]

    for i in split_employee:
        if "$" in i:
            average_deal_size = i
    average_deal_size = average_deal_size.split("$")[0]

    dollars_index = split_employee.index("dollars")
    revenue_index = dollars_index-1
    revenue = split_employee[revenue_index]

    average_deal_size = int(average_deal_size)
    call_number = int(call_number)
    revenue = int(revenue)

    names.append(name)
    call_numbers.append(call_number)
    average_deal_sizes.append(average_deal_size)
    revenues.append(revenue)

print("Names:", names)
print("Number of calls:", call_numbers)
print("Average deal size:",average_deal_sizes)
print("Revenue:",revenues)
print("-------------------------------------")

names = []
call_numbers=[]
average_deal_sizes=[]
revenues=[]

def clean_extract(lines):
    for employee in lines:
        employee = employee.strip(" ")
        employee = employee.lower()
        employee = employee.capitalize()
        split_employee = employee.split(" ")
        name = split_employee[0]
        call_number = split_employee[2]

        for i in split_employee:
            if "$" in i:
                average_deal_size = i
        average_deal_size = average_deal_size.split("$")[0]

        dollars_index = split_employee.index("dollars")
        revenue_index = dollars_index - 1
        revenue = split_employee[revenue_index]

        average_deal_size = int(average_deal_size)
        call_number = int(call_number)
        revenue = int(revenue)

        names.append(name)
        call_numbers.append(call_number)
        average_deal_sizes.append(average_deal_size)
        revenues.append(revenue)

    return names,call_numbers,average_deal_sizes,revenues

names, call_numbers, average_deal_sizes, revenues = clean_extract(lines)
print("Names:", names)
print("Number of calls:", call_numbers)
print("Average deal size:",average_deal_sizes)
print("Revenue:",revenues)

print("-------------------------------------")

print(len(names))
print("-------------------------------------")

IDs = list(range(0,11))

print(IDs)
print("-------------------------------------")

print(len(IDs))
print("-------------------------------------")

dictionary1 = dict(zip(IDs,names)),
print(dictionary1)
print("-------------------------------------")

dictionary2 = dict(zip(revenues,names))
print(dictionary2)
print("---------------54----------------------")

sorted_dictionary = sorted(dictionary2)[0:3]
for i in sorted_dictionary:
    print(dictionary2[i])
print("-------------------------------------")

sorted_dictionary = sorted(dictionary2,reverse= True)[0:3]

for i in sorted_dictionary:
    print(dictionary2[i])

string1 = ["Merhaba AI Dünyası"]

string1 = string1.split("")
print(string1)

