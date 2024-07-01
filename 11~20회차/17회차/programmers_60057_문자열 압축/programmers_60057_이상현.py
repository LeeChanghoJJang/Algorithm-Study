def solution(s):
    answer = float('inf')
    len_ = len(s)

    for i in range(1, len_ + 1):
        compressed = []
        prev_chunk = s[:i]
        count = 1

        for j in range(i, len_ + i, i):
            if prev_chunk == s[j : j + i]:
                count += 1
            else:
                compressed.append(f'{count}{prev_chunk}' if count != 1 else prev_chunk)
                prev_chunk = s[j : j + i]
                count = 1

        compressed = ''.join(compressed)
        answer = min(answer, len(compressed))

    return answer