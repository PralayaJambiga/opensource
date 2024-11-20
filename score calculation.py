def calculate_scores(test_cases):
    results = []
    for x, n in test_cases:
        points_per_test_case = x // 10
        score = points_per_test_case * n
        results.append(score)
    return results
t = int(input())
test_cases = [tuple(map(int, input().split())) for  _ in range(t)]
scores = calculate_scores(test_cases)
for score in scores:
    print(score)
