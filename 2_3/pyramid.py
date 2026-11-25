def print_pyramid(n):
    """높이 n인 가운데 정렬 별 피라미드를 출력합니다."""
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)


if __name__ == "__main__":
    try:
        n = int(input("피라미드의 높이를 입력하세요: "))
        if n <= 0:
            print("1 이상의 양의 정수를 입력해주세요.")
        else:
            print_pyramid(n)
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
