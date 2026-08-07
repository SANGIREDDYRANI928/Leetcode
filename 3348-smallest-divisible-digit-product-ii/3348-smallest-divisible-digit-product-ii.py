class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        A = B = C = D = 0
        tt = t
        while tt % 2 == 0: tt //= 2; A += 1
        while tt % 3 == 0: tt //= 3; B += 1
        while tt % 5 == 0: tt //= 5; C += 1
        while tt % 7 == 0: tt //= 7; D += 1
        if tt != 1:
            return "-1"

        n = len(num)
        digs = [int(c) for c in num]

        exp = {1:(0,0,0,0), 2:(1,0,0,0), 3:(0,1,0,0), 4:(2,0,0,0),
               5:(0,0,1,0), 6:(1,1,0,0), 7:(0,0,0,1), 8:(3,0,0,0), 9:(0,2,0,0)}

        pre2 = [0]*(n+1); pre3 = [0]*(n+1); pre5 = [0]*(n+1); pre7 = [0]*(n+1)
        for i in range(n):
            e2, e3, e5, e7 = exp.get(digs[i], (0,0,0,0))
            pre2[i+1] = pre2[i] + e2
            pre3[i+1] = pre3[i] + e3
            pre5[i+1] = pre5[i] + e5
            pre7[i+1] = pre7[i] + e7

        # f[x][y] = min digits (from {2,3,4,6,8,9}) to reach >=x units of 2 and >=y units of 3
        f = [[0]*(B+1) for _ in range(A+1)]
        options = [(1,0),(0,1),(2,0),(1,1),(3,0),(0,2)]
        for x in range(A+1):
            for y in range(B+1):
                if x == 0 and y == 0:
                    continue
                best = float('inf')
                for dx, dy in options:
                    nx, ny = max(0, x-dx), max(0, y-dy)
                    if (nx, ny) == (x, y):
                        continue
                    best = min(best, f[nx][ny] + 1)
                f[x][y] = best

        def needed(r2, r3, r5, r7):
            return r5 + r7 + f[r2][r3]

        def greedy_suffix(r2, r3, r5, r7, length):
            res = []
            cr2, cr3, cr5, cr7 = r2, r3, r5, r7
            rem = length
            for _ in range(length):
                rem -= 1
                for dcand in range(1, 10):
                    e2, e3, e5, e7 = exp[dcand]
                    nr2, nr3 = max(0, cr2-e2), max(0, cr3-e3)
                    nr5, nr7 = max(0, cr5-e5), max(0, cr7-e7)
                    if needed(nr2, nr3, nr5, nr7) <= rem:
                        res.append(str(dcand))
                        cr2, cr3, cr5, cr7 = nr2, nr3, nr5, nr7
                        break
            return ''.join(res)

        # Case 0: num itself
        if 0 not in digs and pre2[n] >= A and pre3[n] >= B and pre5[n] >= C and pre7[n] >= D:
            return num

        p_min = n
        for i, d in enumerate(digs):
            if d == 0:
                p_min = i
                break

        start_i = min(n-1, p_min)
        found_i = found_v = -1
        for i in range(start_i, -1, -1):
            pe2, pe3, pe5, pe7 = pre2[i], pre3[i], pre5[i], pre7[i]
            L = n - 1 - i
            for v in range(digs[i] + 1, 10):
                e2, e3, e5, e7 = exp[v]
                r2 = max(0, A - pe2 - e2); r3 = max(0, B - pe3 - e3)
                r5 = max(0, C - pe5 - e5); r7 = max(0, D - pe7 - e7)
                if needed(r2, r3, r5, r7) <= L:
                    found_i, found_v = i, v
                    break
            if found_i != -1:
                break

        if found_i != -1:
            i, v = found_i, found_v
            pe2, pe3, pe5, pe7 = pre2[i], pre3[i], pre5[i], pre7[i]
            e2, e3, e5, e7 = exp[v]
            r2 = max(0, A - pe2 - e2); r3 = max(0, B - pe3 - e3)
            r5 = max(0, C - pe5 - e5); r7 = max(0, D - pe7 - e7)
            L = n - 1 - i
            return num[:i] + str(v) + greedy_suffix(r2, r3, r5, r7, L)

        Lmin = needed(A, B, C, D)
        L2 = max(n + 1, Lmin)
        return greedy_suffix(A, B, C, D, L2)