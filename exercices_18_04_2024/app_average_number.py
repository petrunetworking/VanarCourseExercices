#Home Work Calculate and Display the average of numbers enters sequancialy from keyboard ontill the first negative
total = 0
count = 0

while True:
    digit = int(input("Enter digit: "))
    if digit >= 0:
        total += digit
        count += 1
        average = total / count
    else:
        break

    print(f"Average of Numbers entered is {average}")
