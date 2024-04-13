from data import order
#CALCULATION ORDER CLIENT
cost ={
    "amount":0,
    "currency":"MDL"
}

for item in range(len(order["items"])):
    cost["amount"] +=order["items"][item]["price"]["amount"] * order["items"][item]["quantity"]
#PRINT ORDER CLIENT DETAIL INFORMATION
print("ORDER INFORMATION:")
print("="*30)
print(order["client"]["name"])
print(order["client"]["phone"])
print(f"Placed Order on: {order['placed_on'][-8:-3]}")
#Rezolvarea pe acasa
print("="*30)
print("ITEMS:")
for item in range(len(order["items"])):
    print(f"{order['items'][item]['quantity']} {order['items'][item]['name']} x {order['items'][item]['price']['amount']} {order['items'][item]['price']['currency']} = {order['items'][item]['price']['amount'] * order['items'][item]['quantity']} {order['items'][item]['price']['currency']}")
print("="*30)
print(f"TOTAL ITEMS COST:{cost['amount']} {cost['currency']}")
print("="*30)
print("ADITIONAL DATA:")
print(f"ORDER DELIVERED: {order['delivery']['delivery_at'][-8:-3]} by {order['delivery']['delivery_by']}")
print("="*30)