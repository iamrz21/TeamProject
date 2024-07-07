# Mohammad Reza Zarei

def menu_dict_generator(x):
    menu_dict = dict(x.split() for x in x.split(','))
    return menu_dict

def order_dict_generator(y):
    order_dict = {}
    order_inp = y.split(',')
    for i in order_inp:
        order, order_count = i.split()
        if order not in order_dict:
            order_dict[order] = int(order_count)
        else:
            order_dict[order] += int(order_count)
    return order_dict

menu_inp = input()
menu_dict = menu_dict_generator(menu_inp)
order_list = []
while True:
    order_inp = input()
    if order_inp == 'end':
        break
    else:
        order_dict = order_dict_generator(order_inp)
        order_list.append(order_dict)

sale_dict = {}
for ordered, price in menu_dict.items():
    sale_dict[ordered] = 0.0
    for order in order_list:
        if ordered in order:
            number = order[ordered]
            sale_dict[ordered] += float(price) * number

for food, sales in sale_dict.items():
    print(f'{food} {round(sales, 2)}')
