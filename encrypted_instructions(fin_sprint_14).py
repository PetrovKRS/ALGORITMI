# номер успешной посылки: 104898453
def encripted_instructions(instructions: str) -> str:
    i: int = 0
    rate: str = ''
    mark_left: int = 0
    mark_right: int = 0
    while i < len(instructions):
        if instructions.count('[') == 0:
            return instructions
        elif instructions[i] == '[':
            mark_left = i
            i += 1
        elif (
                mark_left != 0
                and mark_right != 0
                and instructions[mark_left + 1:mark_right].count('[') == 0
        ):
            j = mark_left - 1
            while (
                    instructions[j].isdigit()
                    and j >= 0
            ):
                rate = instructions[j:mark_left]
                j -= 1
            instructions: str = (
                            instructions[:mark_left - len(rate)]
                            + int(rate) * instructions[mark_left + 1: mark_right]
                            + instructions[mark_right + 1:]
            )
            mark_left = mark_right = i = 0
            rate = ''
            encripted_instructions(instructions)
        elif instructions[i] == ']':
            mark_right = i
        else:
            i += 1


if __name__ == '__main__':
    instructions: str = input()
    print(encripted_instructions(instructions))
