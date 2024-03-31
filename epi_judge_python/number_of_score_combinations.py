from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # TODO - you fill in here.
    """
    DP solution 만들기
    - subproblem 의 최적 결과를 이용해 주어진 instance 의 solution 을 찾아야 한다.
    - subproblem 정의
        - DP[i] -> i 를 만들 수 있는 combination 수
        - 문제? 2 3 / 3 2 를 걸러낼 수없다.
        - 결국 cache 에 각 score 별 사용 횟수가 들어가야 함?
        - DP[i][j] -> i 번째 score 까지 고려했을 때 j 점을 만들 수 있는 경우의 수 (2, 2/3, 2/3/7 . 순서가 바뀌어도 되나?)
        - DP[i][j] = DP[i-1][j] + sum(DP[i][j- n*score[i]] for n in range(1 .. ) if j - n*score[i] >= 0)
    Args:
        final_score:
        individual_play_scores:

    Returns:
    """

    dp = [
        [0] * (final_score + 1),
        [0] * (final_score + 1),
    ]

    dp[0][0] = 1
    dp[1][0] = 1

    for i in range(len(individual_play_scores)):
        dp_idx = i % 2
        dp_prev_idx = abs(dp_idx - 1)

        dp_cur = dp[dp_idx]
        dp_prev = dp[dp_prev_idx]

        score = individual_play_scores[i]

        for j in range(final_score + 1):
            dp_cur[j] = dp_prev[j]

            multiplier = 1
            while j - multiplier * score >= 0:
                dp_cur[j] += dp_prev[j - multiplier * score]
                multiplier += 1

    return dp_cur[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
