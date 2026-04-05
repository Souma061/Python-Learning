def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100


orders = [100,134,566]

for price in orders:
    final_amount = add_vat(price,18)
    print(f"original: {price}, Final with vat: {final_amount}")
