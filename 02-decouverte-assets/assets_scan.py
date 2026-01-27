import argparse
import csv
import hashlib


def fake_hosts(target: str) -> list[tuple[str, str]]:
    base = "192.168.0"
    if target.count(".") >= 2:
        parts = target.split(".")
        base = ".".join(parts[:3])
    ip1 = f"{base}.10"
    ip2 = f"{base}.20"
    macs = []
    for ip in [ip1, ip2]:
        digest = hashlib.md5(ip.encode("utf-8")).hexdigest()
        mac = ":".join(digest[i : i + 2] for i in range(0, 12, 2))
        macs.append(mac)
    return [(ip1, macs[0]), (ip2, macs[1])]


def main() -> None:
    parser = argparse.ArgumentParser(description="Decouverte d'assets (ARP)")
    parser.add_argument("--target", default="192.168.1.0/24")
    parser.add_argument("--timeout", type=int, default=2)
    parser.add_argument("--output", help="Export CSV (ip,mac)")
    parser.add_argument("--offline", action="store_true", help="Mode demo sans reseau")
    args = parser.parse_args()

    results = []
    if args.offline:
        results = fake_hosts(args.target)
    else:
        try:
            from scapy.all import ARP, Ether, srp  # type: ignore
        except Exception:
            print("Scapy requis. Installez: pip install scapy")
            print("Astuce: relancez avec --offline pour une demo.")
            return

        packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=args.target)
        result = srp(packet, timeout=args.timeout, verbose=0)[0]
        results = [(received.psrc, received.hwsrc) for _, received in result]

    for ip, mac in results:
        print(f"{ip} {mac}")

    if args.output:
        with open(args.output, "w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["ip", "mac"])
            writer.writerows(results)
        print(f"Export CSV: {args.output}")


if __name__ == "__main__":
    main()
