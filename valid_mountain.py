def valid_mountain_array():
    data = input().split()
    data = list(map(int, data))
    top_mountain = 0
    if len(data) >= 3:
        for i in range(len(data) - 1):
            if data[i] < data[i + 1]:
                top_mountain = i + 1
            elif data[i] == data[i + 1] or i == 0:
                return False
            else:
                for j in range(top_mountain, len(data) - 1):
                    if data[j] < data[j + 1]:
                        return False
                return True
    return False


if __name__ == '__main__':
    print(valid_mountain_array())
