X, Y = map(int, input().strip().split())
if 1 <= X <= 100000 and 1 <= Y <= 100000:
    max_chocolates = X // Y
    print(max_chocolates)
else:
    print("Invalid input. X and Y must be between 1 and 100000.")
