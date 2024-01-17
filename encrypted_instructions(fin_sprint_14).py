# номер успешной посылки: 105159271

def encripted_instructions(
        instructions: str,
        brackets_idx: list,
        i: int,
        rate: str,
        mark_left: int,
        mark_right: int
) -> str:
    while i < len(instructions):
        if (
                mark_left != 0
                and mark_right != 0
        ):
            j = mark_left - 1
            while (
                    instructions[j].isdecimal()
                    and j >= 0
            ):
                j -= 1
            rate = instructions[j + 1:mark_left]
            instructions = (
                            instructions[:mark_left - len(rate)]
                            + int(rate) * instructions[mark_left + 1: mark_right]
                            + instructions[mark_right + 1:]
            )
            brackets_idx.pop(-1)
            if len(brackets_idx) == 0:
                i = mark_right + 1
            else:
                i = brackets_idx.pop()
            mark_left = mark_right = 0
            rate = ''
        elif instructions[i] == '[':
            mark_left = i
            brackets_idx.append(i)
            i += 1
            return encripted_instructions(
                instructions, brackets_idx, i, rate, mark_left, mark_right
            )
        elif instructions[i] == ']':
            mark_right = i
        else:
            i += 1
    return instructions


if __name__ == '__main__':
    instructions: str = input()
    instructions_new: str = ''
    brackets_idx: list[int] = []
    i: int = 0
    rate: str = ''
    mark_left: int = 0
    mark_right: int = 0
    print(encripted_instructions(
            instructions, brackets_idx, i, rate, mark_left, mark_right
        )
    )
