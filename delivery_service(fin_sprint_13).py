# номер успешной посылки: 103952733
import time


def delivery_service(r_weights: list[int], plat_limit: int) -> int:
    """ Вычисляем кол-во платформ для роботов. """
    weights: list[int] = sorted(r_weights)
    platforms: int = 0
    left_idx: int = 0
    right_idx: int = len(weights) - 1
    if weights[-1] > plat_limit:
        raise ValueError(
            'Максимальный вес 1 робота не может быть '
            'больше лимита платформы!'
        )
    while left_idx <= right_idx:
        sum_left_right: int = (
                weights[left_idx]
                + weights[right_idx]
        )
        if sum_left_right <= plat_limit:
            left_idx += 1
        platforms += 1
        right_idx -= 1
    return platforms


if __name__ == '__main__':
    start_time = time.time()
    robots_weights: list[int] = list(map(int, input().split()))
    limit: int = int(input())
    print(delivery_service(robots_weights, limit))
    print(time.time() - start_time)
