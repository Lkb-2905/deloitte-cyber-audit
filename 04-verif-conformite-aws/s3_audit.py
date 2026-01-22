def main() -> None:
    try:
        import boto3  # type: ignore
    except Exception:
        print("Boto3 requis. Installez: pip install boto3")
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
