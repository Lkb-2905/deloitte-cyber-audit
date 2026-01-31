# Deloitte - Cyber Audit (demo portfolio)

Objectif: proposer des mini-outils d'audit cyber utilisables en demo, avec
des sorties claires pour des captures d'ecran.

## Contenu
- `01-generateur-rapport-audit`: genere un rapport HTML d'audit.
- `02-decouverte-assets`: decouverte d'assets (mode offline possible).
- `03-calculateur-risque`: calcul Impact x Probabilite (CLI).
- `04-verif-conformite-aws`: audit S3 (mode offline possible).
- `05-simulateur-force-mdp`: estimation temps de craquage.

## Demarrage rapide (demos)
```
cd 01-generateur-rapport-audit
python report.py --output report.html

cd ../02-decouverte-assets
python assets_scan.py --target 192.168.1.0/24 --offline --output assets_report.csv

cd ../03-calculateur-risque
python risk_calc.py --impact 4 --prob 3

cd ../04-verif-conformite-aws
python s3_audit.py --offline --input buckets.sample.json

cd ../05-simulateur-force-mdp
python password_strength.py
```

## Captures conseillees
- `01-generateur-rapport-audit/report.html`
- `02-decouverte-assets/assets_report.csv`
- Terminal: score de risque + audit S3 + estimation de force.

## Dependances
Voir `requirements.txt`.

## Roadmap et suggestions
- `ROADMAP.md`
- `CODE_SUGGESTIONS.md`
