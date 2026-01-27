import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit S3 (buckets publics)")
    parser.add_argument("--input", default="buckets.sample.json", help="JSON de demo")
    parser.add_argument("--offline", action="store_true", help="Mode demo sans AWS")
    args = parser.parse_args()

    if args.offline:
        with open(args.input, "r", encoding="utf-8") as handle:
            buckets = json.load(handle)
        for bucket in buckets:
            status = "PUBLIC" if bucket.get("public") else "PRIVE"
            print(f"{bucket.get('name', 'unknown')}: {status}")
        return

    try:
        import boto3  # type: ignore
    except Exception:
        print("Boto3 requis. Installez: pip install boto3")
        print("Astuce: relancez avec --offline pour une demo.")
        return

    s3 = boto3.client("s3")
    buckets = s3.list_buckets().get("Buckets", [])
    for bucket in buckets:
        name = bucket["Name"]
        acl = s3.get_bucket_acl(Bucket=name)
        grants = acl.get("Grants", [])
        public = any(
            g.get("Grantee", {}).get("URI", "").endswith("AllUsers") for g in grants
        )
        status = "PUBLIC" if public else "PRIVE"
        print(f"{name}: {status}")


if __name__ == "__main__":
    main()
