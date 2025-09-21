i = 0
user = int(input("Enter the size of the pattern:"))
while i < user:
    for j in range(user):
        print("*", end = "")
    print()
    i += 1