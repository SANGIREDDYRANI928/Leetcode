from bisect import bisect_right

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = []

        for i in range(n):
            arr.append([
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            ])

        # Sort according to left endpoint
        arr.sort()

        # All left endpoints
        starts = []
        for x in arr:
            starts.append(x[0])

        # next[i] = first interval whose left > arr[i][1]
        next_index = [0] * n

        for i in range(n):
            next_index[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = best answer using intervals from i onwards
        # choosing at most k intervals
        #
        # Each value = (score, list_of_indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            for k in range(1, 5):

                # Option 1: don't take current interval
                best_score = dp[i + 1][k][0]
                best_list = dp[i + 1][k][1]

                # Option 2: take current interval
                take_score = arr[i][2] + dp[next_index[i]][k - 1][0]

                take_list = [arr[i][3]] + dp[next_index[i]][k - 1][1]

                # Sort because answer must be lexicographically smallest
                take_list.sort()

                if take_score > best_score:
                    best_score = take_score
                    best_list = take_list

                elif take_score == best_score:
                    if take_list < best_list:
                        best_list = take_list

                dp[i][k] = (best_score, best_list)

        return dp[0][4][1]