COMBINATIONS_COUNT = 3**9
CODE_TO_OPERATION = {"0": "+", "1": "-", "2": ""}


def convert_10_to_3(num: int) -> str:
    """
    Converts integer number into ternary number string.
    """
    if num < 0:
        raise ValueError("Can not process negative number")

    digits = []
    while num >= 3:
        num, modulo = num // 3, num % 3
        digits.append(str(modulo))
    digits.append(str(num))

    return "".join(reversed(digits))


class Solution:
    def find_combinations_sum_up_to_200():
        combinations = []

        for i in range(COMBINATIONS_COUNT):
            operation_codes = convert_10_to_3(i).zfill(9)
            # print(operation_codes)

            equation = []
            for digit, operation_code in zip(range(9, 0, -1), operation_codes):
                operation = CODE_TO_OPERATION.get(operation_code)

                equation.append(str(digit) + operation)
            equation = "".join(equation) + "0"

            if eval(equation) == 200:
                combinations.append(equation)

        return combinations


if __name__ == "__main__":
    solution = Solution.find_combinations_sum_up_to_200()
    assert len(solution) == 5
    print(*solution, sep="\n")
