import argparse


def read_score(label: str) -> int:
    while True:
        raw = input(f"{label} (1-5): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= 5:
            return int(raw)
        print("Valeur invalide. Entrez un nombre entre 1 et 5.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculateur de risque (Impact x Probabilite)")
    parser.add_argument("--impact", type=int, help="Impact (1-5)")
    parser.add_argument("--prob", type=int, help="Probabilite (1-5)")
    args = parser.parse_args()

    impact = args.impact if args.impact and 1 <= args.impact <= 5 else read_score("Impact")
    prob = args.prob if args.prob and 1 <= args.prob <= 5 else read_score("Probabilite")
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
