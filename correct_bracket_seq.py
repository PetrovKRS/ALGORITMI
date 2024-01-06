def is_correct_bracket_seq():
    """ Функция, которая принимает на вход скобочную последовательность и
    возвращает True, если последовательность правильная, и False —
    в остальных случаях.
    """
    seq = input()
    seq = list(seq)
    correct_bracket = ['{}', '[]', '()']
    if len(seq) == 0:
        return True
    else:
        i = 0
        while i < len(seq) - 1:
            seq_temp = seq[i] + seq[i + 1]
            if seq_temp in correct_bracket:
                del seq[i]
                del seq[i]
                i = 0
                if len(seq) == 0:
                    return True
            else:
                i += 1
        return False


if __name__ == '__main__':
    print(is_correct_bracket_seq())
