import math


def entropy(length: int, charset: int) -> float:
    return length * math.log2(charset)


def crack_time(ent: float, guesses_per_sec: float = 1e9) -> float:
    return (2 ** ent) / guesses_per_sec


def main() -> None:
    for length in [4, 8, 12]:
        ent = entropy(length, 94)
        seconds = crack_time(ent)
        print(f"Longueur {length}: entropie {ent:.1f} bits, temps ~ {seconds:.2e} s")


if __name__ == "__main__":
    main()
