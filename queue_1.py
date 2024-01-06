class Queue:

    def __init__(self):
        # Для хранения элементов применяем список.
        self.__items = []

    def push(self, item):
        """Добавить элемент в очередь."""
        # Добавляем элемент не в конец списка,
        # а в начало - на место элемента с индексом 0.
        self.__items.insert(0, item)

    def pop(self):
        """Вернуть элемент из очереди."""
        return self.__items.pop()

    def peek(self):
        """Вернуть последний элемент, но не удалять его из очереди."""
        return self.__items[-1]

    def size(self):
        """Вернуть размер очереди."""
        return len(self.__items)


def main():
    pass


if __name__ == '__main__':
    main()
    