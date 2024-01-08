# work: 104385497
def sort_merging_blocks(n, array):
    mass = []
    mass_i = []
    r = 0
    i = 0
    while i < n:
        if len(mass) < 1:
            if (
                    0 in mass_i
                    and max(mass_i) == len(mass_i) - 1
            ):
                r += len(mass_i)
                mass.append(mass_i)
                mass_i = []
            else:
                mass_i.append(array[i])
                i += 1
        else:
            if (
                    r in mass_i
                    and array[i] > max(mass_i)
            ):
                r += len(mass_i)
                mass.append(mass_i)
                mass_i = []
            else:
                mass_i.append(array[i])
                i += 1
    mass.append(mass_i)
    return len(mass)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(sort_merging_blocks(n, arr))
