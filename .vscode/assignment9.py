count=100
while(count > 0):
    print(count)
    if count % 3 == 0 and count % 5 == 0:
        print("fizz buzz")

    elif count % 3 == 0:
        print("fizz")
    elif count % 5 == 0:
        print("buzz")
    count = count -1