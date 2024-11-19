A = int(input().strip())
if 1 <= A <= 12:
    if 3 <= A <= 5:
        print("Spring")
    elif 6 <= A <= 8:
        print("Summer")
    elif 9 <= A <= 11:
        print("Autumn")
    else:  # December, January, February
        print("Winter")
else:
    print("Invalid")
