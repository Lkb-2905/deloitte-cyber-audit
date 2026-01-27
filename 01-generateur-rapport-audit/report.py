import argparse
from datetime import datetime, timezone


TEMPLATE = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ font-family: Arial, sans-serif; margin: 40px; }}
    h1 {{ color: #1a1a1a; }}
    .finding {{ margin-bottom: 16px; padding: 12px; border: 1px solid #ddd; }}
    .severity {{ font-weight: bold; }}
  </style>
</head>
<body>
  <h1>Rapport d'audit</h1>
  <p>Date: {date}</p>
  {findings}
</body>
</html>
"""


def render_findings(items: list) -> str:
    blocks = []
    for item in items:
        blocks.append(
            f"<div class='finding'><div class='severity'>{item['severity']}</div>"
            f"<div>{item['title']}</div><div>{item['desc']}</div></div>"
        )
    return "\n".join(blocks)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generateur rapport audit (HTML/PDF)")
    parser.add_argument("--output", default="report.html")
    args = parser.parse_args()

    findings = [
        {"title": "Faille XSS", "severity": "Eleve", "desc": "Injection possible via champ commentaire."},
        {"title": "SSL faible", "severity": "Moyen", "desc": "TLS 1.0 active sur le serveur."},
    ]
    html = TEMPLATE.format(date=datetime.now(timezone.utc).date(), findings=render_findings(findings))
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(html)
    print(f"Rapport genere: {args.output}")


if __name__ == "__main__":
    main()
