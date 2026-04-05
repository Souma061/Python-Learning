users = [
    {"id": 1, "total" : 100, "coupon": "P100"},
    {"id": 2, "total" : 200, "coupon": "P200"},
    {"id": 3, "total" : 300, "coupon": "P300"}
]


discounts = {
  "P100": (0.2, 0),
  "P200": (0.2, 0),
  "P300": (0.2, 10)
}


for user in users:
    percent,flat = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + flat
    final_price = user["total"] - discount
    print(f"User {user['id']} gets a discount of {discount} and has to pay {final_price}")
