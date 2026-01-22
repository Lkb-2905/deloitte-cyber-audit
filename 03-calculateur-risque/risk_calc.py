def main() -> None:
    impact = int(input("Impact (1-5): "))
    prob = int(input("Probabilite (1-5): "))
    score = impact * prob

    if score >= 16:
        level = "critique"
    elif score >= 9:
        level = "eleve"
    elif score >= 4:
        level = "moyen"
    else:
        level = "faible"

    print(f"Score: {score} / Niveau: {level}")


if __name__ == "__main__":
    main()
