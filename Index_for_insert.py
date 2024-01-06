def index_for_insert():
    ordered_list = input().split()
    ordered_list = list(map(int, ordered_list))
    ordered_list.sort()
    element = int(input())
    left = 0
    right = len(ordered_list) - 1
    if ordered_list.count(element) > 1:
        return ordered_list.index(element)
    else:
        while left <= right:
            mid = (left + right) // 2
            if ordered_list[mid] == element:
                return mid
            if ordered_list[mid] < element:
                left = mid + 1
            if ordered_list[mid] > element:
                right = mid - 1
        return left


if __name__ == '__main__':
    print(index_for_insert())
