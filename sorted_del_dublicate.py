def sort_del_duplicate():
    element_count = int(input())
    ordered_list = input().split()
    ordered_list = list(map(int, ordered_list))
    ordered_list.sort()
    ordered_list = list(map(str, ordered_list))
    for item in ordered_list:
        if item == '_':
            break
        if ordered_list.count(item) > 1:
            for i in range(ordered_list.count(item) - 1):
                ordered_list.remove(item)
                ordered_list.append('_')
    print(' '.join(ordered_list))


if __name__ == '__main__':
    sort_del_duplicate()
    