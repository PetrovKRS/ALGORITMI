# 104040445

def sorting_by_template(n, m, list_n, list_m):
    if (
            len(list_n) == n
            and len(list_m) == m
    ):
        index = 0
        # сортировка по шаблону.
        for i in range(len(list_m)):
            for j in range(len(list_n)):
                current = list_n[j]
                if current == list_m[i]:
                    k = j
                    while k > index:
                        list_n[k] = list_n[k - 1]
                        k -= 1
                    list_n[index] = current
                    index += 1
        # сортировка остатка по возрастанию.
        for i in range(index, len(list_n)):
            current = list_n[i]
            prev = i - 1
            while prev >= index and list_n[prev] > current:
                list_n[prev + 1] = list_n[prev]
                prev -= 1
            list_n[prev + 1] = current
    return list_n


if __name__ == '__main__':
    try:
        nn = int(input())
        list_nn = list(map(int, input().split()))
        mm = int(input())
        list_mm = list(map(int, input().split()))
    except EOFError:
        list_mm = []
    print(
        ' '.join(
            str(i) for i in sorting_by_template(nn, mm, list_nn, list_mm)
        )
    )
