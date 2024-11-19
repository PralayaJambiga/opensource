X, N = map(int, input().split())
planes_needed = (N + 99) // 100
new_planes_needed = max(0, planes_needed - X)
print(new_planes_needed)
