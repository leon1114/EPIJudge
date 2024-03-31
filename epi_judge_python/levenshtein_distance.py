from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    # TODO - you fill in here.
    """
    DP[i][j] = A[:i], B[:j] 까지 고려 했을 때의 레벤슈타인 거리
    DP[i][j] = DP[i-1][j-1] + A[i] != B[j]
    init -> 각 dimension 의 0 은 empty string 을 표현. 0부터 1씩 단조 증가하는 값으로 채워넣기


    """
    dp = []
    for _ in range(len(A) + 1):
        dp.append([0] * (len(B) + 1))

    for i in range(len(A) + 1):
        dp[i][0] = i

    for j in range(len(B) + 1):
        dp[0][j] = j

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            dp[i][j] = min(
                dp[i-1][j-1] + (A[i-1] != B[j-1]),
                dp[i][j-1] + 1,
                dp[i-1][j] + 1
            )

    return dp[-1][-1]


if __name__ == '__main__':
    # print(levenshtein_distance('saturday', 'sunday'))
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
