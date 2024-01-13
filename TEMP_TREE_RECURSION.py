# Двоичная конструкция дерева
class BinTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Операционная функция
def count_Note(btree):
    if btree == None:
        return 0
        # еще:  # Рекурсивное решение
    return 1 + count_Note(btree.left) + count_Note(btree.right)


btree = BinTree(
    1,
    BinTree(
        2,
        BinTree(3)
    ),
    BinTree(
        5,
        BinTree(
            6,
            BinTree(9)
        )
    )
)


# Предзаказ рекурсивного обхода
def traversal(btree):
    # если
    # btree
    # не
    # None
    # и
    # btree.data
    # не
    # None:  # потому что конечным элементом является None
    print(btree.data)
    traversal(btree.left)
    traversal(btree.right)


traversal(btree)
