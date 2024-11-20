def can_reach_on_time(test_cases):
    results = []
    for x  in test_cases:
        if x >= 30:
            results.append("YES")
        else:
            results.append("NO")
    return results
t = int(input())
test_cases= [int(input()) for _ in range(t)]
results = can_reach_on_time(test_cases)
for result in results:
    print(result)
