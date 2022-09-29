my_name = "İbrahim"
my_surname = "Cebe"
my_age = 22
Id_Number = 12344321
where_i_live = "Turkey"
health_insurance = True

print(f"My name is {my_name} {my_surname} I am {my_age} years old, I live in{where_i_live}")
# formatlı string literals” veya “f-strings”
# F-dizeleri, değişkenler veya matematiksel işlemler gibi Python ifadelerini gömmek
# için kısa ve kullanışlı bir yol sağlar.
item_list = ['laptop', 'Headset', 'Second monitor', 'mousepad', 'usb driver', 'External Driver']

print(item_list)
mandatory_item_list = item_list[0:3]
optional_item_list = item_list[3:6]
print(mandatory_item_list)
print(optional_item_list)

limit = 5000
price_sheet = {
    'laptop': 1500,
    'Headset': 100,
    'Second monitor': 200,
    'mousepad': 50,
    'usb driver': 70,
    'External Driver': 250
}
cart = []


def add_to_cart(item, quantity):
    # append ekleme için kullanılır
    cart.append((item, quantity))
    # remove çıkarmak için kullanılır
    item_list.remove(item)


def create_invocel():
    total_amount_inc_tax = 0
    for item, quantity in cart:
        price = price_sheet[item]
        tax = 0.25 * price
        total = (tax + price) * quantity
        total_amount_inc_tax += total
        print('Item:', item, '\t', 'Price:', price, '\t', 'Quantity:', quantity, '\t', 'Tax:', tax, '\t', 'Total:',
              total, '\n')

    print("After the taxes are applied the total amount is:", '\t', total_amount_inc_tax)
    return total_amount_inc_tax


def checkout():
    global limit
    total_amount = create_invocel()
    if limit == 0:
        print("you dont have any budget")
    elif total_amount > limit:
        print("The amount you have to pay is above the spending limit. You havte yo drop some items.")
    else:
        limit -= total_amount
        print(f"The total amount(incl. taxes) you have paid is {total_amount}. You have  {limit} dollars left")


add_to_cart("laptop", 1)
add_to_cart("Headset", 8)
add_to_cart("Second monitor", 1)
add_to_cart("mousepad", 1)
add_to_cart("usb driver", 2)
add_to_cart("External Driver", 4)

checkout()


