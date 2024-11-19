bill_amount = float(input())
discount_10_percent = bill_amount * 0.10
discount_flat_100 = 100
max_discount = max(discount_10_percent, discount_flat_100)
amount_to_pay = bill_amount - max_discount
print(int(amount_to_pay))
