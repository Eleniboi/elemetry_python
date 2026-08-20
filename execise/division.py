def division(a: int, b: int) -> float | int:
    if b == 0:
       return print(f"{a}  can't be divisible by {b}")
    return a / b


def main() -> float | int:
    print(division(10, 5))

if __name__ == "__main__":
    main()