#Home Work Calculate and Display the sum of numbers enters sequancialy from keyboard ontill the first negative
result = 0
while True:
    digit = int(input("Enter digit:"))
    if digit > 0:
        result = digit + result
        print(result)
    else:
        break
    print(f"Sum of Numbers entered with you is {result}")