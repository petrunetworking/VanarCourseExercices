#Home Work Create an app that declares a list of friends initialy and lets you extend it using the keyboard inputs
#add every time a friend is added to the list display the number of friends

friends_list = ['Alice','Peter','Marie','Alexander']
while True:
    friend = input("Add to List New Friend:")
    friends_list.append(friend)
    print(f"Number of friends is:{len(friends_list)}")
    choice = input("You want to add New Friend(yes/no):")
    if choice == "yes":
        continue
    if choice == "no":
        break   