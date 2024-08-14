customer_type = "loyal"
total_purchase = 120

if customer_type == "loyal":
    if total_purchase > 100:
        print("Eligible for 20% discount")
    else:
        print("Eligible for 10% discount")
else:
    if total_purchase > 100:
        print("Eligible for 5% discount")
    else:
        print("No discount")
