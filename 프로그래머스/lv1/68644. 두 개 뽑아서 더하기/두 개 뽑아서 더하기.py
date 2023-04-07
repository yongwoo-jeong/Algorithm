def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            summed = numbers[i]
            if j == i:
                continue
            summed += numbers[j]
            answer.append(summed)

    return sorted(list(set(answer)))