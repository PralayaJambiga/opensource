N = int(input()) 
k = int(input()) 
mask = 1 << (k - 1)
if N & mask:
    print("true")
else:
    print("false")
