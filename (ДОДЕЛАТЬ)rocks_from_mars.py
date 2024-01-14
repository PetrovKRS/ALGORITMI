def rocks_from_mars(n: int, orders: list[int], m: int, delivered_orders: list[int]):
    orders.sort(reverse=True)
    delivered_orders.sort(reverse=True)
    j = 0
    i = 0
    while i < m - 1:
        if delivered_orders[i] >= orders[j]:
            orders.remove(orders[j])
            delivered_orders.remove(delivered_orders[i])
            rocks_from_mars(len(orders), orders, len(delivered_orders), delivered_orders)
        elif (
                delivered_orders[i] < orders[j]
                and j < n - 1
        ):
            j += 1
        else:
            i += 1

    return len(orders)


if __name__ == '__main__':
    # n: int = int(input())
    # orders: list[int] = list(map(int, input().split()))
    # m: int = int(input())
    # delivered_orders: list[int] = list(map(int, input().split()))
    n = 10
    orders = [8, 5, 5, 8, 6, 9, 8, 2, 4, 7]
    m = 8
    delivered_orders = [9, 8, 1, 1, 1, 5, 10, 8]
    rocks_from_mars(n, orders, m, delivered_orders)
