#! /usr/bin/python
import math, random

# Item prices
items =  [
    12.95,
    18.95,
    1.50,
    6.50,
    2.25,
    2.95,
    3.95,
    4.50
]

random.seed(0)

self_id = 0
order_id = 1
for i in range(1, 1000):
    date_id = random.randint(1,96)
    customer_id = random.randint(1,20)
    staff_id = random.randint(1,4)
    table_number = random.randint(1,5)

    items_in_order = random.randint(1,3) * [1]
    items_in_order = [random.randint(0, len(items)-1) for _ in items_in_order]

    for item in items_in_order:
        item_id = item+1
        price = items[item]

        self_id += 1

        print "%d;%d;%d;%d;%d;%d;%d;%.2f" % (
            self_id, order_id, customer_id, staff_id,table_number,date_id, item_id, price)

    
    order_id += 1



