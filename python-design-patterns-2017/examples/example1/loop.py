for item in items:
    if is_for_sale(item):
        cost = compute_cost(item)
        if cost <= wallet.money:
            buy(item)


# Better


for item in items:
    if not is_for_sale(item):
        continue
    cost = compute_cost(item)
    if cost > wallet.money:
        continue
    buy(item)


# By Brandon Rhodes
# http://rhodesmill.org/brandon/slides/2012-07-pyohio/
