#! /usr/bin/python
import math, random

origins = {
    '1' : 0.95,
    '2' : 1.45,
    '3' : 0.45,
    '4' : 1.95
}

for i in range (1,501):
    
    customer_id = random.randint(1,999)
    t_number = random.randint(1,5)
    d_booked = random.randint(1,80)
    d_booking = d_booked + random.randint(0,16)

    origin = random.choice(origins.keys())
    origin_fee = origins[origin]

    n_people = random.randint(1,4)
    fee = n_people * origin_fee
    no_show = 0
    if random.random() < .15:
        no_show = 1

    print "%d,%d,%d,%d,%d,%s,%.2f,%d,%d" % (i, customer_id, t_number, d_booked, d_booking, origin, fee, n_people, no_show)
    