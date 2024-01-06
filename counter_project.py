# 103986708
import time


def bidder_counter(bidders: list[int], tact: list[int]) -> int:

    def sort_bidders(bidder: int, bidders: list[int]):
        temp: list[int] = []
        if bidder < len(bidders):
            i = bidder
        else:
            i = 0
        while bidder != bidders[0]:
            temp.append(bidders[i])
            if len(temp) == len(bidders):
                bidders.clear()
                bidders.extend(temp)
                return bidders
            elif i == len(bidders) - 1:
                i = 0
            elif i != len(bidders):
                i += 1

    count: int = len(tact) % len(bidders)
    group: list[int] = []
    i: int = 0
    j: int = 0
    if len(bidders) == 1:
        return bidders[0]
    elif count > 0:
        while i < count:
            if len(tact) == 1:
                return bidders[-1]
            elif len(bidders) > len(tact):
                return len(tact) + 1
            elif j == len(bidders):
                j = 0
            else:
                group.append(bidders[j])
                j += 1
                i += 1
    else:
        group.append(bidders[-1])
    index: int = bidders.index(group[-1])
    bidders.remove(group[-1])
    sort_bidders(index, bidders)
    return bidder_counter(bidders, tact)


if __name__ == '__main__':
    start_time: time = time.time()
    N: int = int(input())
    K: int = int(input())
    N: list[int] = [i + 1 for i in range(N)]
    K: list[int] = [i + 1 for i in range(K)]
    print(bidder_counter(N, K))
    print(time.time() - start_time)
