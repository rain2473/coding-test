def solution(sequence):
    S = [0] * len(sequence)
    for i in range(len(sequence)):
        try:
            S[i] = S[i -1] + (-1) ** i * sequence[i]
        except:
            S[i] = sequence[i]
    answer = max(abs(min(S)),abs(max(S)), abs(min(S)-max(S)))
    return answer